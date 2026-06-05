"""
从 c4832db 的正确 config.js 恢复基础结构，
然后重新插入今天（2026-06-05）的数据。

策略：用 Python 的 json 序列化处理所有数据，
手动拼接 JS 对象字面量而非 f-string 嵌套大括号。
"""
import re
import json
import os
import subprocess
from datetime import date as Date

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(REPO_ROOT, "config.js")

# ============================================================
# Step 1: 从当前 config.js（今天的已生成版本）提取今日论文数据
# ============================================================

def extract_today_data():
    """从今天已生成的 config.js 中提取 2026-06-05 的 papers 数组"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 尝试用 Node 解析，提取 papers 数组
    # 直接定位 "id: \"2026-06-05\"" 并在其上下文中提取 papers 数组
    
    # 找到 today 的入口
    today_marker = 'id: "2026-06-05"'
    today_pos = content.find(today_marker)
    if today_pos == -1:
        print("ERROR: 未找到 2026-06-05 的日报条目")
        return None
    
    # 找到 papers: [
    papers_start = content.find("papers: [", today_pos)
    if papers_start == -1:
        print("ERROR: 未找到 papers 数组")
        return None
    
    # 手工追踪括号，找到匹配的 ]
    bracket_depth = 0
    in_string = False
    in_single = False
    esc = False
    pos = content.find("[", papers_start) + 1  # 跳过最初的 [
    start = pos
    bracket_depth = 1
    
    while pos < len(content) and bracket_depth > 0:
        c = content[pos]
        if esc:
            esc = False
        elif c == '\\':
            esc = True
        elif c == '"' and not in_single:
            in_string = not in_string
        elif c == "'" and not in_string:
            in_single = not in_single
        elif not in_string and not in_single:
            if c == '[':
                bracket_depth += 1
            elif c == ']':
                bracket_depth -= 1
        pos += 1
    
    papers_text = content[start:pos-1]
    
    # 现在用 Node.js 解析这个 JS 数组
    # 写一个临时 Node 脚本来解析
    temp_js = f"""
const fs = require('fs');
try {{
    const data = [{papers_text}];
    console.log(JSON.stringify(data));
}} catch(e) {{
    console.error('PARSE_ERROR:', e.message);
    process.exit(1);
}}
"""
    temp_path = os.path.join(REPO_ROOT, "_temp_parse.js")
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(temp_js)
    
    result = subprocess.run(
        ["C:/Users/miclo/.workbuddy/binaries/node/versions/22.22.2/node.exe", temp_path],
        capture_output=True, text=True, cwd=REPO_ROOT,
        env={**dict(os.environ), "NODE_OPTIONS": ""}
    )
    os.unlink(temp_path)
    
    if result.returncode != 0:
        print(f"Node parse error: {result.stderr}")
        # 回退：提取 JSON 字符串
        return extract_via_regex(papers_text)
    
    return json.loads(result.stdout.strip())


def extract_via_regex(text):
    """回退方案：用正则提取论文条目"""
    papers = []
    # 匹配每个 {...} 对象
    brace_depth = 0
    in_str = False
    in_sgl = False
    esc = False
    current = ""
    
    for c in text:
        if esc:
            esc = False
            current += c
            continue
        if c == '\\':
            esc = True
            current += c
            continue
        if c == '"' and not in_sgl:
            in_str = not in_str
            current += c
            continue
        if c == "'" and not in_str:
            in_sgl = not in_sgl
            current += c
            continue
        if not in_str and not in_sgl:
            if c == '{':
                brace_depth += 1
                if brace_depth == 1:
                    current = ""
                    continue
            elif c == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    paper = parse_one_paper(current)
                    if paper:
                        papers.append(paper)
                    continue
        if brace_depth > 0:
            current += c
    
    return papers


def parse_one_paper(text):
    """解析一个论文对象文本为 dict"""
    paper = {}
    
    def extract_str_field(name):
        patterns = [
            rf'{name}:\s*"([^"]*)"',
        ]
        for p in patterns:
            m = re.search(p, text)
            if m:
                return m.group(1)
        return None
    
    def extract_arr_field(name):
        # 找到 name: [ 后面的数组
        m = re.search(rf'{name}:\s*\[', text)
        if not m:
            return []
        start = m.end() - 1  # position of [
        depth = 0
        in_str = False
        esc = False
        pos = start
        while pos < len(text):
            c = text[pos]
            if esc:
                esc = False
            elif c == '\\':
                esc = True
            elif c == '"':
                in_str = not in_str
            elif not in_str:
                if c == '[':
                    depth += 1
                elif c == ']':
                    depth -= 1
                    if depth == 0:
                        arr_text = text[start+1:pos]
                        # Parse JSON array
                        items = json.loads(f"[{arr_text}]")
                        return items
            pos += 1
        return []
    
    def extract_bool_field(name):
        m = re.search(rf'{name}:\s*(true|false)', text)
        return m.group(1) == "true" if m else False
    
    paper['id'] = extract_str_field('id') or ""
    paper['group'] = extract_str_field('group') or ""
    paper['groupName'] = extract_str_field('groupName') or ""
    paper['title'] = extract_str_field('title') or ""
    paper['authors'] = extract_arr_field('authors')
    paper['venue'] = extract_str_field('venue') or ""
    paper['arxivId'] = extract_str_field('arxivId') or ""
    paper['tags'] = extract_arr_field('tags')
    paper['summary'] = extract_str_field('summary') or ""
    paper['highlights'] = extract_arr_field('highlights')
    paper['pdfUrl'] = extract_str_field('pdfUrl') or ""
    paper['worthReading'] = extract_bool_field('worthReading')
    
    return paper


# ============================================================
# Step 2: 从 git 获取基础 config.js（c4832db）
# ============================================================

def get_base_config():
    result = subprocess.run(
        ["git", "show", "c4832db:config.js"],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout if result.returncode == 0 else None


# ============================================================
# Step 3: 构建完整的 config.js
# ============================================================

def serialize_value(v):
    """将 Python 值序列化为 JS 字面量"""
    if isinstance(v, bool):
        return "true" if v else "false"
    elif isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    elif isinstance(v, (int, float)):
        return str(v)
    elif isinstance(v, list):
        items = [json.dumps(item, ensure_ascii=False) for item in v]
        return "[" + ", ".join(items) + "]"
    elif isinstance(v, dict):
        return "{" + ", ".join(
            f"{k}: {serialize_value(val)}"
            for k, val in v.items()
        ) + "}"
    return json.dumps(v, ensure_ascii=False)


def indent_lines(text, spaces):
    """给多行文本的每一行添加缩进"""
    return "\n".join(" " * spaces + line if line.strip() else line
                     for line in text.split("\n"))


def serialize_paper(paper, indent=20):
    """将论文对象序列化为 JS 对象字面量"""
    lines = []
    prefix = " " * indent
    inner = " " * (indent + 4)
    
    lines.append(f"{prefix}{{")
    lines.append(f'{inner}id: {json.dumps(paper.get("id", ""), ensure_ascii=False)},')
    lines.append(f'{inner}group: {json.dumps(paper.get("group", ""), ensure_ascii=False)},')
    lines.append(f'{inner}groupName: {json.dumps(paper.get("groupName", ""), ensure_ascii=False)},')
    lines.append(f'{inner}title: {json.dumps(paper.get("title", ""), ensure_ascii=False)},')
    
    authors = paper.get("authors", [])
    if isinstance(authors, str):
        authors = [authors]
    lines.append(f'{inner}authors: {json.dumps(authors, ensure_ascii=False)},')
    
    lines.append(f'{inner}venue: {json.dumps(paper.get("venue", ""), ensure_ascii=False)},')
    lines.append(f'{inner}arxivId: {json.dumps(paper.get("arxivId", paper.get("arxiv_id", "")), ensure_ascii=False)},')
    
    tags = paper.get("tags", [])
    lines.append(f'{inner}tags: {json.dumps(tags, ensure_ascii=False)},')
    lines.append(f'{inner}summary: {json.dumps(paper.get("summary", ""), ensure_ascii=False)},')
    
    highlights = paper.get("highlights", [])
    if isinstance(highlights, str):
        highlights = [highlights]
    lines.append(f'{inner}highlights: {json.dumps(highlights, ensure_ascii=False)},')
    
    lines.append(f'{inner}pdfUrl: {json.dumps(paper.get("pdfUrl", paper.get("pdf_url", "")), ensure_ascii=False)},')
    
    worth = paper.get("worthReading", paper.get("worth_reading", False))
    lines.append(f'{inner}worthReading: {serialize_value(bool(worth))}')
    
    lines.append(f"{prefix}}}")
    return "\n".join(lines)


def build_today_entry(papers, date_str="2026-06-05", html_filename="daily_reports/2026-06-05-arXiv.html"):
    """构建今日的日报条目"""
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    d = Date.fromisoformat(date_str)
    date_display = f"{months[d.month-1]} {d.day:02d}, {d.year}"
    weekday = weekday_names[d.weekday()]
    
    # 分组统计
    groups = {"A": [], "B": [], "C": []}
    for p in papers:
        g = p.get("group", "C")
        if g in groups:
            groups[g].append(p)
        else:
            groups["C"].append(p)
    
    total = len(papers)
    
    lines = []
    lines.append("        {")
    lines.append(f'            id: "{date_str}",')
    lines.append(f'            date: "{date_str}",')
    lines.append(f'            dateDisplay: "{date_display}",')
    lines.append(f'            weekday: "{weekday}",')
    lines.append(f'            filename: "{html_filename}",')
    lines.append(f"            paperCount: {total},")
    
    group_counts = {g: len(gs) for g, gs in groups.items()}
    lines.append(f"            groups: {json.dumps(group_counts)},")
    
    # featuredPapers (取第一篇 A 组论文)
    featured = groups.get("A", [])
    if not featured:
        featured = groups.get("B", []) if groups.get("B") else groups.get("C", [])
    
    if featured:
        fp = featured[0]
        lines.append("            featuredPapers: [")
        lines.append("                {")
        lines.append(f"                    title: {json.dumps(fp.get('title', ''), ensure_ascii=False)},")
        authors_str = ", ".join(fp.get("authors", [])[:3]) if isinstance(fp.get("authors"), list) else fp.get("authors", "")
        lines.append(f"                    authors: {json.dumps(authors_str, ensure_ascii=False)},")
        lines.append(f'                    venue: "arXiv {d.year}",')
        lines.append(f'                    arxivId: {json.dumps(fp.get("arxivId", fp.get("arxiv_id", "")), ensure_ascii=False)},')
        tags = fp.get("tags", [])
        lines.append(f"                    tags: {json.dumps(tags, ensure_ascii=False)},")
        lines.append(f"                    summary: {json.dumps(fp.get('summary', ''), ensure_ascii=False)},")
        highlights = fp.get("highlights", [])
        if isinstance(highlights, str):
            highlights = [highlights]
        lines.append(f"                    highlights: {json.dumps(highlights, ensure_ascii=False)},")
        lines.append(f"                    pdfUrl: {json.dumps(fp.get('pdfUrl', fp.get('pdf_url', '')), ensure_ascii=False)}")
        lines.append("                }")
        lines.append("            ],")
    
    # papers 数组
    lines.append("            papers: [")
    paper_strs = []
    for g_name in ["A", "B", "C"]:
        for idx, p in enumerate(groups.get(g_name, [])):
            p_with_id = dict(p)
            p_with_id["id"] = f"{g_name}{idx+1}"
            paper_strs.append(serialize_paper(p_with_id, indent=20))
    lines.append(",\n".join(paper_strs))
    lines.append("            ]")
    lines.append("        },")
    
    return "\n".join(lines)


def main():
    print("=" * 60)
    print("重建 config.js")
    print("=" * 60)
    
    # Step 1: 获取基础 config.js
    print("\nStep 1: 获取基础 config.js (c4832db)...")
    base = get_base_config()
    if not base:
        print("ERROR: 无法获取基础 config.js")
        return
    
    # 验证基础版本
    with open("_base_check.js", "w", encoding="utf-8") as f:
        f.write(base)
    result = subprocess.run(
        ["C:/Users/miclo/.workbuddy/binaries/node/versions/22.22.2/node.exe", "--check", "_base_check.js"],
        capture_output=True, text=True, cwd=REPO_ROOT,
        env={**dict(os.environ), "NODE_OPTIONS": ""}
    )
    if result.returncode != 0:
        print(f"基础 config.js 验证失败: {result.stderr}")
        # 仍然继续
    else:
        print("基础 config.js 语法合法")
    
    # Step 2: 提取今日论文
    print("\nStep 2: 提取今日 (2026-06-05) 论文数据...")
    today_papers = extract_today_data()
    if not today_papers:
        print("ERROR: 无法提取今日论文数据")
        return
    print(f"提取到 {len(today_papers)} 篇论文")
    
    # Step 3: 构建今日条目
    print("\nStep 3: 构建今日日报条目...")
    today_entry = build_today_entry(today_papers)
    
    # Step 4: 插入到基础 config.js 中
    print("\nStep 4: 插入到基础 config.js...")
    
    # 找到 dailyReports: [ 后面的第一个 {
    insert_pos = base.find("dailyReports: [")
    if insert_pos == -1:
        print("ERROR: 找不到 dailyReports: [")
        return
    
    insert_pos = base.find("{", insert_pos)
    if insert_pos == -1:
        print("ERROR: 找不到 {")
        return
    
    # 找到这一行的开头
    line_start = base.rfind("\n", 0, insert_pos) + 1
    indent = base[line_start:insert_pos]
    
    # 构建新的 config.js
    new_config = base[:line_start] + today_entry + "\n" + base[line_start:]
    
    # 更新 meta
    # totalPapers: 加上今天的论文数
    meta_match = re.search(r'totalPapers:\s*(\d+)', base)
    if meta_match:
        old_total = int(meta_match.group(1))
        new_total = old_total + len(today_papers)
        new_config = re.sub(
            r'totalPapers:\s*\d+',
            f'totalPapers: {new_total}',
            new_config,
            count=1
        )
    
    # totalDays: +1
    meta_match = re.search(r'totalDays:\s*(\d+)', base)
    if meta_match:
        old_days = int(meta_match.group(1))
        new_days = old_days + 1
        new_config = re.sub(
            r'totalDays:\s*\d+',
            f'totalDays: {new_days}',
            new_config,
            count=1
        )
    
    # lastUpdated
    new_config = re.sub(
        r'lastUpdated:\s*".*?"',
        'lastUpdated: "2026-06-05"',
        new_config
    )
    
    # lastModified
    new_config = re.sub(
        r'@lastModified \S+',
        '@lastModified 2026-06-05',
        new_config
    )
    
    # 写入文件
    print(f"\n写入 config.js...")
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(new_config)
    
    # 验证
    print("验证 config.js...")
    result = subprocess.run(
        ["C:/Users/miclo/.workbuddy/binaries/node/versions/22.22.2/node.exe", "--check", CONFIG_PATH],
        capture_output=True, text=True, cwd=REPO_ROOT,
        env={**dict(os.environ), "NODE_OPTIONS": ""}
    )
    
    if result.returncode == 0:
        print("✅ config.js 语法合法！")
    else:
        print(f"❌ 语法错误: {result.stderr}")
        # 显示出错行附近内容
        print(f"\nstdout: {result.stdout}")
    
    # 清理
    if os.path.exists("_base_check.js"):
        os.unlink("_base_check.js")
    
    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
