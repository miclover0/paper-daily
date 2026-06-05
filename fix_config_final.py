"""
最终修复脚本：
1. 从 git c4832db 获取正确结构的 config.js 基础
2. 从当前 config.js 提取所有论文数据
3. 重建 config.js
"""
import json, re, os, subprocess

REPO = "C:/Users/miclo/WorkBuddy/2026-06-05-20-27-02/paper-daily"
CONFIG = os.path.join(REPO, "config.js")
NODE = "C:/Users/miclo/.workbuddy/binaries/node/versions/22.22.2/node.exe"

# ============================================================
# 从 git 获取 c4832db 的正确 config.js
# ============================================================
print("Step 1: 获取 c4832db 的正确 config.js...")
r = subprocess.run(["git", "show", "c4832db:config.js"], capture_output=True, text=True, cwd=REPO)
base = r.stdout
if not base:
    print("ERROR: 无法获取")
    exit(1)
print(f"  获取到 {len(base)} 字符")

# ============================================================
# 从当前 config.js 提取论文（用 Node.js 先修正后解析）
# ============================================================
print("\nStep 2: 从当前 config.js 提取论文数据...")
with open(CONFIG, "r", encoding="utf-8") as f:
    curr = f.read()

# 方法: 定位 "id: \"2026-06-05\"" 的位置, 然后找到其 papers: [...] 数组
today_marker = 'id: "2026-06-05"'
pos = curr.find(today_marker)
if pos == -1:
    print("ERROR: 找不到 2026-06-05 条目")
    exit(1)

# 找 papers: [ 开始位置
papers_keyword = curr.find("papers: [", pos)
if papers_keyword == -1:
    print("ERROR: 找不到 papers: [")
    exit(1)

# 追踪括号提取 papers 数组文本
arr_start = curr.find("[", papers_keyword) + 1
depth = 1
i = arr_start
in_dq = False; in_sq = False; esc = False
while i < len(curr) and depth > 0:
    c = curr[i]
    if esc: esc = False
    elif c == '\\': esc = True
    elif c == '"' and not in_sq: in_dq = not in_dq
    elif c == "'" and not in_dq: in_sq = not in_sq
    elif not in_dq and not in_sq:
        if c == '[': depth += 1
        elif c == ']': depth -= 1
    i += 1

papers_raw = curr[arr_start:i-1]
print(f"  提取到 papers 文本, {len(papers_raw)} 字符")

# 分割各个 paper 对象
def split_paper_objects(text):
    """按顶层 { } 分割"""
    papers = []
    depth = 0
    in_str = False; in_sgl = False; esc = False
    current = []
    
    for c in text:
        if esc: esc = False; current.append(c); continue
        if c == '\\': esc = True; current.append(c); continue
        if c == '"' and not in_sgl: in_str = not in_str; current.append(c); continue
        if c == "'" and not in_str: in_sgl = not in_sgl; current.append(c); continue
        if not in_str and not in_sgl:
            if c == '{':
                depth += 1
                if depth == 1: continue  # skip opening brace
            elif c == '}':
                depth -= 1
                if depth == 0:
                    papers.append(''.join(current))
                    current = []
                    continue
        if depth > 0:
            current.append(c)
    
    return papers

raw_papers = split_paper_objects(papers_raw)
print(f"  分割出 {len(raw_papers)} 个论文对象")

# 解析每个论文对象
def parse_paper(raw):
    """从原始文本解析论文字段"""
    def s(name):
        # 提取字符串字段
        for pat in [rf'{name}:\s*"((?:[^"\\]|\\.)*)"', rf"{name}:\s*'((?:[^'\\]|\\.)*)'"]:
            m = re.search(pat, raw)
            if m: 
                val = m.group(1)
                # 处理转义
                val = val.replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
                return val
        return ""
    
    def a(name):
        # 提取数组字段: xxx: [...]
        m = re.search(rf'{name}:\s*\[', raw)
        if not m: return []
        start = m.end() - 1  # position of [
        depth = 1
        i = start + 1
        in_dq = False; in_sq = False; esc = False
        while i < len(raw) and depth > 0:
            c = raw[i]
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"' and not in_sq: in_dq = not in_dq
            elif c == "'" and not in_dq: in_sq = not in_sq
            elif not in_dq and not in_sq:
                if c == '[': depth += 1
                elif c == ']': depth -= 1
            i += 1
        arr_text = raw[start+1:i-1]
        # 尝试用 JSON 解析
        try:
            return json.loads(f"[{arr_text}]")
        except:
            # 手动提取引号字符串
            items = re.findall(r'"((?:[^"\\]|\\.)*)"', arr_text)
            return items
    
    def b(name):
        m = re.search(rf'{name}:\s*(true|false)', raw)
        return m and m.group(1) == 'true'

    return {
        "id": s("id"),
        "group": s("group"),
        "groupName": s("groupName"),
        "title": s("title"),
        "authors": a("authors"),
        "venue": s("venue"),
        "arxivId": s("arxivId"),
        "tags": a("tags"),
        "summary": s("summary"),
        "highlights": a("highlights"),
        "pdfUrl": s("pdfUrl"),
        "worthReading": b("worthReading"),
    }

papers = [parse_paper(p) for p in raw_papers]
print(f"  解析出 {len(papers)} 篇论文")

# 按 group 分类统计
groups = {"A": [], "B": [], "C": []}
for p in papers:
    g = p.get("group", "C")
    groups.setdefault(g, []).append(p)
for g in ["A", "B", "C"]:
    print(f"    {g}组: {len(groups[g])} 篇")

# ============================================================
# 构建今日的日报条目
# ============================================================
print("\nStep 3: 构建今日日报条目...")

def serialize_paper_js(paper, indent=20):
    inner = " " * (indent + 4)
    pref = " " * indent
    
    authors = paper.get("authors", [])
    if isinstance(authors, str):
        authors = [authors] if authors else []
    
    tags = paper.get("tags", [])
    highlights = paper.get("highlights", [])
    if isinstance(highlights, str):
        highlights = [highlights] if highlights else []
    
    worth = "true" if paper.get("worthReading", False) else "false"
    
    return f"""{pref}{{
{inner}id: {json.dumps(paper.get("id", ""), ensure_ascii=False)},
{inner}group: {json.dumps(paper.get("group", ""), ensure_ascii=False)},
{inner}groupName: {json.dumps(paper.get("groupName", ""), ensure_ascii=False)},
{inner}title: {json.dumps(paper.get("title", ""), ensure_ascii=False)},
{inner}authors: {json.dumps(authors, ensure_ascii=False)},
{inner}venue: {json.dumps(paper.get("venue", ""), ensure_ascii=False)},
{inner}arxivId: {json.dumps(paper.get("arxivId", paper.get("arxiv_id", "")), ensure_ascii=False)},
{inner}tags: {json.dumps(tags, ensure_ascii=False)},
{inner}summary: {json.dumps(paper.get("summary", ""), ensure_ascii=False)},
{inner}highlights: {json.dumps(highlights, ensure_ascii=False)},
{inner}pdfUrl: {json.dumps(paper.get("pdfUrl", paper.get("pdf_url", "")), ensure_ascii=False)},
{inner}worthReading: {worth}
{pref}}}"""

# 构建今日条目
paper_strs = []
for g in ["A", "B", "C"]:
    for idx, p in enumerate(groups[g]):
        p["id"] = f"{g}{idx+1}"
        paper_strs.append(serialize_paper_js(p, indent=20))

papers_block = ",\n".join(paper_strs)

# featured paper
featured_block = ""
if groups.get("A"):
    fp = groups["A"][0]
    auth = ", ".join(fp.get("authors", [])[:3]) if fp.get("authors") else ""
    f_tags = fp.get("tags", [])
    f_high = fp.get("highlights", [])
    if isinstance(f_high, str): f_high = [f_high] if f_high else []
    featured_block = f"""            featuredPapers: [
                {{
                    title: {json.dumps(fp.get('title', ''), ensure_ascii=False)},
                    authors: {json.dumps(auth, ensure_ascii=False)},
                    venue: "arXiv 2026",
                    arxivId: {json.dumps(fp.get('arxivId', ''), ensure_ascii=False)},
                    tags: {json.dumps(f_tags, ensure_ascii=False)},
                    summary: {json.dumps(fp.get('summary', ''), ensure_ascii=False)},
                    highlights: {json.dumps(f_high, ensure_ascii=False)},
                    pdfUrl: {json.dumps(fp.get('pdfUrl', ''), ensure_ascii=False)}
                }}
            ],
"""

groupCounts = json.dumps({g: len(gs) for g, gs in groups.items()})

today_entry = f"""        {{
            id: "2026-06-05",
            date: "2026-06-05",
            dateDisplay: "June 05, 2026",
            weekday: "Friday",
            filename: "daily_reports/2026-06-05-arXiv.html",
            paperCount: {len(papers)},
            groups: {groupCounts},
{featured_block}            papers: [
{papers_block}
            ]
        }},"""

print(f"  条目长度: {len(today_entry)} 字符")

# ============================================================
# 插入到基础 config.js
# ============================================================
print("\nStep 4: 插入到基础 config.js...")

# 找到 dailyReports: [ 后面第一个 {
insert_pos = base.find("dailyReports: [")
insert_pos = base.find("{", insert_pos + len("dailyReports: ["))
line_start = base.rfind("\n", 0, insert_pos) + 1

new_config = base[:line_start] + today_entry + "\n" + base[line_start:]

# 更新 meta
old_total = int(re.search(r'totalPapers:\s*(\d+)', base).group(1))
new_total = old_total + len(papers)
new_config = re.sub(r'totalPapers:\s*\d+', f'totalPapers: {new_total}', new_config, count=1)
old_days = int(re.search(r'totalDays:\s*(\d+)', base).group(1))
new_config = re.sub(r'totalDays:\s*\d+', f'totalDays: {old_days + 1}', new_config, count=1)
new_config = re.sub(r'lastUpdated:\s*".*?"', 'lastUpdated: "2026-06-05"', new_config)
new_config = re.sub(r'@lastModified \S+', '@lastModified 2026-06-05', new_config)

# 写入文件
with open(CONFIG, "w", encoding="utf-8") as f:
    f.write(new_config)

# 用 Node 验证
r = subprocess.run([NODE, "--check", CONFIG], capture_output=True, text=True, cwd=REPO,
                   env={**dict(os.environ), "NODE_OPTIONS": ""})
if r.returncode == 0:
    print("✅ config.js 语法合法!")
else:
    print(f"❌ 语法错误: {r.stderr[:300]}")
    # 显示出错行附近
    lines = new_config.split("\n")
    m = re.search(r':(\d+)\b', r.stderr)
    if m:
        ln = int(m.group(1))
        for i in range(max(0, ln-3), min(len(lines), ln+3)):
            marker = ">>>" if i+1 == ln else "   "
            print(f"{marker} {i+1}: {lines[i][:120]}")

print("\n=== 完成 ===")
print(f"论文总数: {len(papers)} 篇")
print(f"文件路径: {CONFIG}")
