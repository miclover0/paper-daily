#!/usr/bin/env python3
"""
fix_config_v3.py - 把破损的 config.js 转成合法 JS
方法: 
1. 去掉注释
2. 给无引号 key 加引号 → 合法 JSON
3. 去掉 trailing commas
4. 解析 JSON
5. 重新序列化为合法 JS（所有 key 无引号）
"""
import re, json, sys

def unquote_js_keys(content):
    """把 JSON 格式（"key": value）转回 JS 对象格式（key: value）"""
    # 只处理对象 key（字符串后跟 :）
    # 简单方法：用 json.dumps 输出，然后替换 "key": 为 key:
    # 但 json 输出可能把 key 放在任意位置
    
    # 更好的方法：直接用 json.dumps 输出缩进格式，然后处理
    # 实际上最简单：输出为 JSON，然后 index.html 中改用 fetch + JSON.parse
    # 但这需要改 index.html...
    
    # 最靠谱：直接输出 JS 对象字面量
    return content

def main():
    input_file = 'config.js'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Step 1: 去掉注释
    # 简单方法：逐行处理，保留非注释部分
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        # 跳过注释行
        if stripped.startswith('//'):
            cleaned_lines.append('')  # 保留空行（不改变行号）
            continue
        # 去掉行尾注释（但要小心里面有 http:// 等）
        # 简单方法：忽略
        cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines)
    
    # Step 2: 去掉多行注释
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Step 3: 去掉 trailing commas (在 } 或 ] 之前的逗号)
    content = re.sub(r',(\s*[}\]])', r'\1', content)
    
    # Step 4: 给无引号的 key 加引号（转 JSON）
    # 策略：匹配行首空白后跟 identifier: 的模式
    # 但只在对象上下文内部处理
    
    # 更可靠的方法：直接用 regex 匹配
    # 匹配: 在 { 或 , 之后的行首空白 + 标识符 + : 
    # (?:^|[{,])\s*(\w[\w$]*)\s*:
    
    # We'll be aggressive and quote ALL identifier: patterns
    # But avoid string values like "something:"
    
    # Actually, a simpler approach: just convert the entire object value
    # by finding const PAPER_ARCHIVE_CONFIG = { and extracting the object
    
    # Find the object literal
    match = re.search(r'const\s+PAPER_ARCHIVE_CONFIG\s*=\s*', content)
    if not match:
        print("ERROR: Cannot find PAPER_ARCHIVE_CONFIG")
        sys.exit(1)
    
    obj_start = content.index('{', match.end())
    
    # Find matching }
    depth = 0
    i = obj_start
    while i < len(content):
        c = content[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                obj_end = i
                break
        i += 1
    else:
        print("ERROR: Unclosed object")
        sys.exit(1)
    
    obj_str = content[obj_start:obj_end+1]
    
    # Now convert obj_str (JS object literal) to valid JSON
    # Strategy: use regex to quote ALL unquoted keys
    
    # Common keys in our data:
    keys = [
        'meta', 'title', 'subtitle', 'description', 'totalPapers', 'totalDays',
        'lastUpdated', 'author', 'repository', 'dailyReports',
        'id', 'date', 'dateDisplay', 'weekday', 'filename', 'paperCount',
        'groups', 'featuredPapers', 'papers', 'group', 'groupName',
        'authors', 'venue', 'arxivId', 'tags', 'summary', 'highlights',
        'pdfUrl', 'worthReading', 'bg', 'text', 'name',
        'score', 'reportFile', 'totalPapers', 'A', 'B', 'C'
    ]
    
    # Convert JS to JSON by quoting all known keys
    for key in keys:
        # Match key followed by : (not inside strings)
        # Pattern: (not alphanumeric before) + key + optional spaces + :
        obj_str = re.sub(
            r'(?<![\\w"])' + re.escape(key) + r'\\s*:',
            '"' + key + '":',
            obj_str
        )
    
    # Also handle numeric-like keys (group labels)
    # Already covered above with A, B, C
    
    # Remove trailing commas
    obj_str = re.sub(r',\s*([}\]])', r'\1', obj_str)
    
    # Try parsing as JSON
    try:
        data = json.loads(obj_str)
        print(f"Successfully parsed! {data['meta']['totalDays']} days, {data['meta']['totalPapers']} papers")
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Context: ...{obj_str[max(0,e.pos-50):e.pos+50]}...")
        
        # Try a different approach: use js2py or execjs
        # Or just try to load via Node
        print("Trying Node.js to parse...")
        
        # Write to temp file and use Node to parse
        temp_js = f'const PAPER_ARCHIVE_CONFIG = {obj_str};\nconsole.log(JSON.stringify(PAPER_ARCHIVE_CONFIG));'
        with open('_temp_parse.js', 'w', encoding='utf-8') as f:
            f.write(temp_js)
        
        import subprocess, os
        env = os.environ.copy()
        # Try to run with NODE_OPTIONS cleared
        if 'NODE_OPTIONS' in env:
            del env['NODE_OPTIONS']
        
        result = subprocess.run(
            ['C:/Users/miclo/.workbuddy/binaries/node/versions/22.12.0/node.exe', '_temp_parse.js'],
            capture_output=True, text=True, timeout=30, env=env
        )
        
        if result.returncode == 0:
            data = json.loads(result.stdout.strip())
            print(f"Node.js parsed successfully! {data['meta']['totalDays']} days")
        else:
            print(f"Node.js error: {result.stderr}")
            sys.exit(1)
    
    # Now reconstruct the full config.js
    # Note: we need to preserve tagColors, groupColors etc at the end
    prefix = content[:obj_start]
    suffix = content[obj_end+1:]
    
    # Generate valid JS output (JSON is valid JS, but we'll use unquoted keys for readability)
    # Actually, JSON is valid JS! Let's just output as JSON and wrap in const assignment
    # "key": value  in object literals IS valid JS
    
    # For compatibility, output as proper JS with "key": value format (JSON-style)
    # This is perfectly valid JS
    output = '/**\n * Paper Daily Archive\n */\n\n'
    output += 'const PAPER_ARCHIVE_CONFIG = '
    output += json.dumps(data, indent=4, ensure_ascii=False)
    output += ';\n'
    
    # Add tag colors etc (from the original suffix)
    # The original suffix has tagColors, groupColors, module.exports
    # But they're part of the object (should be inside config)
    
    # Actually, looking at the original, tagColors and groupColors are OUTSIDE
    # the PAPER_ARCHIVE_CONFIG object. So they're separate constants.
    # But the index.html probably only uses PAPER_ARCHIVE_CONFIG...
    
    # Let's keep the suffix as-is (comments, tag/group config, exports)
    output += '\n'
    output += 'const tagColors = {\n'
    output += '    "DAOD": { "bg": "#7c3aed", "text": "#fff" },\n'
    output += '    "UAV": { "bg": "#0891b2", "text": "#fff" },\n'
    output += '    "FTTA": { "bg": "#dc2626", "text": "#fff" },\n'
    output += '    "CoTTA": { "bg": "#ea580c", "text": "#fff" },\n'
    output += '    "VLM": { "bg": "#7c3aed", "text": "#fff" },\n'
    output += '    "Embodied AI": { "bg": "#059669", "text": "#fff" },\n'
    output += '    "Agents": { "bg": "#2563eb", "text": "#fff" },\n'
    output += '    "Edge Computing": { "bg": "#0891b2", "text": "#fff" },\n'
    output += '    "Federated Learning": { "bg": "#4f46e5", "text": "#fff" },\n'
    output += '    "World Model": { "bg": "#d97706", "text": "#fff" },\n'
    output += '    "Streaming Video": { "bg": "#db2777", "text": "#fff" },\n'
    output += '    "default": { "bg": "#64748b", "text": "#fff" }\n'
    output += '};\n\n'
    output += 'const groupColors = {\n'
    output += '    "A": { "bg": "#dbeafe", "text": "#1d4ed8", "name": "目标检测强相关" },\n'
    output += '    "B": { "bg": "#dcfce7", "text": "#15803d", "name": "端云协同" },\n'
    output += '    "C": { "bg": "#fef3c7", "text": "#b45309", "name": "其他AI相关" }\n'
    output += '};\n\n'
    output += 'if (typeof module !== "undefined" && module.exports) {\n'
    output += '    module.exports = PAPER_ARCHIVE_CONFIG;\n'
    output += '}\n'
    
    # 写入
    with open('config.js', 'w', encoding='utf-8') as f:
        f.write(output)
    
    print("✅ config.js has been regenerated as valid JavaScript!")

if __name__ == '__main__':
    main()
