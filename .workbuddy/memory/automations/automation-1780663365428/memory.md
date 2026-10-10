# 自动化执行记录：每日论文自动追踪

## 2026-10-09 (周五) 执行摘要
- **结果**：成功。日报 2026-10-09 已生成并推送至 GitHub Pages。
- **抓取**：ArXiv RSS 4 个分类全部正常（cs.CV=302、cs.LG=472、cs.AI=472、cs.RO=154），共 1090 篇 → 关键词过滤 289 篇。
- **筛选/分组**：相关度阈值 86.0，取前 50 篇强相关 → A组=28、B组=22、C组=0。
- **精读推荐**：20 篇 / 50 篇标记值得精读。
- **产物**：`daily_reports/2026-10-09-arXiv.html`，`config.js`/`config.json` 更新（累计 290 篇 / 6 天）。
- **Git**：commit `35c1452`，push 首次遇 `Connection reset by 20.205.243.166 port 22`（网络问题），重试第 2 次成功（`11f8786..35c1452 main -> main`），SSH 认证正常。
- **备注**：pull 因 memory.md 未暂存改动先 stash 再 pull（Already up to date）再 pop，正常恢复。本次数据完整（4 分类齐全），无需补跑。

## 2026-10-08 (周四) 执行摘要
- **结果**：成功。日报 2026-10-08 已生成并推送至 GitHub Pages。
- **抓取**：ArXiv RSS 4 个分类（cs.CV=262、cs.LG=471[含1次超时重试]、cs.AI=240、cs.RO=89），共 1062 篇 → 关键词过滤 293 篇。
- **筛选/分组**：相关度阈值 81.0，取前 50 篇强相关 → A组=21、B组=29、C组=0。
- **精读推荐**：20 篇 / 50 篇标记值得精读。
- **产物**：`daily_reports/2026-10-08-arXiv.html`，`config.js`/`config.json` 更新（累计 240 篇 / 5 天）。
- **Git**：commit `11f8786`，push 成功（`d5e508c..11f8786 main -> main`），SSH 认证正常。
- **备注**：pull 因网络 `Connection reset by 20.205.243.166 port 22` 失败，按预案跳过；stash/pop 正常恢复本地改动。本次数据完整（4 分类齐全），无需补跑。

## 2026-10-07 (周三) 执行摘要
- **结果**：成功。日报 2026-10-07 已生成并推送至 GitHub Pages。
- **抓取**：ArXiv RSS 4 个分类全部正常（上次 cs.CV/LG/AI 超时，本次网络恢复）：cs.CV=247、cs.LG=480、cs.AI=848、cs.RO=139，共 1714 篇 → 关键词过滤 519 篇。
- **筛选/分组**：相关度阈值 88.0，取前 50 篇强相关 → A组=32、B组=18、C组=0。
- **精读推荐**：20 篇 / 50 篇标记值得精读。
- **产物**：`daily_reports/2026-10-07-arXiv.html`，`config.js`/`config.json` 更新（累计 190 篇 / 4 天）。
- **Git**：commit `d5e508c`，push 首次遇 GitHub 端 `Internal Server Error`（remote rejected，非认证问题），重试 3 次仍失败，等待 60s 后第 4 次成功（`781e293..d5e508c main -> main`），SSH 认证正常。
- **备注**：本次数据完整（4 分类齐全），无需补跑。

## 2026-10-06 (周二) 执行摘要
- **结果**：成功，但**数据不完整**。日报 2026-10-06 已生成并推送至 GitHub Pages。
- **抓取异常**：4 个 RSS feed 中仅 `cs.RO` 成功（267 篇）；`cs.CV`、`cs.LG`、`cs.AI` 均因 `WinError 10060` 连接超时 3 次重试失败（本机网络无法连到 rss.arxiv.org 这三个分类）。
- **过滤/分组**：267 篇 → 关键词过滤 40 篇 → A组=7（产业界/端云结合）、B组=33（Agent/RSI/Agentic RL）、C组=0。阈值 29.0，全部 40 篇入选（远低于昨日 251 篇，因缺 3 个分类）。
- **精读推荐**：20 篇 / 40 篇标记值得精读。
- **产物**：`daily_reports/2026-10-06-arXiv.html`，`config.js`/`config.json` 更新（累计 140 篇 / 3 天）。
- **Git**：commit `781e293`，push 成功（`2d26148..781e293 main -> main`），SSH 认证正常。
- **待办**：网络恢复后建议补跑 cs.CV/LG/AI 三个分类（当前日报缺这三类论文）。本次因自动化环境网络不稳未重试，直接提交现有结果。

## 2026-10-05 (周一) 执行摘要
- **结果**：成功。日报 2026-10-05 已生成并推送至 GitHub Pages。
- **抓取**：ArXiv RSS 4 个分类（cs.CV/LG/AI/RO）共 911 篇 → 关键词过滤后 251 篇。
- **筛选**：相关度评分取前 50 篇（阈值 >= 78.0）。
- **分组**：A组=26（产业界/端云结合）、B组=24（Agent/RSI/Agentic RL）、C组=0。
- **精读推荐（值得精读）**：20 篇。
- **产物**：`daily_reports/2026-10-05-arXiv.html`，`config.js`/`config.json` 更新（累计 100 篇 / 2 天）。
- **Git**：commit `2d26148`，push 成功（`137ec24..2d26148 main -> main`），SSH 认证正常。

## 本次遇到的问题与修复（已写入 scripts/daily_fetch.py）
- **现象**：首次运行挂起 11+ 分钟未完成（被手动 kill）。
- **根因**：① 本机网络到 ArXiv RSS 极慢（~24 KB/s，单 feed 878 KB），原 `timeout=30` 不足以载完；② `generate_bilingual_summary` 逐句调用 MyMemory（50 篇 × ~5 句 ≈ 250+ 次 HTTP），是主要耗时。
- **修复**：
  1. `safe_request` 超时 30→60s，保证慢 feed 能载完。
  2. `generate_bilingual_summary` 改为按论文批量翻译（复用既有 `_mymemory_translate_block`，每批≤5句）。
- **效果**：二次运行总耗时 ~7.5 分钟（翻译阶段约 2 分钟），正常完成。
- **注意**：当前网络下 RSS 抓取本身约 5 分钟，属环境瓶颈；若自动化超时可考虑进一步增大超时或并发抓取。

## 执行前检查记录
- git pull --rebase 因有未暂存文件（旧 .bak 删除、memory.md 改动等）先 stash 再 pull（Already up to date）再 pop，正常恢复。
