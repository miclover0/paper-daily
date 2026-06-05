#!/usr/bin/env python3
"""
Daily ArXiv Paper Tracker - 每日论文自动追踪脚本
====================================================
功能:
  1. 从 ArXiv API 获取当天新发表的相关论文
  2. 按主题筛选：VLM、开放世界、TTA、CoTTA、跨域自适应、Agent、视频分析、目标检测、端云协同
  3. 分为三组：A(检测强相关) / B(端云协同) / C(其他)
  4. 生成日报 HTML 页面（含中文摘要、主要问题、贡献、是否值得精读）
  5. 更新 config.js 数据文件

运行方式:
  python scripts/daily_fetch.py [--date YYYY-MM-DD]
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import os
import re
import sys
import time
import html as html_module
from datetime import datetime, timedelta, timezone

# ============================================================
# 配置区
# ============================================================

# ArXiv 数据源配置
# 使用 RSS Feed 获取每日新论文（比 API 更可靠，不受速率限制）
ARXIV_RSS_FEEDS = [
    "https://rss.arxiv.org/rss/cs.CV",
    "https://rss.arxiv.org/rss/cs.LG",
    "https://rss.arxiv.org/rss/cs.AI",
    "https://rss.arxiv.org/rss/cs.RO",
]
# 备用：API 模式（当 RSS 不可用时）
ARXIV_API_URL = "http://export.arxiv.org/api/query"
MAX_RESULTS_PER_CALL = 100
REQUEST_DELAY = 2  # 请求间延迟（秒）

# 工作目录（脚本所在目录的上级，即 paper-daily 根目录）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

# 论文搜索关键词（英文）
SEARCH_KEYWORDS = [
    "vision language model",
    "VLM",
    "open world detection",
    "open vocabulary detection",
    "open set recognition",
    "zero-shot detection",
    "test time adaptation",
    "continual test time adaptation",
    "CoTTA",
    "TTA",
    "domain adaptation",
    "cross domain adaptation",
    "cross domain generalization",
    "AI agent",
    "embodied agent",
    "multi-agent",
    "video understanding",
    "video analysis",
    "video object detection",
    "object detection",
    "edge computing",
    "edge device",
    "cloud edge collaboration",
    "cloud edge inference",
    "federated learning",
    "distributed inference",
    "model compression",
    "knowledge distillation",
    "model partitioning",
    "edge intelligence",
]

# 分组关键词（用于分类判断）
GROUP_A_KEYWORDS = [
    "object detection", "detector", "detection", "bounding box",
    "region proposal", "object localization", "object recognition",
    "target detection", "open vocabulary detect", "zero-shot detect",
    "YOLO", "DETR", "R-CNN", "SSD", "RetinaNet", "FCOS",
    "instance segmentation", "panoptic segmentation",
    "grounding", "referring expression", "visual grounding",
    "open world", "open set", "open vocabulary",
]

GROUP_B_KEYWORDS = [
    "edge computing", "edge device", "edge intelligence",
    "cloud edge", "cloud-edge", "edge cloud",
    "federated learning", "distributed training", "distributed inference",
    "model compression", "model pruning", "model quantization",
    "knowledge distillation", "model partitioning", "split computing",
    "tiny model", "efficient inference", "on-device",
    "mobile deployment", "resource constrained", "latency",
    "FLOPs", "parameter efficient", "lightweight",
    "collaborative inference", "co-inference",
]

# 分组展示标签
GROUP_LABELS = {
    "A": "目标检测强相关",
    "B": "端云协同/边缘计算",
    "C": "其他AI相关",
}

# 标签颜色映射
TAG_COLORS = {
    "VLM": {"bg": "#7c3aed", "text": "#fff"},
    "CoTTA": {"bg": "#ea580c", "text": "#fff"},
    "TTA": {"bg": "#dc2626", "text": "#fff"},
    "FTTA": {"bg": "#dc2626", "text": "#fff"},
    "Open World": {"bg": "#0891b2", "text": "#fff"},
    "Open Vocabulary": {"bg": "#0d9488", "text": "#fff"},
    "Domain Adaptation": {"bg": "#7c3aed", "text": "#fff"},
    "Cross Domain": {"bg": "#a855f7", "text": "#fff"},
    "Agents": {"bg": "#2563eb", "text": "#fff"},
    "Agent": {"bg": "#2563eb", "text": "#fff"},
    "Embodied AI": {"bg": "#059669", "text": "#fff"},
    "Video Analysis": {"bg": "#db2777", "text": "#fff"},
    "Object Detection": {"bg": "#1d4ed8", "text": "#fff"},
    "Edge Computing": {"bg": "#0891b2", "text": "#fff"},
    "Federated Learning": {"bg": "#4f46e5", "text": "#fff"},
    "World Model": {"bg": "#d97706", "text": "#fff"},
    "Distributed": {"bg": "#6366f1", "text": "#fff"},
    "Model Compression": {"bg": "#16a34a", "text": "#fff"},
    "LLM": {"bg": "#9333ea", "text": "#fff"},
    "AI": {"bg": "#64748b", "text": "#fff"},
}


# ============================================================
# 工具函数
# ============================================================

def log(msg):
    """带时间戳的日志输出"""
    try:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)
    except UnicodeEncodeError:
        # Windows GBK 编码兜底
        safe_msg = msg.encode('ascii', errors='replace').decode('ascii')
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {safe_msg}", flush=True)


def safe_request(url, max_retries=3):
    """安全的 HTTP 请求，带重试和速率限制"""
    for attempt in range(max_retries):
        try:
            time.sleep(REQUEST_DELAY)
            req = urllib.request.Request(url, headers={"User-Agent": "PaperDailyBot/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            log(f"  请求失败 (尝试 {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
    return None


def parse_arxiv_xml(xml_text):
    """解析 ArXiv API 返回的 XML"""
    papers = []
    try:
        root = ET.fromstring(xml_text)
        ns = {
            "atom": "http://www.w3.org/2005/Atom",
            "arxiv": "http://arxiv.org/schemas/atom",
        }
        for entry in root.findall("atom:entry", ns):
            paper = _parse_api_entry(entry, ns)
            if paper:
                papers.append(paper)
        return papers
    except ET.ParseError as e:
        log(f"  XML 解析错误: {e}")
        return []


def _parse_api_entry(entry, ns):
    """解析单个 API 条目"""
    paper = {
        "id": entry.find("atom:id", ns).text.strip() if entry.find("atom:id", ns) is not None else "",
        "title": " ".join(entry.find("atom:title", ns).text.strip().split()) if entry.find("atom:title", ns) is not None else "",
        "summary": " ".join(entry.find("atom:summary", ns).text.strip().split()) if entry.find("atom:summary", ns) is not None else "",
        "published": entry.find("atom:published", ns).text.strip() if entry.find("atom:published", ns) is not None else "",
        "updated": entry.find("atom:updated", ns).text.strip() if entry.find("atom:updated", ns) is not None else "",
        "authors": [],
        "categories": [],
        "pdf_url": "",
        "arxiv_id": "",
    }

    for author in entry.findall("atom:author", ns):
        name = author.find("atom:name", ns)
        if name is not None:
            paper["authors"].append(name.text.strip())

    for cat in entry.findall("atom:category", ns):
        term = cat.get("term", "")
        if term:
            paper["categories"].append(term)

    for link in entry.findall("atom:link", ns):
        if link.get("title") == "pdf":
            paper["pdf_url"] = link.get("href", "")
        elif link.get("rel") == "alternate":
            paper["abs_url"] = link.get("href", "")

    arxiv_url = paper.get("id", "")
    if "arxiv.org/abs/" in arxiv_url:
        paper["arxiv_id"] = arxiv_url.split("arxiv.org/abs/")[-1]

    if not paper["pdf_url"] and paper["arxiv_id"]:
        paper["pdf_url"] = f"https://arxiv.org/pdf/{paper['arxiv_id']}"

    return paper


def parse_arxiv_rss(xml_text, source_feed=""):
    """
    解析 ArXiv RSS Feed XML
    RSS Feed 格式与传统 RSS 2.0 兼容，包含 dc:creator, dc:date 等命名空间
    """
    papers = []
    try:
        root = ET.fromstring(xml_text)

        # RSS 命名空间
        ns = {
            "dc": "http://purl.org/dc/elements/1.1/",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        }

        # 尝试标准 RSS 2.0 结构
        items = root.findall(".//item")
        if not items:
            # 尝试 RDF 结构
            items = root.findall(".//{http://www.w3.org/1999/02/22-rdf-syntax-ns#}item")
            if not items:
                # 尝试 Atom 结构
                atom_ns = {"atom": "http://www.w3.org/2005/Atom"}
                items = root.findall(".//atom:entry", atom_ns)

        for item in items:
            paper = _parse_rss_item(item, ns, source_feed)
            if paper:
                papers.append(paper)

        return papers
    except ET.ParseError as e:
        log(f"  RSS XML 解析错误: {e}")
        return []


def _parse_rss_item(item, ns, source_feed):
    """解析单个 RSS item"""
    # 提取标题
    title_el = item.find("title")
    title = ""
    if title_el is not None and title_el.text:
        title = " ".join(title_el.text.strip().split())

    # 提取链接
    link_el = item.find("link")
    abs_url = ""
    if link_el is not None and link_el.text:
        abs_url = link_el.text.strip()

    # 提取描述（包含 arXiv ID 和摘要）
    desc_el = item.find("description")
    description = ""
    arxiv_id_from_desc = ""
    if desc_el is not None and desc_el.text:
        desc_text = desc_el.text.strip()
        # 格式: "arXiv:XXXX.XXXXXv1 Announce Type: new \nAbstract: ..."
        # 提取 arXiv ID
        arxiv_match = re.search(r'arXiv:(\d{4}\.\d{4,6})', desc_text)
        if arxiv_match:
            arxiv_id_from_desc = arxiv_match.group(1)
        # 提取 Abstract 部分
        abs_match = re.search(r'Abstract:\s*(.+)', desc_text, re.DOTALL)
        if abs_match:
            description = abs_match.group(1).strip()[:2000]

    # 提取作者 (dc:creator) - ArXiv RSS 中所有作者在同一个元素中，逗号分隔
    authors = []
    creator_el = item.find("dc:creator", ns)
    if creator_el is not None and creator_el.text:
        # 作者可能用逗号分隔
        author_text = creator_el.text.strip()
        authors = [a.strip() for a in author_text.split(",") if a.strip()]

    # 提取日期
    date_el = item.find("pubDate")  # RSS 标准的 pubDate
    if date_el is None:
        date_el = item.find("dc:date", ns)
    pub_date = date_el.text.strip() if date_el is not None and date_el.text else ""

    # 从 URL 提取 arXiv ID（备用）
    arxiv_id = ""
    if "arxiv.org/abs/" in abs_url:
        arxiv_id = abs_url.split("arxiv.org/abs/")[-1].rstrip("/")
    if not arxiv_id:
        arxiv_id = arxiv_id_from_desc

    # 提取分类
    categories = []
    for cat_el in item.findall("category"):
        if cat_el.text:
            categories.append(cat_el.text.strip())

    # 构建 paper 结构
    paper = {
        "id": abs_url,
        "title": title,
        "summary": description,
        "published": pub_date[:10] if pub_date else "",
        "updated": pub_date[:10] if pub_date else "",
        "authors": authors,
        "categories": categories,
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}" if arxiv_id else "",
        "abs_url": abs_url,
        "arxiv_id": arxiv_id,
    }

    return paper


def fetch_papers_from_rss():
    """从 ArXiv RSS Feed 获取今天的论文"""
    all_papers = []
    seen_ids = set()

    for feed_url in ARXIV_RSS_FEEDS:
        log(f"  获取 RSS: {feed_url.split('/')[-1]}...")
        xml_text = safe_request(feed_url)
        if not xml_text:
            log(f"    RSS 获取失败: {feed_url}")
            continue

        papers = parse_arxiv_rss(xml_text, feed_url)
        new_count = 0
        for p in papers:
            pid = p["arxiv_id"]
            if pid and pid not in seen_ids:
                seen_ids.add(pid)
                all_papers.append(p)
                new_count += 1

        log(f"    获取 {len(papers)} 篇, 新增 {new_count} 篇 (累计: {len(all_papers)})")

    return all_papers


# ============================================================
# 论文搜索
# ============================================================

def build_search_query():
    """构建 ArXiv API 搜索查询（已 URL 编码）"""
    # 使用 OR 连接所有关键词
    keyword_groups = []
    for kw in SEARCH_KEYWORDS:
        keyword_groups.append(f'all:"{kw}"')
    keyword_query = " OR ".join(keyword_groups)

    # 限制分类
    cat_query = "(cat:cs.CV OR cat:cs.LG OR cat:cs.AI OR cat:cs.RO)"

    full_query = f"({keyword_query}) AND {cat_query}"
    # URL 编码
    return urllib.parse.quote(full_query, safe="")


def fetch_papers_by_date(target_date):
    """
    获取指定日期的论文
    优先使用 RSS Feed（更快更可靠），失败时回退到 API
    """
    date_str = target_date.strftime("%Y-%m-%d")
    log("  尝试 RSS Feed...")

    all_papers = fetch_papers_from_rss()

    if all_papers:
        # RSS 返回的就是今天的论文，进行关键词过滤
        log(f"  RSS 获取到 {len(all_papers)} 篇论文，开始关键词过滤...")
        filtered = filter_by_keywords(all_papers)
        log(f"  关键词过滤后剩余 {len(filtered)} 篇")
        return filtered

    # 回退：使用 API（带日期过滤）
    log("  RSS 无结果，尝试 API 回退...")
    return fetch_papers_from_api(target_date)


def filter_by_keywords(papers):
    """根据关键词过滤论文"""
    filtered = []
    for p in papers:
        combined = (p["title"] + " " + p["summary"]).lower()
        # 检查是否匹配任一关键词
        matched = False
        for kw in SEARCH_KEYWORDS:
            if kw.lower() in combined:
                matched = True
                break
        if matched:
            filtered.append(p)
    return filtered


def fetch_papers_from_api(target_date):
    """API 回退方案"""
    query = build_search_query()
    all_papers = []
    seen_ids = set()
    date_str = target_date.strftime("%Y-%m-%d")

    for start in range(0, 300, MAX_RESULTS_PER_CALL):
        url = (
            f"{ARXIV_API_URL}?search_query={query}"
            f"&start={start}"
            f"&max_results={MAX_RESULTS_PER_CALL}"
            f"&sortBy=submittedDate"
            f"&sortOrder=descending"
        )
        log(f"  请求 ArXiv API (offset={start})...")
        xml_text = safe_request(url)
        if not xml_text:
            break

        batch = parse_arxiv_xml(xml_text)
        if not batch:
            break

        new_papers = []
        for p in batch:
            pid = p["arxiv_id"]
            if pid and pid not in seen_ids:
                seen_ids.add(pid)
                # 日期过滤
                pub_date = p["published"][:10] if p["published"] else ""
                if pub_date == date_str:
                    new_papers.append(p)

        all_papers.extend(new_papers)
        log(f"  获取 {len(new_papers)} 篇当日论文 (累计: {len(all_papers)})")

        if len(batch) < MAX_RESULTS_PER_CALL:
            break

    log(f"  API 获取 {len(all_papers)} 篇论文 (目标日期: {date_str})")
    return all_papers


# ============================================================
# 论文分类
# ============================================================

def classify_paper(paper):
    """
    将论文分为 A/B/C 组
    - A: 目标检测强相关
    - B: 端云协同/边缘计算
    - C: 其他
    """
    title_lower = paper["title"].lower()
    summary_lower = paper["summary"].lower()
    combined = title_lower + " " + summary_lower

    # 先检查 B 组（端云协同）- 优先检查避免被对象检测覆盖
    b_score = sum(1 for kw in GROUP_B_KEYWORDS if kw.lower() in combined)
    if b_score >= 2:
        return "B"

    # 检查 A 组（目标检测）
    a_score = sum(1 for kw in GROUP_A_KEYWORDS if kw.lower() in combined)
    if a_score >= 2 or "detection" in title_lower:
        return "A"

    # 检查标题中的检测相关
    detect_keywords = ["detect", "yolo", "detr", "rcnn", "faster r-cnn", "ssd", "retinanet",
                       "grounding dino", "grounding", "sam", "segment anything"]
    if any(kw in combined for kw in detect_keywords):
        return "A"

    # B 组的单个关键词匹配（更宽松）
    if b_score >= 1:
        return "B"

    return "C"


def extract_tags(paper):
    """从论文标题和摘要中提取标签"""
    title_lower = paper["title"].lower()
    summary_lower = paper["summary"].lower()
    combined = title_lower + " " + summary_lower

    tags = []
    tag_rules = [
        ("VLM", ["vision language model", "vlm", "visual language model", "vision-language"]),
        ("TTA", ["test time adaptation", "test-time adaptation"]),
        ("CoTTA", ["continual test time", "continual test-time", "cotta"]),
        ("Open World", ["open world", "open-world"]),
        ("Open Vocabulary", ["open vocabulary", "open-vocabulary"]),
        ("Domain Adaptation", ["domain adaptation", "domain generalization", "domain shift"]),
        ("Cross Domain", ["cross domain", "cross-domain", "cross modal"]),
        ("Agent", ["agent", "multi-agent", "agentic"]),
        ("Embodied AI", ["embodied", "robot", "manipulation", "navigation"]),
        ("Video Analysis", ["video", "temporal", "action recognition"]),
        ("Object Detection", ["object detection", "detector", "detection"]),
        ("Edge Computing", ["edge computing", "edge device", "edge intelligence"]),
        ("Federated Learning", ["federated learning", "federated"]),
        ("World Model", ["world model", "world-model"]),
        ("Model Compression", ["model compression", "pruning", "quantization", "distillation"]),
        ("Distributed", ["distributed", "decentralized"]),
    ]

    for tag_name, keywords in tag_rules:
        if any(kw in combined for kw in keywords):
            tags.append(tag_name)
            if len(tags) >= 3:  # 最多3个标签
                break

    if not tags:
        tags.append("AI")

    return tags[:3]


# ============================================================
# 论文评分 & 是否值得精读
# ============================================================

def compute_relevance_score(title, summary, categories):
    """
    计算论文与 AI/CV/Agent/边缘计算等方向的「相关度分数」（0-100）
    用于从每天 ~200 篇论文中筛选「强相关」的 50 篇。
    评分因素：
    - ArXiv 类别（cs.AI/cs.LG/cs.CV/cs.RO 权重最高）
    - 标题/摘要核心关键词匹配
    - 负面关键词减分（medical/biology/finance 等非核心方向）
    - 标题/摘要质量加分
    """
    score = 0.0
    title_lower = title.lower()
    summary_lower = summary.lower()
    combined = title_lower + " " + summary_lower

    # 1. 类别权重（0-40分）
    cat_score = 0
    for cat in categories:
        if cat == "cs.AI":
            cat_score = max(cat_score, 40)
        elif cat == "cs.LG":
            cat_score = max(cat_score, 38)
        elif cat == "cs.CV":
            cat_score = max(cat_score, 35)
        elif cat == "cs.RO":
            cat_score = max(cat_score, 32)
        elif cat.startswith("cs."):
            cat_score = max(cat_score, 20)
    score += cat_score

    # 2. 核心关键词匹配（累计，最高40分）
    core_keywords = [
        ("vision language model", 15), ("vlm", 15), ("visual language", 12),
        ("object detection", 15), ("detector", 10), ("detection", 8),
        ("test time adaptation", 15), ("tta", 15), ("test-time adaptation", 15),
        ("continual test time", 15), ("cotta", 15),
        ("domain adaptation", 12), ("domain generalization", 12), ("cross domain", 10),
        ("open world", 12), ("open vocabulary", 12), ("open set", 10), ("zero-shot", 10),
        ("ai agent", 12), ("multi-agent", 12), ("agentic", 10), ("embodied", 10),
        ("video understanding", 10), ("video analysis", 10), ("temporal", 8),
        ("edge computing", 12), ("edge intelligence", 12), ("edge device", 10),
        ("federated learning", 10), ("distributed inference", 10),
        ("model compression", 10), ("knowledge distillation", 10), ("pruning", 8), ("quantization", 8),
        ("diffusion model", 10), ("diffusion", 8),
        ("transformer", 8), ("attention", 6),
        ("benchmark", 5), ("survey", -20), ("review", -10),
    ]
    for kw, pts in core_keywords:
        if kw in combined:
            score += pts

    # 3. 负面关键词减分
    negative_keywords = [
        "medical", "healthcare", "clinical", "drug", "medicine",
        "biology", "genomic", "protein", "chemical", "molecule",
        "finance", "stock", "trading", "crypto",
        "music", "art", "poetry", "painting",
        "hardware", "circuit", "fpga", "asic",
    ]
    for kw in negative_keywords:
        if kw in combined:
            score -= 18

    # 4. 标题质量加分（5分）
    if 30 <= len(title) <= 150:
        score += 5

    # 5. 摘要质量加分（5分）
    if len(summary) > 500:
        score += 5

    # 6. 是否有具体数值结果（5分）
    if re.search(r'\d+\.?\d*\s*%', summary):
        score += 5

    # 截断到 0-100
    return max(0.0, min(100.0, score))


def select_top_papers(papers, top_n=50):
    """
    从所有论文中筛选「强相关」的前 N 篇（默认50篇）
    返回筛选后的论文列表，并为每篇论文添加 relevance_score 字段
    """
    if not papers:
        return []

    log(f"  计算相关度分数（共 {len(papers)} 篇）...")
    for p in papers:
        p["relevance_score"] = compute_relevance_score(
            p["title"], p["summary"], p.get("categories", [])
        )

    # 按相关度分数降序排序
    sorted_papers = sorted(papers, key=lambda p: p.get("relevance_score", 0), reverse=True)

    # 如果筛选后太少，放宽到分数 >= 30
    if len(sorted_papers) > top_n:
        threshold = sorted_papers[top_n - 1].get("relevance_score", 0)
        # 如果第50名的分数 >= 30，则严格取前50；否则放宽到所有 >= 30 分的
        if threshold >= 30:
            selected = sorted_papers[:top_n]
        else:
            selected = [p for p in sorted_papers if p.get("relevance_score", 0) >= 30]
            log(f"  相关度分数较低，放宽筛选：取所有分数>=30的论文（共 {len(selected)} 篇）")
            selected = selected[:top_n]  # 最多取 top_n
    else:
        selected = sorted_papers

    log(f"  筛选出 {len(selected)} 篇强相关论文（相关度分数 >= {selected[-1].get('relevance_score', 0):.1f}）")
    return selected


def generate_read_reason(paper):
    """
    生成「精读原因」（中文，1-2句话）
    基于论文的标签、分组、评分等信息生成
    """
    tags = paper.get("tags", [])
    group = paper.get("group", "C")
    title = paper["title"]
    summary = paper["summary"]
    combined = (title + " " + summary).lower()

    reasons = []

    # 根据标签生成原因
    tag_reason_map = [
        ("VLM", "本文探索视觉-语言模型（VLM）的前沿进展，对多模态理解有重要参考价值"),
        ("CoTTA", "持续测试时自适应（CoTTA）在实际部署中至关重要，本文提出了有价值的改进思路"),
        ("TTA", "测试时自适应（TTA）是提升模型泛化能力的关键技术，本文值得深入研究"),
        ("Open World", "开放世界识别是计算机视觉的核心挑战，本文可能带来新的解决思路"),
        ("Open Vocabulary", "开放词汇检测是连接视觉与语言的重要方向，本文具有一定的创新价值"),
        ("Domain Adaptation", "域自适应技术对于跨场景泛化至关重要，本文值得深入理解"),
        ("Cross Domain", "跨域泛化是实际部署中的核心挑战，本文提供了有价值的技术方案"),
        ("Agent", "AI Agent 是当前研究热点，本文可能包含创新性的设计思路"),
        ("Embodied AI", "具身智能是通向通用 AI 的重要路径，本文值得关注"),
        ("Video Analysis", "视频理解是计算机视觉的重要方向，本文可能推动该领域的进展"),
        ("Object Detection", "目标检测是基础且重要的研究方向，本文可能带来性能或效率的显著提升"),
        ("Edge Computing", "边缘计算与端云协同是实际系统的核心挑战，本文提供了实用的解决方案"),
        ("Federated Learning", "联邦学习对于隐私保护场景至关重要，本文值得深入研究"),
        ("Model Compression", "模型压缩对于边缘部署至关重要，本文可能带来新的压缩技术"),
        ("World Model", "世界模型是提升模型泛化能力的前沿方向，本文具有一定的探索价值"),
        ("Distributed", "分布式训练/推理是大规模系统的核心技术，本文提供了有价值的优化思路"),
    ]
    for tag, reason in tag_reason_map:
        if tag in tags:
            reasons.append(reason)
            if len(reasons) >= 2:
                break

    # 根据分组补充原因
    if not reasons:
        if group == "A":
            reasons.append("本文与目标检测高度相关，可能包含可借鉴的技术思路")
        elif group == "B":
            reasons.append("本文涉及端云协同/边缘计算，对系统优化有实际价值")
        else:
            reasons.append("本文与当前 AI 研究前沿相关，值得关注其技术思路")

    # 根据摘要内容补充原因
    if "novel" in summary.lower() or "propose" in summary.lower():
        reasons.append("论文提出了新的方法/框架，具有创新性")
    if "state-of-the-art" in summary.lower() or "sota" in summary.lower():
        reasons.append("论文在多个基准上达到 SOTA 性能，值得深入研究其技术细节")
    if "benchmark" in summary.lower():
        reasons.append("论文建立了新的基准评测，对后续研究有参考价值")

    # 如果原因太多，取前2条合并
    if len(reasons) > 2:
        reasons = reasons[:2]

    return "；".join(reasons)


def select_featured_papers(papers, top_n=20):
    """
    从强相关论文中挑选「精读推荐」（默认20篇）
    综合考量：相关度分数(50%) + 质量评分(50%)
    为每篇生成 read_reason（精读原因）
    """
    if not papers:
        return []

    log(f"  从 {len(papers)} 篇强相关论文中挑选精读推荐...")

    # 综合评分 = 相关度分数 * 0.5 + 质量评分 * 0.5
    for p in papers:
        relevance = p.get("relevance_score", 0)
        quality = p.get("score", 0)
        # 归一化：relevance 0-100, quality 0-10
        p["combined_score"] = relevance * 0.5 + quality * 5.0 * 0.5

    # 按综合评分降序排序
    sorted_papers = sorted(papers, key=lambda p: p.get("combined_score", 0), reverse=True)

    # 取前 N 篇
    featured = sorted_papers[:top_n]

    # 为每篇生成精读原因
    for p in featured:
        p["read_reason"] = generate_read_reason(p)

    log(f"  精读推荐 {len(featured)} 篇")
    return featured


def score_paper(paper, group):
    """
    对论文进行质量评分（用于判断是否值得精读）
    评分因素：
    - 标题长度（太短或太长都不好）
    - 摘要长度（有实质性内容）
    - 关键词密度
    - 小组匹配度
    - 是否有具体方法名
    """
    score = 0.0
    title = paper["title"]
    summary = paper["summary"]

    # 标题质量
    title_len = len(title)
    if 40 <= title_len <= 150:
        score += 1.0
    elif 20 <= title_len <= 200:
        score += 0.5

    # 摘要质量
    summary_len = len(summary)
    if summary_len > 500:
        score += 2.0
    elif summary_len > 200:
        score += 1.0

    # 方法关键词
    method_keywords = ["novel", "state-of-the-art", "outperform", "propose", "framework",
                       "benchmark", "achieve", "improve", "efficient", "robust",
                       "method", "approach", "architecture"]
    method_count = sum(1 for kw in method_keywords if kw in summary.lower())
    score += min(method_count * 0.5, 3.0)

    # 组匹配度加分
    if group == "A":
        a_score = sum(1 for kw in GROUP_A_KEYWORDS if kw.lower() in (title.lower() + " " + summary.lower()))
        score += min(a_score * 0.3, 2.0)
    elif group == "B":
        b_score = sum(1 for kw in GROUP_B_KEYWORDS if kw.lower() in (title.lower() + " " + summary.lower()))
        score += min(b_score * 0.3, 2.0)

    # 是否有具体数值结果
    if re.search(r'\d+\.?\d*\s*%', summary):
        score += 1.0

    return score


def mark_worth_reading(papers):
    """标记约30%的论文为值得精读"""
    if not papers:
        return papers

    top_count = max(1, int(len(papers) * 0.3))
    sorted_papers = sorted(papers, key=lambda p: p.get("score", 0), reverse=True)

    worth_ids = set()
    for i in range(min(top_count, len(sorted_papers))):
        worth_ids.add(sorted_papers[i]["arxiv_id"])

    for p in papers:
        p["worth_reading"] = p["arxiv_id"] in worth_ids

    return papers


# ============================================================
# 中文摘要生成
# ============================================================

def generate_chinese_summary(paper, group):
    """
    生成完整的中文摘要（基于英文摘要的结构化信息提取）
    输出 3-5 句中文摘要，包含：研究背景、方法思路、核心贡献、实验结果
    """
    title = paper["title"]
    summary = paper["summary"]
    summary_lower = summary.lower()
    tags = paper.get("tags", [])

    # ---- 1. 领域描述 ----
    domain_desc = "计算机视觉与深度学习"
    domain_map = [
        ("VLM", "视觉-语言模型（VLM）"),
        ("Object Detection", "目标检测"),
        ("Domain Adaptation", "域自适应"),
        ("Agent", "AI智能体（Agent）"),
        ("Embodied AI", "具身智能与机器人"),
        ("Edge Computing", "边缘计算与端云协同"),
        ("Video Analysis", "视频分析"),
        ("World Model", "世界模型"),
        ("TTA", "测试时自适应"),
        ("CoTTA", "持续测试时自适应"),
        ("Federated Learning", "联邦学习"),
        ("Model Compression", "模型压缩"),
        ("Distributed", "分布式学习"),
    ]
    for tag, desc in domain_map:
        if tag in tags:
            domain_desc = desc
            break

    # ---- 2. 研究动机/背景 ----
    background = ""
    bg_patterns = [
        (r'([^.?!]*(?:challenge|problem|limitation|bottleneck|issue|remain|suffer|lack)[^.?!]*[.?!])', "当前方法面临"),
        (r'([^.?!]*(?:Recent|Recent advances|With the|In recent years|The field of)[^.?!]*[.?!])', "近年来"),
    ]
    for pattern, label in bg_patterns:
        m = re.search(pattern, summary, re.IGNORECASE)
        if m:
            bg_text = m.group(1).strip()
            if len(bg_text) > 30 and len(bg_text) < 300:
                background = bg_text
                break
    if not background:
        first_sent = re.split(r'(?<=[.!?])\s+', summary)
        if first_sent and len(first_sent[0]) > 20:
            background = first_sent[0][:250]

    # ---- 3. 方法描述 ----
    method_desc = ""
    method_patterns = [
        (r'(?:we|this paper|this work)\s+(?:propose|present|introduce|develop|design)[^.?!]*[.?!]', "提出"),
        (r'(?:we|this paper)\s+(?:explore|investigate|study)[^.?!]*[.?!]', "探索"),
        (r'(?:we|this paper)\s+(?:leverage|utilize|employ|use|adopt)[^.?!]*[.?!]', "采用"),
        (r'(?:we|this paper)\s+(?:introduce|present)\s+a\s+(?:novel|new)[^.?!]*[.?!]', "创新性地提出"),
        (r'(?:our|the proposed)\s+(?:method|approach|framework|model|system|architecture)[^.?!]*[.?!]', "核心方法"),
    ]
    for pattern, label in method_patterns:
        m = re.search(pattern, summary, re.IGNORECASE)
        if m:
            mt = m.group(0).strip()
            if len(mt) > 30 and len(mt) < 300:
                method_desc = mt
                break

    # ---- 4. 实验结果/性能 ----
    performance = ""
    perf_patterns = [
        (r'([^.?!]*(?:achieve|achieves|achieved|obtain|obtains|outperform|surpass|exceed|improve|improves|boost|state-of-the-art|SOTA)[^.?!]*?(\d+\.?\d*\s*[%％]|\d+\.?\d*\s*(?:points|percent)|by\s+\d+\.?\d*)[^.?!]*[.?!])', ""),
        (r'([^.?!]*(?:experiment|evaluate|benchmark|result|performance)[^.?!]*?(\d+\.?\d*\s*[%％]|\d+\.?\d*\s*(?:points|percent))[^.?!]*[.?!])', ""),
    ]
    for pattern, _ in perf_patterns:
        m = re.search(pattern, summary, re.IGNORECASE)
        if m:
            pt = m.group(1).strip()
            if len(pt) > 30 and len(pt) < 300:
                performance = pt
                break

    # ---- 5. 贡献总结 ----
    contribution = ""
    contrib_patterns = [
        (r'([^.?!]*(?:contribution|main contribution|key contribution|we demonstrate|we show|in summary|overall)[^.?!]*[.?!])', ""),
    ]
    for pattern, _ in contrib_patterns:
        m = re.search(pattern, summary, re.IGNORECASE)
        if m:
            ct = m.group(1).strip()
            if len(ct) > 20 and len(ct) < 250:
                contribution = ct
                break

    # ---- 组装中文摘要 ----
    parts = [f"【研究背景】该论文聚焦{domain_desc}领域。"]

    if background:
        parts.append(f"{truncate_en_sentence(background, 200)}。")

    if method_desc:
        parts.append(f"【核心方法】{truncate_en_sentence(method_desc, 250)}。")

    if performance:
        parts.append(f"【实验结果】{truncate_en_sentence(performance, 200)}。")

    if contribution:
        parts.append(f"【主要贡献】{truncate_en_sentence(contribution, 200)}。")

    if len(parts) < 3:
        # 如果太少，补充额外的信息
        sentences = re.split(r'(?<=[.!?])\s+', summary)
        for s in sentences[:4]:
            s = s.strip()
            if 40 < len(s) < 200 and s not in "".join(parts):
                parts.append(f"{truncate_en_sentence(s, 200)}。")
            if len(parts) >= 5:
                break

    # 如果还不够，加标签提示
    tags_zh = "、".join(tags[:3]) if tags else "AI"
    if len(parts) < 3:
        parts.append(f"该论文涉及{tags_zh}等关键技术方向。")

    return "\n".join(parts)


def truncate_en_sentence(text, max_len):
    """截断英文句子到合理长度"""
    if len(text) <= max_len:
        return text
    # 尝试在单词边界截断
    cut = text[:max_len].rstrip()
    last_space = cut.rfind(" ")
    if last_space > max_len // 2:
        cut = cut[:last_space]
    return cut + "..."


def extract_highlights(paper):
    """提取论文的创新点和贡献"""
    summary = paper["summary"]
    highlights = []

    # 关键词驱动的亮点提取
    highlight_patterns = [
        (r'(propose|present|introduce)\s+(?:a\s+)?(?:novel\s+)?([^,.]+?(?:framework|method|approach|model|architecture|technique|algorithm))', "提出"),
        (r'(achieve|obtain|reach)\s+(?:the\s+)?(?:new\s+)?(?:state-of-the-art|SOTA)[^,.]+', "性能突破"),
        (r'(outperform|surpass|exceed)[^,.]+', "超越现有方法"),
        (r'(reduce|decrease|lower)\s+\w+\s+(?:by\s+)?\d+[%％]', "效率提升"),
        (r'(improve|increase|boost)\s+\w+\s+(?:by\s+)?\d+[%％]', "性能提升"),
        (r'(without|no\s+need\s+for|free\s+of)\s+[^,.]+(?:training|label|annotation|supervision)', "无需标注"),
        (r'(first|first-ever)\s+[^,.]+', "首次提出"),
    ]

    for pattern, label in highlight_patterns:
        match = re.search(pattern, summary, re.IGNORECASE)
        if match:
            text = match.group(0).strip()
            if len(text) > 5 and text not in [h[1] for h in highlights]:
                highlights.append((label, text[:120]))

    # 如果提取不足3条，添加通用亮点
    if len(highlights) < 2:
        title = paper["title"]
        # 从标题提取关键短语
        title_parts = re.split(r'[:\-–—]', title)
        if len(title_parts) >= 2:
            highlights.append(("核心思路", title_parts[0].strip()[:100]))

        # 从分类标签生成
        cats = paper.get("categories", [])
        if cats:
            highlights.append(("研究领域", f"隶属于 {', '.join(cats[:2])}"))

    # 保证至少3条
    if len(highlights) < 3:
        for s in re.split(r'(?<=[.!?])\s+', summary):
            s = s.strip()
            if len(s) > 20 and len(s) < 150:
                highlights.append(("研究要点", s[:120]))
                if len(highlights) >= 3:
                    break

    return highlights[:3]


# ============================================================
# 主要问题提取
# ============================================================

def extract_main_problem(paper):
    """提取论文主要解决的问题"""
    summary = paper["summary"]
    title = paper["title"]

    # 常见问题模式
    problem_patterns = [
        (r'(challenge|problem|issue|limitation|bottleneck|difficulty)\s+(?:of|in|with|is\s+that)\s+([^,.]+)', "挑战"),
        (r'(suffer\s+from|lack\s+of|struggle\s+with|limited\s+by)\s+([^,.]+)', "不足"),
        (r'(current|existing|traditional|conventional)\s+(?:methods|approaches|models)\s+([^,.]+)', "现有方法问题"),
        (r'(address|tackle|solve|overcome|mitigate)\s+(?:the\s+)?([^,.]+)', "解决"),
    ]

    for pattern, label in problem_patterns:
        match = re.search(pattern, summary, re.IGNORECASE)
        if match:
            return match.group(0).strip()[:150]

    # Fallback: 从标题提取
    parts = re.split(r'[:\-–—]', title)
    if len(parts) >= 2:
        return f"针对 {parts[0].strip()[:80]} 中的问题，{parts[1].strip()[:60]}"

    return f"解决 {paper.get('tags', ['AI'])[0]} 领域的关键挑战"


# ============================================================
# HTML 生成
# ============================================================

def generate_daily_html(papers, target_date, groups):
    """生成日报 HTML 页面 — 左右两栏布局：左侧目录 + 右侧内容"""
    date_str = target_date.strftime("%Y-%m-%d")
    total = len(papers)
    group_counts = {g: len(gs) for g, gs in groups.items()}

    def esc(text):
        if not text:
            return ""
        return html_module.escape(str(text))

    # 先构建 TOC 条目和内容卡片
    toc_items = []
    content_cards = []
    group_order = ["A", "B", "C"]
    badge_classes = {"A": "badge-a", "B": "badge-b", "C": "badge-c"}

    for gi, group_name in enumerate(group_order):
        group_papers = groups.get(group_name, [])
        if not group_papers:
            continue
        label = GROUP_LABELS[group_name]
        # TOC 分组标题
        toc_items.append(
            f'<li class="toc-group-header"><span class="badge {badge_classes[group_name]}">{group_name}组</span> {label} ({len(group_papers)}篇)</li>'
        )
        # 内容分组标题
        content_cards.append(
            f'<h2 class="section-header" id="group-{group_name}"><span class="badge {badge_classes[group_name]}">{group_name}组</span> {label}</h2>'
        )

        for idx, paper in enumerate(group_papers):
            pid = f"{group_name}{idx+1}"
            worth = paper.get("worth_reading", False)
            card_class = "card worth-reading" if worth else "card"

            # TOC 条目
            title_short = paper["title"][:55] + "..." if len(paper["title"]) > 55 else paper["title"]
            toc_class = "toc-link worth-reading" if worth else "toc-link"
            toc_items.append(
                f'<li><a href="#{pid}" class="{toc_class}">{pid} {esc(title_short)}</a></li>'
            )

            # 标签
            tags_html = ""
            for tag in paper.get("tags", []):
                tc = TAG_COLORS.get(tag, TAG_COLORS["AI"])
                tags_html += f"<span class='tag' style='background:{tc['bg']};color:{tc['text']}'>{esc(tag)}</span>"

            # 中文摘要（支持多行）
            chinese_summary = paper.get("chinese_summary", paper["summary"][:300])
            chinese_summary_html = chinese_summary.replace("\n", "<br>") if chinese_summary else ""

            # 主要问题
            main_problem = paper.get("main_problem", "")
            main_problem_html = (
                f'<div class="problem-box"><strong>🔍 主要解决问题：</strong>{esc(main_problem)}</div>'
                if main_problem else ""
            )

            # 亮点
            highlights = paper.get("highlights", [])
            highlights_html = ""
            if highlights:
                for h in highlights:
                    if isinstance(h, tuple):
                        highlights_html += f"<li><strong>{esc(h[0])}：</strong>{esc(h[1])}</li>"
                    else:
                        highlights_html += f"<li>{esc(h)}</li>"

            # 精读原因
            read_reason = paper.get("read_reason", "")
            read_reason_html = ""
            if read_reason and worth:
                read_reason_html = (
                    f'<div class="read-reason-box"><strong>📖 精读原因：</strong>{esc(read_reason)}</div>'
                )

            # 链接
            pdf_url = paper.get("pdf_url", paper.get("abs_url", "#"))
            arxiv_id = paper.get("arxiv_id", "")

            content_cards.append(f'''
<div class='{card_class}' id='{pid}'>
    {f'<div class="worth-badge">⭐ 值得精读</div>' if worth else ''}
    <h3><span class='badge {badge_classes[group_name]}'>{pid}</span> {esc(paper["title"])}</h3>
    <p class='meta'>
        <span class='badge badge-source'>arXiv: {esc(arxiv_id[:20])}</span>
        {tags_html}
    </p>
    <div class="chinese-summary"><strong>📝 中文摘要：</strong><br>{chinese_summary_html}</div>
    {main_problem_html}
    {read_reason_html}
    <p><strong>📌 核心亮点：</strong></p>
    <ul>{highlights_html}</ul>
    <p>
        <a href='{esc(pdf_url)}' target='_blank'>📄 论文链接</a>
        {' | <a href="https://arxiv.org/abs/' + esc(arxiv_id) + '" target="_blank">📋 arXiv 页面</a>' if arxiv_id else ''}
    </p>
</div>''')

    # 组装 HTML
    toc_html = "\n".join(toc_items)
    content_html = "\n".join(content_cards)

    html = f'''<!DOCTYPE html>
<html lang='zh-CN'>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>论文日报 {date_str}</title>
<style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.75;color:#172033;background:#f6f8fb}}
    .layout{{display:flex;min-height:100vh}}
    
    .toc{{width:280px;min-width:260px;max-width:320px;background:#fff;border-right:1px solid #e2e8f0;padding:16px 0;overflow-y:auto;position:sticky;top:0;height:100vh;flex-shrink:0}}
    .toc h2{{font-size:15px;padding:0 18px 10px;color:#1a1a2e;border-bottom:1px solid #e2e8f0;margin-bottom:6px}}
    .toc ul{{list-style:none;padding:0}}
    .toc li{{margin:0}}
    .toc .toc-group-header{{padding:8px 18px 4px;font-size:13px;font-weight:600;color:#64748b;margin-top:6px}}
    .toc .toc-link{{display:block;padding:5px 18px 5px 26px;font-size:12px;color:#475569;text-decoration:none;line-height:1.45;transition:background .15s,border-color .15s;border-left:3px solid transparent}}
    .toc .toc-link:hover{{background:#f1f5f9;color:#1e293b;border-left-color:#2563eb}}
    .toc .toc-link.worth-reading{{font-weight:500}}
    .toc .toc-link.worth-reading::after{{content:' ⭐';font-size:10px}}
    
    .content{{flex:1;padding:24px 48px;min-width:0;overflow-y:auto}}
    .header{{margin-bottom:20px;text-align:center;max-width:1100px;margin-left:auto;margin-right:auto}}
    .meta{{color:#566074;font-size:14px}}
    .section-header{{margin:32px 0 16px;font-size:20px;color:#2563eb;border-bottom:2px solid #2563eb;padding-bottom:8px;max-width:1100px;margin-left:auto;margin-right:auto}}
    .card{{border:1px solid #dbe2ea;border-radius:16px;padding:20px;margin:20px 0;background:#fff;box-shadow:0 4px 14px rgba(15,23,42,.04);position:relative;scroll-margin-top:20px;max-width:1100px;margin-left:auto;margin-right:auto;width:auto}}
    .card.worth-reading{{border-left:4px solid #f59e0b;background:linear-gradient(135deg,#fffbeb 0%,#fff 100%);max-width:1100px;margin-left:auto;margin-right:auto;width:auto}}
    .worth-badge{{position:absolute;top:14px;right:14px;background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;padding:4px 14px;border-radius:999px;font-size:12px;font-weight:600}}
    h1{{font-size:28px;margin:0 0 8px;color:#1a1a2e}}
    h3{{margin:0 0 10px;font-size:17px;color:#1e293b;padding-right:90px}}
    p{{margin:10px 0}}
    ul{{margin:10px 0 0 20px;padding:0}}
    li{{margin:8px 0}}
    .chinese-summary{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:12px 14px;margin:12px 0;font-size:14px;color:#334155;line-height:1.85}}
    .chinese-summary strong{{color:#1e293b}}
    .problem-box{{background:#f0f9ff;border:1px solid #bae6fd;border-radius:8px;padding:10px 14px;margin:12px 0;font-size:14px;color:#0369a1;line-height:1.7}}
    .problem-box strong{{color:#0284c7}}
    .read-reason-box{{background:#fefce8;border:1px solid #fde68a;border-radius:8px;padding:10px 14px;margin:12px 0;font-size:14px;color:#854d0e}}
    .read-reason-box strong{{color:#d97706}}
    a{{color:#2563eb;word-break:break-all;text-decoration:none}}
    a:hover{{text-decoration:underline}}
    .badge{{display:inline-block;padding:2px 10px;border-radius:999px;font-size:12px;margin-right:6px}}
    .badge-a{{background:#dbeafe;color:#1d4ed8}}
    .badge-b{{background:#dcfce7;color:#15803d}}
    .badge-c{{background:#fef3c7;color:#b45309}}
    .badge-source{{background:#f1f5f9;color:#475569}}
    .tag{{display:inline-block;padding:2px 8px;border-radius:999px;font-size:11px;margin-right:4px}}
    .nav-back{{text-align:center;margin:20px 0;max-width:1100px;margin-left:auto;margin-right:auto}}
    .nav-back a{{color:#64748b;text-decoration:none;font-size:14px}}
    .nav-back a:hover{{color:#2563eb}}
    .footer{{text-align:center;margin-top:40px;padding:20px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;max-width:1100px;margin-left:auto;margin-right:auto}}
    @media (max-width:768px){{
        .layout{{flex-direction:column}}
        .toc{{width:100%;min-width:100%;height:auto;max-height:40vh;position:relative;border-right:none;border-bottom:2px solid #e2e8f0}}
        .content{{max-width:100%;padding:16px}}
        .card{{padding:14px}}
        h3{{padding-right:0}}
        .worth-badge{{position:static;display:inline-block;margin-bottom:8px}}
    }}
</style>
</head>
<body>
<div class="layout">
    <aside class="toc">
        <h2>📑 目录</h2>
        <ul>{toc_html}</ul>
    </aside>
    <main class="content">
        <div class='header'>
            <h1>📚 论文日报</h1>
            <p class='meta'>{date_str} · A组({group_counts.get("A",0)})+B组({group_counts.get("B",0)})+C组({group_counts.get("C",0)}) 共 {total} 篇</p>
            <p class='meta' style='font-size:13px;color:#64748b'>
                A组：目标检测强相关 · B组：端云协同/边缘计算 · C组：其他AI相关
            </p>
            <p class='meta' style='font-size:13px;color:#64748b'>⭐ 精读推荐 20 篇，点击左侧目录跳转</p>
        </div>
        <div class='nav-back'><a href='./index.html'>← 返回首页</a></div>
        {content_html}
        <div class='nav-back'><a href='./index.html'>← 返回首页</a></div>
        <div class='footer'>
            <p>由 WorkBuddy 论文日报管道自动生成</p>
            <p>投递时间：{datetime.now().strftime("%Y-%m-%d %H:%M")} · <a href='https://github.com/miclover0/paper-daily'>miclover0/paper-daily</a></p>
        </div>
    </main>
</div>
</body></html>'''
    return html


# ============================================================
# config.js 更新
# ============================================================

def update_config_json(papers, target_date, groups, html_filename, featured_papers=None):
    """更新 config.json + config.js —— 纯 JSON 数据源 + JS 脚本自动生成，保证绝对合法"""
    config_json_path = os.path.join(REPO_ROOT, "config.json")
    config_js_path = os.path.join(REPO_ROOT, "config.js")

    date_str = target_date.strftime("%Y-%m-%d")
    total = len(papers)

    # 从 config.json 加载已有数据
    data = None
    if os.path.exists(config_json_path):
        try:
            with open(config_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            pass

    if not data or "dailyReports" not in data:
        data = {
            "meta": {
                "title": "Vision Intelligence Daily Archive",
                "subtitle": "Daily Research Paper Digest",
                "description": "Automated collection of cutting-edge research papers in Computer Vision, UAV, FTTA, and Domain Adaptation.",
                "totalPapers": 0,
                "totalDays": 0,
                "lastUpdated": date_str,
                "author": "@miclover0",
                "repository": "https://github.com/miclover0/paper-daily"
            },
            "dailyReports": []
        }

    # 构建日期显示
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = weekday_names[target_date.weekday()]
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    date_display = f"{months[target_date.month-1]} {target_date.day:02d}, {target_date.year}"

    # 构建 featuredPapers（精读推荐，含 readReason）
    featured = []
    if featured_papers:
        for p in featured_papers:
            highlights_list = [h[1] if isinstance(h, tuple) else h for h in p.get("highlights", [])]
            featured.append({
                "title": p["title"],
                "authors": ", ".join(p.get("authors", [])[:3]),
                "venue": f"arXiv {target_date.year}",
                "arxivId": f"arXiv:{p.get('arxiv_id', '')}",
                "tags": p.get("tags", []),
                "summary": p.get("chinese_summary", p.get("summary", "")[:200]),
                "highlights": highlights_list,
                "pdfUrl": p.get("pdf_url", ""),
                "readReason": p.get("read_reason", "")  # 精读原因
            })
    else:
        # 兼容旧逻辑：从 groups 取第一篇作为 featured
        for g in ["A", "B", "C"]:
            if groups.get(g):
                fp = groups[g][0]
                highlights_list = [h[1] if isinstance(h, tuple) else h for h in fp.get("highlights", [])]
                featured.append({
                    "title": fp["title"],
                    "authors": ", ".join(fp.get("authors", [])[:3]),
                    "venue": f"arXiv {target_date.year}",
                    "arxivId": f"arXiv:{fp.get('arxiv_id', '')}",
                    "tags": fp.get("tags", []),
                    "summary": fp.get("chinese_summary", fp.get("summary", "")[:200]),
                    "highlights": highlights_list,
                    "pdfUrl": fp.get("pdf_url", ""),
                    "readReason": fp.get("read_reason", "")
                })
                break

    # 构建 papers 数组
    papers_list = []
    for group_name in ["A", "B", "C"]:
        group_papers = groups.get(group_name, [])
        for idx, p in enumerate(group_papers):
            pid = f"{group_name}{idx+1}"
            highlights_list = [h[1] if isinstance(h, tuple) else h for h in p.get("highlights", [])]
            papers_list.append({
                "id": pid,
                "anchorId": pid,
                "group": group_name,
                "groupName": GROUP_LABELS[group_name],
                "title": p["title"],
                "authors": p.get("authors", []),
                "venue": f"arXiv {target_date.year}",
                "arxivId": f"arXiv:{p.get('arxiv_id', '')}",
                "tags": p.get("tags", []),
                "summary": p.get("chinese_summary", p.get("summary", "")[:200]),
                "highlights": highlights_list,
                "pdfUrl": p.get("pdf_url", ""),
                "worthReading": p.get("worth_reading", False)
            })

    # 构建新条目
    new_entry = {
        "id": date_str,
        "date": date_str,
        "dateDisplay": date_display,
        "weekday": weekday,
        "filename": html_filename,
        "paperCount": total,
        "groups": {g: len(gs) for g, gs in groups.items()},
        "featuredPapers": featured,
        "papers": papers_list
    }

    # 插入到 dailyReports 最前面
    data["dailyReports"] = [r for r in data["dailyReports"] if r.get("id") != date_str]
    data["dailyReports"].insert(0, new_entry)

    # 更新 meta
    data["meta"]["totalPapers"] = sum(r.get("paperCount", 0) for r in data["dailyReports"])
    data["meta"]["totalDays"] = len(data["dailyReports"])
    data["meta"]["lastUpdated"] = date_str

    # 写入 config.json（数据源）和 config.js（供 index.html 加载）
    json_str = json.dumps(data, ensure_ascii=False, indent=2)

    with open(config_json_path, "w", encoding="utf-8") as f:
        f.write(json_str)

    js_content = f"const PAPER_ARCHIVE_CONFIG = {json_str};\n"
    with open(config_js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    log(f"  config.json/config.js 已更新: +{total} 篇, 累计 {data['meta']['totalPapers']}篇/{data['meta']['totalDays']}天")
    return True


# ============================================================
# 主流程
# ============================================================

def main():
    # 解析日期参数
    target_date = datetime.now(timezone.utc).date() - timedelta(days=0)  # 默认今天
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.startswith("--date="):
                try:
                    target_date = datetime.strptime(arg.split("=")[1], "%Y-%m-%d").date()
                except ValueError:
                    log(f"无效日期格式: {arg}")
                    sys.exit(1)

    date_str = target_date.strftime("%Y-%m-%d")
    log(f"=" * 60)
    log(f"📚 论文日报生成 - {date_str}")
    log(f"=" * 60)

    # Step 1: 获取论文
    log("Step 1: 从 ArXiv 获取论文...")
    papers = fetch_papers_by_date(target_date)

    if not papers:
        log(f"⚠️  {date_str} 未找到相关论文")
        # 即使没找到论文也生成空日报
        groups = {"A": [], "B": [], "C": []}
    else:
        log(f"✓ 共获取 {len(papers)} 篇论文")

        # Step 2: 分类
        log("Step 2: 论文分类...")
        for p in papers:
            p["group"] = classify_paper(p)
            p["tags"] = extract_tags(p)

        # 分组
        groups = {"A": [], "B": [], "C": []}
        for p in papers:
            groups[p["group"]].append(p)

        log(f"  A组(检测强相关): {len(groups['A'])} 篇")
        log(f"  B组(端云协同): {len(groups['B'])} 篇")
        log(f"  C组(其他): {len(groups['C'])} 篇")

        # Step 2.5: 筛选强相关论文（从全部论文中筛选前50篇）
        log("Step 2.5: 筛选强相关论文...")
        top_papers = select_top_papers(papers, top_n=50)
        log(f"  从 {len(papers)} 篇中筛选出 {len(top_papers)} 篇强相关论文")

        # 重新分组（只保留筛选后的论文）
        groups = {"A": [], "B": [], "C": []}
        for p in top_papers:
            groups[p["group"]].append(p)

        log(f"  筛选后分组: A组={len(groups['A'])}, B组={len(groups['B'])}, C组={len(groups['C'])}")

        # Step 2.6: 挑选精读推荐（从强相关论文中选前20篇）
        log("Step 2.6: 挑选精读推荐...")
        featured_papers = select_featured_papers(top_papers, top_n=20)

        # 标记精读推荐
        featured_ids = set(p["arxiv_id"] for p in featured_papers)
        for p in top_papers:
            p["worth_reading"] = p["arxiv_id"] in featured_ids

        # Step 3: 评分 & 标记值得精读
        log("Step 3: 论文评分...")
        for p in top_papers:
            p["score"] = score_paper(p, p["group"])

        worth_count = sum(1 for p in top_papers if p.get("worth_reading"))
        log(f"  标记 {worth_count}/{len(top_papers)} 篇为值得精读")

        # Step 4: 生成中文摘要 & 提取信息
        log("Step 4: 生成中文摘要和亮点...")
        for p in top_papers:
            p["chinese_summary"] = generate_chinese_summary(p, p["group"])
            p["main_problem"] = extract_main_problem(p)
            p["highlights"] = extract_highlights(p)
            p["contributions"] = p.get("contributions", "")

    # Step 5: 生成 HTML
    log("Step 5: 生成日报 HTML...")
    # 保存到 daily_reports/ 目录（与 index.html 链接对齐）
    reports_dir = os.path.join(REPO_ROOT, "daily_reports")
    os.makedirs(reports_dir, exist_ok=True)
    html_filename = f"daily_reports/{date_str}-arXiv.html"

    # 使用筛选后的论文生成 HTML
    html_papers = top_papers if 'top_papers' in locals() else papers
    html_groups = groups
    html_path = os.path.join(REPO_ROOT, html_filename)
    html_content = generate_daily_html(html_papers, target_date, html_groups)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    log(f"  HTML 已保存: {html_path}")

    # Step 6: 更新 config.js
    log("Step 6: 更新 config.js...")
    success = update_config_json(
        html_papers, target_date, html_groups, html_filename,
        featured_papers=featured_papers if 'featured_papers' in locals() else None
    )
    if success:
        log("  config.js 更新成功")
    else:
        log("  config.js 更新失败，请手动检查")

    # 总结
    log("=" * 60)
    log(f"✅ 完成！日报 {date_str} 生成完毕")
    log(f"   论文总数: {len(papers)}")
    log(f"   HTML文件: {html_filename}")
    log(f"   config.js: {'已更新' if success else '更新失败'}")
    log("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
