#!/usr/bin/env python3
"""
fix_config_v2.py - 完整修复 config.js
方法：正则提取 dailyReports 数据 → Python dict → 合法 JS 对象字面量
"""
import re, json, sys, os

def extract_string(content, start):
    """从 start 位置提取字符串（支持引号转义），返回 (字符串, 结束位置)"""
    quote_char = content[start]
    result = []
    i = start + 1
    while i < len(content):
        c = content[i]
        if c == '\\':
            result.append(c)
            result.append(content[i+1])
            i += 2
        elif c == quote_char:
            return ''.join(result), i + 1
        else:
            result.append(c)
            i += 1
    return ''.join(result), i

def extract_value(content, start):
    """
    从 start 位置提取一个 JS 值，返回 (value, end_pos)
    value 是 Python 对象（str, list, dict, number, bool, None）
    """
    i = start
    while i < len(content) and content[i] in ' \t\n\r':
        i += 1
    if i >= len(content):
        return None, i
    
    c = content[i]
    
    # 字符串
    if c in ('"', "'"):
        s, end = extract_string(content, i)
        return s, end
    
    # 数组
    if c == '[':
        arr = []
        i += 1
        while i < len(content):
            while i < len(content) and content[i] in ' \t\n\r,':
                i += 1
            if i < len(content) and content[i] == ']':
                i += 1
                break
            val, end = extract_value(content, i)
            arr.append(val)
            i = end
        return arr, i
    
    # 对象
    if c == '{':
        obj = {}
        i += 1
        while i < len(content):
            while i < len(content) and content[i] in ' \t\n\r,':
                i += 1
            if i < len(content) and content[i] == '}':
                i += 1
                break
            # 读取 key
            key, end = extract_key(content, i)
            i = end
            # 跳过 :
            while i < len(content) and content[i] in ' \t\n\r:':
                i += 1
            # 读取值
            val, end = extract_value(content, i)
            obj[key] = val
            i = end
        return obj, i
    
    # 数字 / true / false / null
    m = re.match(r'(true|false|null|[\d.]+)', content[i:], re.IGNORECASE)
    if m:
        word = m.group(1)
        if word.lower() == 'true':
            return True, i + len(word)
        if word.lower() == 'false':
            return False, i + len(word)
        if word.lower() == 'null':
            return None, i + len(word)
        # 数字
        try:
            if '.' in word:
                return float(word), i + len(word)
            return int(word), i + len(word)
        except:
            pass
    
    return None, i

def extract_key(content, start):
    """提取对象的 key，返回 (key_str, end_pos)"""
    i = start
    # 跳过空白
    while i < len(content) and content[i] in ' \t\n\r':
        i += 1
    
    c = content[i] if i < len(content) else ''
    
    # 引号包裹的 key
    if c in ('"', "'"):
        s, end = extract_string(content, i)
        return s, end
    
    # 无引号 key（JS 标识符）
    m = re.match(r'[\w$]+', content[i:])
    if m:
        return m.group(0), i + len(m.group(0))
    
    return '', i

def parse_js_object(js_str):
    """
    将 JS 对象字面量字符串解析为 Python dict。
    支持：引号/无引号 key、字符串值、数组、嵌套对象、数字、bool、null。
    """
    js_str = js_str.strip()
    # 去掉外层 {}
    if js_str.startswith('{'):
        js_str = js_str[1:]
    if js_str.endswith('}'):
        js_str = js_str[:-1]
    
    # 使用 extract_value 来解析
    obj, _ = extract_value('{' + js_str + '}', 0)
    return obj

def parse_daily_report_entries(content):
    """从 config.js 内容中提取所有 dailyReports 条目，返回 list of dict"""
    # 找到 dailyReports 数组内容
    dr_match = re.search(r'dailyReports:\s*\[', content)
    if not dr_match:
        print("ERROR: dailyReports not found")
        return []
    
    arr_start = dr_match.end() - 1  # '[' 的位置
    # 找到匹配的 ]
    depth = 0
    i = arr_start
    while i < len(content):
        c = content[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                arr_end = i
                break
        i += 1
    else:
        print("ERROR: unclosed dailyReports array")
        return []
    
    arr_content = content[arr_start + 1:arr_end]
    
    # 提取每个 { ... } 条目
    entries = []
    i = 0
    while i < len(arr_content):
        while i < len(arr_content) and arr_content[i] in ' \t\n\r,':
            i += 1
        if i >= len(arr_content):
            break
        if arr_content[i] != '{':
            i += 1
            continue
        
        # 找到匹配的 }
        depth = 0
        j = i
        while j < len(arr_content):
            c = arr_content[j]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        
        entry_str = arr_content[i:j+1]
        try:
            entry = parse_js_object(entry_str)
            if entry and 'id' in entry:
                entries.append(entry)
                print(f"  Parsed: {entry.get('id', '?')} ({len(entry.get('papers', []))} papers)")
        except Exception as e:
            print(f"  ERROR parsing entry at pos {i}: {e}")
            print(f"  Entry preview: {entry_str[:200]}")
        
        i = j + 1
    
    return entries

def extract_meta(content):
    """提取 meta 对象"""
    meta_match = re.search(r'meta:\s*\{', content)
    if not meta_match:
        return {}
    
    meta_start = meta_match.end() - 1
    depth = 0
    i = meta_start
    while i < len(content):
        c = content[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                meta_end = i
                break
        i += 1
    else:
        return {}
    
    meta_str = content[meta_start:meta_end+1]
    try:
        return parse_js_object(meta_str)
    except:
        return {}

def serialize_value(val, indent=0):
    """将 Python 值序列化为 JS 字面量（无引号 key）"""
    pad = '    ' * indent
    pad1 = '    ' * (indent + 1)
    
    if val is None:
        return 'null'
    if isinstance(val, bool):
        return 'true' if val else 'false'
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        return str(val)
    if isinstance(val, str):
        # 转义 JS 字符串
        escaped = val.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
        return f'"{escaped}"'
    if isinstance(val, list):
        items = []
        for item in val:
            items.append(pad1 + serialize_value(item, indent + 1))
        return '[\n' + ',\n'.join(items) + '\n' + pad + ']'
    if isinstance(val, dict):
        items = []
        for k, v in val.items():
            items.append(f'{pad1}{k}: {serialize_value(v, indent + 1)}')
        return '{\n' + ',\n'.join(items) + '\n' + pad + '}'
    return str(val)

def serialize_paper(paper, indent=0):
    """序列化单篇论文条目（特殊处理 authors 数组）"""
    pad = '    ' * indent
    pad1 = '    ' * (indent + 1)
    lines = []
    lines.append(pad + '{')
    
    for key in ['id', 'group', 'groupName', 'title', 'authors', 'venue', 'arxivId', 'tags', 'summary', 'highlights', 'pdfUrl', 'worthReading']:
        if key not in paper:
            continue
        val = paper[key]
        if key == 'authors' and isinstance(val, list):
            authors_str = '[' + ', '.join(f'"{a}"' for a in val) + ']'
            lines.append(f'{pad1}{key}: {authors_str},')
        elif key == 'tags' and isinstance(val, list):
            tags_str = '[' + ', '.join(f'"{t}"' for t in val) + ']'
            lines.append(f'{pad1}{key}: {tags_str},')
        elif key == 'highlights' and isinstance(val, list):
            hl_str = '[' + ', '.join(f'"{h}"' for h in val) + ']'
            lines.append(f'{pad1}{key}: {hl_str},')
        elif key == 'worthReading':
            lines.append(f'{pad1}{key}: {"true" if val else "false"},')
        elif isinstance(val, str):
            lines.append(f'{pad1}{key}: {serialize_value(val)},')
        else:
            lines.append(f'{pad1}{key}: {serialize_value(val)},')
    
    # 去掉最后一行的逗号（JS 允许尾逗号，但严谨一点）
    if lines[-1].endswith(','):
        lines[-1] = lines[-1][:-1]
    
    lines.append(pad + '}')
    return '\n'.join(lines)

def generate_config_js(meta, entries):
    """生成完整的合法 config.js 内容"""
    lines = []
    lines.append('/**')
    lines.append(' * Paper Daily Archive - 数据配置文件')
    lines.append(' * ')
    lines.append(' * 该文件存储每日论文报告的结构化数据')
    lines.append(' * index.html 会动态读取并渲染这些数据')
    lines.append(' * ')
    lines.append(' * @author QClaw Auto-Generated')
    lines.append(f' * @lastModified {meta.get("lastUpdated", "")}')
    lines.append(' */')
    lines.append('')
    lines.append('const PAPER_ARCHIVE_CONFIG = {')
    lines.append('    // 全局元数据')
    lines.append('    meta: {')
    lines.append(f'        title: "{meta.get("title", "")}",')
    lines.append(f'        subtitle: "{meta.get("subtitle", "")}",')
    lines.append(f'        description: "{meta.get("description", "")}",')
    lines.append(f'        totalPapers: {meta.get("totalPapers", 0)},')
    lines.append(f'        totalDays: {meta.get("totalDays", 0)},')
    lines.append(f'        lastUpdated: "{meta.get("lastUpdated", "")}",')
    lines.append(f'        author: "{meta.get("author", "")}",')
    lines.append(f'        repository: "{meta.get("repository", "")}"')
    lines.append('    },')
    lines.append('')
    lines.append('    // 每日报告数据数组')
    lines.append('    // 按日期倒序排列（最新的在前）')
    lines.append('    dailyReports: [')
    
    for idx, entry in enumerate(entries):
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
            groups_js = '{' + ', '.join(f'"{k}": {v}' for k, v in groups.items()) + '}'
            lines.append(f'            groups: {groups_js},')
        
        # featuredPapers
        fp_list = entry.get('featuredPapers', [])
        if fp_list and isinstance(fp_list, list) and len(fp_list) > 0:
            lines.append('            featuredPapers: [')
            for fp in fp_list:
                lines.append('                {')
                for k, v in fp.items():
                    if isinstance(v, str):
                        lines.append(f'                    {k}: "{v}",')
                    elif isinstance(v, list):
                        v_str = '[' + ', '.join(f'"{x}"' for x in v) + ']'
                        lines.append(f'                    {k}: {v_str},')
                    else:
                        lines.append(f'                    {k}: {json.dumps(v, ensure_ascii=False)},')
                # 去掉最后逗号
                if lines[-1].endswith(','):
                    lines[-1] = lines[-1][:-1]
                lines.append('                },')
            # 去掉最后一个条目的逗号
            if lines[-1].endswith(','):
                lines[-1] = lines[-1][:-1]
            lines.append('            ],')
        
        # papers
        papers = entry.get('papers', [])
        lines.append('            papers: [')
        for paper in papers:
            p_lines = serialize_paper(paper, 0).split('\n')
            for pl in p_lines:
                if pl.strip() == '{':
                    lines.append('                {')
                elif pl.strip() == '}':
                    lines.append('                }')
                else:
                    lines.append('                ' + pl.strip())
            lines.append('                },')
        
        if lines[-1].strip() == '},':
            lines[-1] = lines[-1][:-1]  # 去掉尾逗号
        
        lines.append('            ]')
        lines.append('        }')
        
        if idx < len(entries) - 1:
            lines[-2] = lines[-2] + ','  # 条目间加逗号
        
        lines.append('')
    
    # 去掉最后一个条目前的空行和逗号，正确处理
    # 简化处理：加 ], 然后处理尾逗号
    lines.append('    ]')
    lines.append('};')
    lines.append('')
    lines.append('// 标签元数据（用于配色）')
    lines.append('tagColors: {')
    lines.append('    "DAOD": { bg: "#7c3aed", text: "#fff" },')
    lines.append('    "UAV": { bg: "#0891b2", text: "#fff" },')
    lines.append('    "FTTA": { bg: "#dc2626", text: "#fff" },')
    lines.append('    "CoTTA": { bg: "#ea580c", text: "#fff" },')
    lines.append('    "VLM": { bg: "#7c3aed", text: "#fff" },')
    lines.append('    "Embodied AI": { bg: "#059669", text: "#fff" },')
    lines.append('    "Agents": { bg: "#2563eb", text: "#fff" },')
    lines.append('    "Edge Computing": { bg: "#0891b2", text: "#fff" },')
    lines.append('    "Federated Learning": { bg: "#4f46e5", text: "#fff" },')
    lines.append('    "World Model": { bg: "#d97706", text: "#fff" },')
    lines.append('    "Streaming Video": { bg: "#db2777", text: "#fff" },')
    lines.append('    "default": { bg: "#64748b", text: "#fff" }')
    lines.append('},')
    lines.append('')
    lines.append('// Group 元数据')
    lines.append('groupColors: {')
    lines.append('    "A": { bg: "#dbeafe", text: "#1d4ed8", name: "目标检测强相关" },')
    lines.append('    "B": { bg: "#dcfce7", text: "#15803d", name: "端云协同" },')
    lines.append('    "C": { bg: "#fef3c7", text: "#b45309", name: "其他AI相关" }')
    lines.append('}')
    lines.append('')
    lines.append('// 导出配置（兼容 ES Module 和 script 标签引入）')
    lines.append('if (typeof module !== "undefined" && module.exports) {')
    lines.append('    module.exports = PAPER_ARCHIVE_CONFIG;')
    lines.append('}')
    
    return '\n'.join(lines)

def main():
    config_path = 'config.js'
    
    if not os.path.exists(config_path):
        print(f"ERROR: {config_path} not found")
        sys.exit(1)
    
    print(f"Reading {config_path}...")
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Extracting meta...")
    meta = extract_meta(content)
    print(f"  Meta: {json.dumps(meta, ensure_ascii=False)}")
    
    print("Extracting daily report entries...")
    entries = parse_daily_report_entries(content)
    print(f"  Found {len(entries)} entries")
    
    if not entries:
        print("ERROR: No entries found!")
        sys.exit(1)
    
    # 按日期倒序排列
    entries.sort(key=lambda e: e.get('id', ''), reverse=True)
    
    print("Regenerating config.js...")
    output = generate_config_js(meta, entries)
    
    # 备份原文件
    backup_path = config_path + '.bak'
    with open(config_path, 'r', encoding='utf-8') as f:
        original = f.read()
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(original)
    print(f"  Backup saved to {backup_path}")
    
    # 写入新文件
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"  config.js has been regenerated!")
    
    # 验证新文件
    print("Validating new config.js with Node.js...")
    ret = os.system(f'NODE_OPTIONS= "C:/Users/miclo/.workbuddy/binaries/node/versions/22.12.0/node.exe" --check {config_path} 2>&1')
    if ret == 0:
        print("  VALID! config.js is valid JavaScript")
    else:
        print(f"  WARNING: Node.js validation returned {ret}")
        print("  You may need to manually fix the file")

if __name__ == '__main__':
    main()
