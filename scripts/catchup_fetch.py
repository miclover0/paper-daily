#!/usr/bin/env python3
"""
Catch-up script: Fetch historical ArXiv papers for missing dates.
Usage: python scripts/catchup_fetch.py --start=2026-06-16 --end=2026-07-04

Strategy: Bulk-fetch ALL papers from cs.CV/cs.LG/cs.AI/cs.RO sorted by
submittedDate descending, then group locally by published date.
This avoids unreliable submittedDate range queries in the ArXiv API.
"""

import sys
import os
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from collections import defaultdict

# Import existing module functions
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import daily_fetch as df

# Larger page size for bulk fetching
BULK_PAGE_SIZE = 200
BULK_MAX_PAGES = 80  # Safety limit: 80 * 200 = 16000 papers max


def fetch_all_papers_bulk(earliest_date, latest_date):
    """
    Bulk fetch all papers from the 4 categories sorted by submittedDate descending.
    Stop when we encounter papers older than earliest_date - 2 days.
    Return a dict: {date_str: [papers]} keyed by published date.
    """
    query = "(cat:cs.CV OR cat:cs.LG OR cat:cs.AI OR cat:cs.RO)"
    encoded_query = urllib.parse.quote(query, safe="")

    # Cutoff: stop fetching when papers are older than this
    cutoff_date = earliest_date - timedelta(days=3)
    cutoff_str = cutoff_date.strftime("%Y-%m-%d")
    df.log(f"  Bulk fetch cutoff: {cutoff_str} (earliest target: {earliest_date})")

    all_papers = []
    seen_ids = set()
    papers_by_date = defaultdict(list)

    for page in range(BULK_MAX_PAGES):
        start = page * BULK_PAGE_SIZE
        url = (
            f"{df.ARXIV_API_URL}?search_query={encoded_query}"
            f"&start={start}"
            f"&max_results={BULK_PAGE_SIZE}"
            f"&sortBy=submittedDate"
            f"&sortOrder=descending"
        )
        df.log(f"  Bulk API page {page+1} (offset={start})...")
        xml_text = df.safe_request(url)
        if not xml_text:
            df.log(f"  API request failed at page {page+1}, stopping")
            break

        batch = df.parse_arxiv_xml(xml_text)
        if not batch:
            df.log(f"  No more results at page {page+1}")
            break

        new_count = 0
        oldest_date_in_batch = None
        for p in batch:
            pid = p["arxiv_id"]
            if pid and pid not in seen_ids:
                seen_ids.add(pid)
                all_papers.append(p)
                new_count += 1

                pub_date = p["published"][:10] if p["published"] else ""
                if pub_date:
                    papers_by_date[pub_date].append(p)
                    if oldest_date_in_batch is None or pub_date < oldest_date_in_batch:
                        oldest_date_in_batch = pub_date

        df.log(f"  Page {page+1}: {len(batch)} papers, {new_count} new (total: {len(all_papers)})")

        if len(batch) < BULK_PAGE_SIZE:
            df.log(f"  Reached end of results at page {page+1}")
            break

        # Check if we've gone past the cutoff date
        if oldest_date_in_batch and oldest_date_in_batch < cutoff_str:
            df.log(f"  Oldest paper in batch: {oldest_date_in_batch} < cutoff {cutoff_str}, stopping")
            break

    # Also fetch today's papers from RSS as a supplement (more reliable for current day)
    df.log(f"  Also checking RSS feed for today's papers...")
    rss_papers = df.fetch_papers_from_rss()
    if rss_papers:
        today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        existing_ids = set(p["arxiv_id"] for p in all_papers)
        rss_new = 0
        for p in rss_papers:
            if p["arxiv_id"] not in existing_ids:
                papers_by_date[today_str].append(p)
                all_papers.append(p)
                existing_ids.add(p["arxiv_id"])
                rss_new += 1
        if rss_new:
            df.log(f"  RSS supplement: +{rss_new} new papers for today")

    df.log(f"  Total unique papers fetched: {len(all_papers)}")
    df.log(f"  Dates covered: {sorted(papers_by_date.keys())}")

    return papers_by_date


def process_date(target_date, papers):
    """Process a single date through the full pipeline."""
    date_str = target_date.strftime("%Y-%m-%d")
    df.log(f"\n{'=' * 60}")
    df.log(f"Paper digest - {date_str}")
    df.log(f"{'=' * 60}")

    if not papers:
        df.log(f"  No papers for {date_str} (likely weekend)")
        groups = {"A": [], "B": [], "C": []}
        html_papers = []
        featured_papers = None
    else:
        df.log(f"  Got {len(papers)} papers for this date")

        # Step 1: Keyword filter
        df.log("Step 1: Keyword filtering...")
        filtered = df.filter_by_keywords(papers)
        df.log(f"  After keyword filter: {len(filtered)} papers")

        if not filtered:
            df.log(f"  No papers after filtering for {date_str}")
            groups = {"A": [], "B": [], "C": []}
            html_papers = []
            featured_papers = None
        else:
            # Step 2: Classify
            df.log("Step 2: Classification...")
            for p in filtered:
                p["group"] = df.classify_paper(p)
                p["tags"] = df.extract_tags(p)

            groups = {"A": [], "B": [], "C": []}
            for p in filtered:
                groups[p["group"]].append(p)

            df.log(f"  A(detection): {len(groups['A'])}, B(edge): {len(groups['B'])}, C(other): {len(groups['C'])}")

            # Step 3: Select top papers
            df.log("Step 3: Select top papers...")
            top_papers = df.select_top_papers(filtered, top_n=50)

            groups = {"A": [], "B": [], "C": []}
            for p in top_papers:
                groups[p["group"]].append(p)

            # Step 4: Featured papers
            df.log("Step 4: Select featured papers...")
            featured_papers = df.select_featured_papers(top_papers, top_n=20)

            featured_ids = set(p["arxiv_id"] for p in featured_papers)
            for p in top_papers:
                p["worth_reading"] = p["arxiv_id"] in featured_ids

            # Step 5: Score
            df.log("Step 5: Scoring...")
            for p in top_papers:
                p["score"] = df.score_paper(p, p["group"])

            # Step 6: Chinese summaries
            df.log("Step 6: Generate Chinese summaries...")
            for p in top_papers:
                p["chinese_summary"] = df.generate_chinese_summary(p, p["group"])
                p["main_problem"] = df.extract_main_problem(p)
                p["highlights"] = df.extract_highlights(p)

            html_papers = top_papers

    # Step 7: Generate HTML
    df.log("Step 7: Generate HTML report...")
    reports_dir = os.path.join(df.REPO_ROOT, "daily_reports")
    os.makedirs(reports_dir, exist_ok=True)
    html_filename = f"daily_reports/{date_str}-arXiv.html"
    html_path = os.path.join(df.REPO_ROOT, html_filename)
    html_content = df.generate_daily_html(html_papers, target_date, groups)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    df.log(f"  HTML saved: {html_path}")

    # Step 8: Update config
    df.log("Step 8: Update config.js...")
    df.update_config_json(html_papers, target_date, groups, html_filename, featured_papers=featured_papers)

    worth_count = sum(1 for p in html_papers if p.get("worth_reading"))
    df.log(f"Done {date_str}: {len(html_papers)} papers, {worth_count} worth reading")
    return len(html_papers), worth_count


def main():
    today = datetime.now(timezone.utc).date()
    start_date = today - timedelta(days=1)
    end_date = today

    for arg in sys.argv[1:]:
        if arg.startswith("--start="):
            start_date = datetime.strptime(arg.split("=")[1], "%Y-%m-%d").date()
        elif arg.startswith("--end="):
            end_date = datetime.strptime(arg.split("=")[1], "%Y-%m-%d").date()

    num_days = (end_date - start_date).days + 1
    df.log(f"Catch-up mode: {start_date} to {end_date} ({num_days} days)")

    # Phase 1: Bulk fetch all papers
    df.log(f"\nPhase 1: Bulk fetching papers from ArXiv API...")
    df.log(f"  Fetching all papers from cs.CV, cs.LG, cs.AI, cs.RO sorted by date...")
    papers_by_date = fetch_all_papers_bulk(start_date, end_date)

    # Phase 2: Process each date
    df.log(f"\nPhase 2: Processing {num_days} dates...")
    total_papers = 0
    total_worth = 0
    dates_processed = 0
    dates_empty = 0

    current = start_date
    while current <= end_date:
        date_str = current.strftime("%Y-%m-%d")
        date_papers = papers_by_date.get(date_str, [])
        try:
            count, worth = process_date(current, date_papers)
            total_papers += count
            total_worth += worth
            dates_processed += 1
            if count == 0:
                dates_empty += 1
        except Exception as e:
            df.log(f"FAILED for {date_str}: {e}")
            import traceback
            traceback.print_exc()
        current += timedelta(days=1)

    df.log(f"\n{'=' * 60}")
    df.log(f"Catch-up complete! {dates_processed} days processed, {dates_empty} empty")
    df.log(f"Total: {total_papers} papers, {total_worth} worth reading")
    df.log(f"{'=' * 60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
