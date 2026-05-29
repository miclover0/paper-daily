# Vision Intelligence Daily Archive

📚 每日 AI & 计算机视觉论文精选简报

---

## 📁 目录结构

```
/paper-daily
├── index.html              # 主页面（聚合展示）
├── config.js                # 数据配置文件
├── push.bat                 # 推送脚本（双击运行）
├── README.md                # 说明文档
├── .nojekyll               # GitHub Pages 配置
└── /daily_reports          # 二级页面文件夹
    └── 2026-05-29-CVPR.html
```

---

## ✨ 功能特性

| 特性 | 说明 |
|------|------|
| 单页面架构 | 主页聚合展示所有日报 |
| 纯前端渲染 | 通过 `config.js` 动态生成 |
| 深色/亮色主题 | 一键切换，自动记忆 |
| 毛玻璃卡片 | 现代化 Glassmorphism 设计 |
| 响应式布局 | 桌面/平板/手机完美适配 |
| 平滑动效 | Hover 上浮、渐入动画 |

---

## 🎨 设计风格

- **配色**：深色模式为主，紫蓝渐变强调色
- **字体**：Inter（正文）+ JetBrains Mono（代码/数字）
- **布局**：卡片式 Grid 布局
- **交互**：平滑微动效，点击跳转详情

---

## 📖 config.js 数据结构

```javascript
const PAPER_ARCHIVE_CONFIG = {
    meta: {
        title: "Vision Intelligence Daily Archive",
        totalPapers: 15,
        totalDays: 1,
        lastUpdated: "2026-05-29"
    },
    dailyReports: [
        {
            id: "2026-05-29",
            date: "2026-05-29",
            filename: "daily_reports/2026-05-29-CVPR.html",
            paperCount: 15,
            featuredPapers: [...],
            papers: [...]
        }
    ],
    tagColors: {...},
    groupColors: {...}
};
```

---

## 🚀 使用方法

### 每日更新（双击运行）

```bash
push.bat
```

### 手动推送

```bash
git add .
git commit -m "feat: 更新日报 - YYYY-MM-DD"
git push origin main
```

---

## 🌐 部署地址

**GitHub Pages**: https://miclover0.github.io/paper-daily/

> ⚠️ 如果网络超时，请稍后重试或配置代理

---

## 🔧 技术栈

- HTML5 + CSS3 + Vanilla JavaScript
- Google Fonts (Inter, JetBrains Mono)
- GitHub Pages

---

🤖 由 QClaw 自动生成 · [@miclover0](https://github.com/miclover0)
