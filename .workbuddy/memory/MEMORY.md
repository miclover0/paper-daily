# Paper Daily 项目记忆

## 关键问题和修复
- config.js 长期存在 JS 语法错误（字符串模板拼接导致括号不匹配）
- 根因：`daily_fetch.py` 用字符串模板拼接 JS 对象字面量，极易出错
- **修复方案**：改用 `json.dumps()` 生成 `const PAPER_ARCHIVE_CONFIG = <JSON>;` 格式
- 同时写入 `config.json`（纯 JSON 备份）和 `config.js`（供 index.html <script> 加载）
- index.html 无需改加载方式，`<script src="config.js">` 对 `const ... = <JSON>;` 完全合法

## 文件结构
- `config.js`：由 `daily_fetch.py` 自动生成，格式为 `const PAPER_ARCHIVE_CONFIG = {...};`
- `config.json`：纯 JSON 备份，与 config.js 内容相同
- `daily_reports/YYYY-MM-DD-arXiv.html`：每日日报 HTML
- `scripts/daily_fetch.py`：主脚本，生成日报 + 更新 config

## 自动化
- 自动化任务 ID：automation-1780663365428
- 每天自动运行 daily_fetch.py → git push → GitHub Pages 更新
