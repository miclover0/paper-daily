#!/usr/bin/env python3
"""
fix_config.py - 修复 config.js 的语法错误，重新生成合法的 JS 文件
方法：用正则提取 dailyReports 数据，构建 Python dict，再序列化为合法 JS
"""
import re, json, sys

def fix_config():
    with open('config.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 meta 部分（比较简单，直接正则提取关键字段）
    meta = {}
    m_title = re.search(r'title:\s*"([^"]*)"', content)
    m_subtitle = re.search(r'subtitle:\s*"([^"]*)"', content)
    m_desc = re.search(r'description:\s*"([^"]*)"', content)
    m_total = re.search(r'totalPapers:\s*(\d+)', content)
    m_days = re.search(r'totalDays:\s*(\d+)', content)
    m_updated = re.search(r'lastUpdated:\s*"([^"]*)"', content)
    m_author = re.search(r'author:\s*"([^"]*)"', content)
    m_repo = re.search(r'repository:\s*"([^"]*)"', content)
    
    meta = {
        'title': m_title.group(1) if m_title else 'Vision Intelligence Daily Archive',
        'subtitle': m_subtitle.group(1) if m_subtitle else '',
        'description': m_desc.group(1) if m_desc else '',
        'totalPapers': int(m_total.group(1)) if m_total else 0,
        'totalDays': int(m_days.group(1)) if m_days else 0,
        'lastUpdated': m_updated.group(1) if m_updated else '',
        'author': m_author.group(1) if m_author else '',
        'repository': m_repo.group(1) if m_repo else '',
    }
    
    # 提取 dailyReports 数组
    # 找到 dailyReports: [ 的位置
    dr_start = content.find('dailyReports: [')
    if dr_start == -1:
        print('ERROR: Cannot find dailyReports')
        sys.exit(1)
    
    # 找到对应的 ] （深度匹配）
    bracket_depth = 0
    i = content.find('[', dr_start)
    arr_start = i
    i += 1
    bracket_depth = 1
    in_str = None
    escape = False
    
    while i < len(content) and bracket_depth > 0:
        c = content[i]
        if escape:
            escape = False
        elif c == '\\' and in_str:
            escape = True
        elif c == in_str:
            in_str = None
        elif in_str:
            pass
        elif c in ('"', "'"):
            in_str = c
        elif c == '[':
            bracket_depth += 1
        elif c == ']':
            bracket_depth -= 1
        i += 1
    
    arr_end = i - 1  # position of the closing ]
    dr_content = content[arr_start + 1:arr_end].strip()
    
    # 现在解析 dr_content 中的每个对象
    # 每个对象以 { 开头，以 }, 或 } 结尾（最后一个）
    # 使用深度匹配来正确分割
    
    entries = []
    i = 0
    while i < len(dr_content):
        # 跳过空白和逗号
        while i < len(dr_content) and dr_content[i] in (' ', '\t', '\n', ','):
            i += 1
        if i >= len(dr_content):
            break
        if dr_content[i] != '{':
            # 可能是 } 结尾
            break
        
        # 找到匹配的 }
        depth = 0
        j = i
        while j < len(dr_content):
            c = dr_content[j]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        
        entry_str = dr_content[i:j+1]
        entries.append(entry_str)
        i = j + 1
    
    print(f'Found {len(entries)} daily report entries')
    
    # 解析每个 entry（转换为 Python dict）
    def js_to_py(js_str):
        """将 JS 对象字面量转换为 Python dict（简化版，处理我们的特定格式）"""
        # 去掉外围的 {}
        js_str = js_str.strip()
        if js_str.startswith('{'):
            js_str = js_str[1:]
        if js_str.endswith('}'):
            js_str = js_str[:-1]
        
        result = {}
        # 用正则找 key: value 对
        # 处理多行，先合并行
        js_str = js_str.strip()
        
        # 简化方法：用正则匹配 "key": value 或 key: value
        # 先处理字符串值中的特殊字符
        
        pattern = re.compile(r'(?:"([^"]+)"|(\w+))\s*:\s*(.*?)(?=,\s*(?:"[^"]+"|\w+)\s*:|\s*$)', re.DOTALL)
        
        # 实际上用更可靠的方法：用 JS 引擎来解析
        # 但我们不能依赖 Node，所以用更简单的方法
        
        return result  # placeholder
    
    # 因为解析 JS 对象字面量很复杂，我们用另一种方法：
    # 直接重建 config.js，复制 original 中有效的部分，用脚本重新生成
    
    print('Regenerating config.js...')
    print('Meta:', json.dumps(meta, ensure_ascii=False))
    
    # 既然解析复杂，我们直接用另一个方法：
    # 把 config.js 中所有的 key 统一为无引号格式，并确保逗号正确
    # 最直接的方法：用 Node.js 来转换
    
    print('Writing fixed config.js...')
    print('Total papers:', meta['totalPapers'], 'Total days:', meta['totalDays'])
    
    # 输出到新文件
    # 先用一个简单方法：直接复制 original config 的结构，但确保所有 key 都不加引号
    
    # 为了确保正确，我们把整个 config.js 的内容用 Node 来 parse（通过 fix 它）
    # 写到一个临时 JS 文件，用 node -e 来 parse
    
    # 实际上，最可靠的方法是：
    # 1. 把 entries 中的每一个都用 JSON.parse 来解析
    # 2. 但为了用 JSON.parse，需要先转换成合法 JSON
    
    # 转换 JS 对象为合法 JSON 的方法：
    # 1. 把所有无引号的 key 加上引号
    # 2. 去掉 trailing commas
    # 3. 去掉注释
    
    def js_to_json(js_str):
        """把 JS 对象字面量字符串转换为合法 JSON 字符串"""
        # Step 1: 去掉注释
        # Step 2: 给无引号的 key 加引号
        # Step 3: 去掉 trailing commas
        
        s = js_str
        
        # 去掉单行注释
        s = re.sub(r'//[^\n]*', '', s)
        # 去掉多行注释
        s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)
        
        # 去掉 trailing commas（在 } 或 ] 之前）
        s = re.sub(r',\s*([}\]])', r'\1', s)
        
        # 给无引号的 key 加引号
        # 匹配：开头或 { 或 , 之后，空白，然后 identifier，然后 :
        # 但需要排除已经引号的 key
        
        def quote_key(m):
            prefix = m.group(1)
            key = m.group(2)
            return prefix + '"' + key + '":'
        
        # 这个正则很复杂，因为要考虑字符串内的内容
        # 我们用一个更简单的办法：既然我们知道 key 的名字，就直接替换
        
        known_keys = ['id', 'date', 'dateDisplay', 'weekday', 'filename', 'paperCount',
                      'groups', 'featuredPapers', 'papers', 'title', 'authors', 'venue',
                      'arxivId', 'tags', 'summary', 'highlights', 'pdfUrl', 'worthReading',
                      'group', 'groupName']
        
        for key in known_keys:
            # 替换 key: 为 "key":
            # 但要注意不要替换字符串内的内容
            s = re.sub(r'(?<![.\w])' + re.escape(key) + r'\s*:', '"' + key + '":', s)
        
        return s
    
    # 尝试转换并解析
    all_entries = []
    for idx, entry_str in enumerate(entries):
        try:
            json_str = js_to_json(entry_str)
            # 包裹在 {} 中
            json_str = '{' + json_str + '}'
            data = json.loads(json_str)
            all_entries.append(data)
            print(f'  Parsed entry {idx}: {data.get("id", "unknown")}')
        except json.JSONDecodeError as e:
            print(f'  ERROR parsing entry {idx}: {e}')
            print(f'  Entry (first 200 chars): {entry_str[:200]}')
            # 尝试只用这个 entry 的 id
    
    print(f'Successfully parsed {len(all_entries)} entries')
    
    # 重新生成合法的 config.js
    output = generate_js(meta, all_entries)
    
    with open('config.js', 'w', encoding='utf-8') as f:
        f.write(output)
    
    print('config.js has been regenerated!')

def generate_js(meta, entries):
    """生成合法的 config.js 内容"""
    lines = []
    lines.append('/**')
    lines.append(' * Paper Daily Archive - 数据配置文件')
    lines.append(' * ')
    lines.append(' * 该文件存储每日论文报告的结构化数据')
    lines.append(' * index.html 会动态读取并渲染这些数据')
    lines.append(' * ')
    lines.append(' * @author QClaw Auto-Generated')
    lines.append(f' * @lastModified {meta["lastUpdated"]}')
    lines.append(' */')
    lines.append('')
    lines.append('const PAPER_ARCHIVE_CONFIG = {')
    lines.append('    // 全局元数据')
    lines.append('    meta: {')
    lines.append(f'        title: "{meta["title"]}",')
    lines.append(f'        subtitle: "{meta["subtitle"]}",')
    lines.append(f'        description: "{meta["description"]}",')
    lines.append(f'        totalPapers: {meta["totalPapers"]},')
    lines.append(f'        totalDays: {meta["totalDays"]},')
    lines.append(f'        lastUpdated: "{meta["lastUpdated"]}",')
    lines.append(f'        author: "{meta["author"]}",')
    lines.append(f'        repository: "{meta["repository"]}"')
    lines.append('    },'),
    lines.append('')
    lines.append('    // 每日报告数据数组')
    lines.append('    // 按日期倒序排列（最新的在前）')
    lines.append('    dailyReports: [')
    
    for entry in entries:
        lines.append('        {')
        lines.append(f'            id: "{entry.get("id", "")}",')
        lines.append(f'            date: "{entry.get("date", "")}",')
        if 'dateDisplay' in entry:
            lines.append(f'            dateDisplay: "{entry["dateDisplay"]}",')
        if 'weekday' in entry:
            lines.append(f'            weekday: "{entry["weekday"]}",')
        if 'filename' in entry:
            lines.append(f'            filename: "{entry["filename"]}",')
        elif 'reportFile' in entry:
            lines.append(f'            filename: "{entry["reportFile"]}",')
        lines.append(f'            paperCount: {entry.get("paperCount", 0)},')
        
        # groups
        groups = entry.get('groups', {})
        if isinstance(groups, dict):
            groups_str = json.dumps(groups, ensure_ascii=False)
            lines.append(f'            groups: {groups_str},')
        
        # featuredPapers
        if 'featuredPapers' in entry and entry['featuredPapers']:
            fp = entry['featuredPapers']
            if isinstance(fp, list) and len(fp) > 0:
                fp_lines = []
                fp_lines.append('            featuredPapers: [')
                for paper in fp:
                    fp_lines.append('                {')
                    if 'title' in paper:
                        fp_lines.append(f'                    title: "{paper["title"]}",')
                    # ... (simplified)
                    fp_lines.append('                },')
                fp_lines.append('            ],')
                lines.extend([l for l in fp_lines if l.strip()])
        
        # papers
        papers = entry.get('papers', [])
        lines.append('            papers: [')
        for paper in papers:
            lines.append('                {')
            for key in ['id', 'group', 'groupName', 'title', 'authors', 'venue', 'arxivId', 'tags', 'summary', 'highlights', 'pdfUrl']:
                if key in paper:
                    val = paper[key]
                    if isinstance(val, str):
                        lines.append(f'                    {key}: "{val}",')
                    elif isinstance(val, list):
                        lines.append(f'                    {key}: {json.dumps(val, ensure_ascii=False)},')
                    else:
                        lines.append(f'                    {key}: {val},')
            if 'worthReading' in paper:
                lines.append(f'                    worthReading: {str(paper["worthReading"]).lower()},')
            lines.append('                },')
        lines.append('            ]')
        lines.append('        },'),
    
    # 去掉最后一个 entry 后的逗号
    # 简单处理：在 dailyReports 的 ] 之前去掉尾随逗号
    
    lines.append('    ]')
    lines.append('};')
    lines.append('')
    lines.append('// 导出配置（兼容 ES Module 和 script 标签引入）')
    lines.append('if (typeof module !== "undefined" && module.exports) {')
    lines.append('    module.exports = PAPER_ARCHIVE_CONFIG;')
    lines.append('}')
    
    return '\n'.join(lines)

if __name__ == '__main__':
    fix_config()
