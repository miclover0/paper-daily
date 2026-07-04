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
- `scripts/catchup_fetch.py`：补录脚本，用于批量补齐历史日期的日报

## 补录脚本 (catchup_fetch.py)
- 用途：当自动化任务中断多天后，批量补齐历史日期的论文日报
- 用法：`python scripts/catchup_fetch.py --start=YYYY-MM-DD --end=YYYY-MM-DD`
- **关键经验**：ArXiv API 的 `submittedDate:[FROM TO]` 日期范围查询不可靠（返回0匹配）
- **正确策略**：批量获取所有论文按 submittedDate 降序 → 本地按 published 日期分组 → 逐日处理
- 2026-07-04 首次使用：补录 6/16-7/4 共19天，830篇论文，7843篇原始获取

## 自动化
- 自动化任务 ID：automation-1780663365428
- 每天自动运行 daily_fetch.py → git push → GitHub Pages 更新
- **Git 推送认证**：已改为 SSH（`git@github.com:miclover0/paper-daily.git`）
  - SSH key：`~/.ssh/id_ed25519`（ed25519，miclo-paper-daily-auto）
  - SSH config 中设置了 `ProxyCommand none` 绕过 127.0.0.1:7897 代理
  - **公钥必须添加到 GitHub** → Settings → SSH and GPG keys（否则仍会失败）
