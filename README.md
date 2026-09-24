# Lhanman 的知识库

和 Claude Code 一起写下的方案、手册和调研，以及从个人知识库同步来的笔记，自动发布在 https://lhanman.github.io/ 。

## 目录结构

- `文档/<项目>/<标题>.html`：每篇文档，按项目分目录，文件名就是标题；不属于任何项目的放在 `文档/其他/`。
- `知识库/<目录>/<笔记>.html`：从知识库同步来的笔记，目录结构和知识库一致。
- `index.html`：网站首页，可以搜索、按标签和类别筛选。
- `知识图谱.html`：知识图谱页，线上在 `graph/`。
- `catalog.json`、`kb.json`：文档和笔记的清单数据。
- `.github/`：部署流程。上线时按清单把页面复制到英文网址 `p/<slug>/`、`kb/<slug>/`，线上不出现中文路径。

这些文件全部由 `dispatch-pages` 自动生成，不要手动修改；笔记的正文请在知识库里改，下一次同步会覆盖这里的副本。

## 文档清单（6 篇）

### ashare-quant

- [青霉素出海股速览](%E6%96%87%E6%A1%A3/ashare-quant/%E9%9D%92%E9%9C%89%E7%B4%A0%E5%87%BA%E6%B5%B7%E8%82%A1%E9%80%9F%E8%A7%88.html) · [线上](https://lhanman.github.io/p/penicillin-export-stocks/) · 2026-09-25 — A股青霉素出海公司：最近一周、日本梅毒事件复盘、买卖点、近一月A股主线与医药走势

### claude-dispatch

- [dispatch 分级调度手册](%E6%96%87%E6%A1%A3/claude-dispatch/dispatch%20%E5%88%86%E7%BA%A7%E8%B0%83%E5%BA%A6%E6%89%8B%E5%86%8C.html) · [线上](https://lhanman.github.io/p/dispatch-manual/) · 2026-09-22 — dispatch 插件手册：分层方案、七条核心原理、运行过程、五个级别、审查环节、模型与消耗、知识库、文档站、脑暴和上手步骤
- [分级调度方案](%E6%96%87%E6%A1%A3/claude-dispatch/%E5%88%86%E7%BA%A7%E8%B0%83%E5%BA%A6%E6%96%B9%E6%A1%88.html) · [线上](https://lhanman.github.io/p/dispatch-design/) · 2026-09-22 — dispatch 的设计决策记录：L0–L4 定级、路由规则、子 agent 编制、审查触发的修订、成本对比，以及业界方案调研与取舍
- [grill-me 与 OpenSpec 手册](%E6%96%87%E6%A1%A3/claude-dispatch/grill-me%20%E4%B8%8E%20OpenSpec%20%E6%89%8B%E5%86%8C.html) · [线上](https://lhanman.github.io/p/grill-openspec/) · 2026-09-19 — grill-me 需求拷问与 OpenSpec 规格驱动开发的使用手册：安装位置、命令、流程和两者的配合
- [dispatch 接入指南](%E6%96%87%E6%A1%A3/claude-dispatch/dispatch%20%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97.html) · [线上](https://lhanman.github.io/p/dispatch-setup/) · 2026-09-19 — dispatch 接入指南：在另一台电脑或给其他人装插件，接上知识库和文档站，在项目里启用、检查和更新

### 其他

- [小说 AI 改编评估](%E6%96%87%E6%A1%A3/%E5%85%B6%E4%BB%96/%E5%B0%8F%E8%AF%B4%20AI%20%E6%94%B9%E7%BC%96%E8%AF%84%E4%BC%B0.html) · [线上](https://lhanman.github.io/p/novel-ai-adaptation/) · 2026-09-19 — 输入书名，产出章节高光与概述、章节漫画、多角色有声剧：国内与海外模型方案的成本对比、可行性、实现方案与风险

## 知识库笔记（15 篇）

### ashare-quant

- [A股中短线策略研究的教训](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/ashare-quant/A%E8%82%A1%E4%B8%AD%E7%9F%AD%E7%BA%BF%E7%AD%96%E7%95%A5%E7%A0%94%E7%A9%B6%E7%9A%84%E6%95%99%E8%AE%AD.html) · [线上](https://lhanman.github.io/kb/ashare-strategy-lessons/) · 2026-09-25 — A股追当天大涨的买点负期望、高开大概率低走；大盘过滤加破位清仓唯一普遍有效；好成绩先查集中度，样本外只考一次
- [自研A股日线回测引擎的几个关键口径](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/ashare-quant/%E8%87%AA%E7%A0%94A%E8%82%A1%E6%97%A5%E7%BA%BF%E5%9B%9E%E6%B5%8B%E5%BC%95%E6%93%8E%E7%9A%84%E5%87%A0%E4%B8%AA%E5%85%B3%E9%94%AE%E5%8F%A3%E5%BE%84.html) · [线上](https://lhanman.github.io/kb/note-f6c1c4/) · 2026-09-23 — A股日线回测：持仓存真实价、除权日按复权因子折股数；先卖后买、开盘涨停作废；账平不代表引擎对
- [A股免费数据源实测与数据层决策](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/ashare-quant/A%E8%82%A1%E5%85%8D%E8%B4%B9%E6%95%B0%E6%8D%AE%E6%BA%90%E5%AE%9E%E6%B5%8B%E4%B8%8E%E6%95%B0%E6%8D%AE%E5%B1%82%E5%86%B3%E7%AD%96.html) · [线上](https://lhanman.github.io/kb/note-a087d7/) · 2026-09-23 — A股日线免费源实测：东财封IP弃用，Baostock主新浪备，北交所靠新浪，涨跌停自算，复权以as_of为基准
- [A股回测引擎体检方法与查出的缺陷](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/ashare-quant/A%E8%82%A1%E5%9B%9E%E6%B5%8B%E5%BC%95%E6%93%8E%E4%BD%93%E6%A3%80%E6%96%B9%E6%B3%95%E4%B8%8E%E6%9F%A5%E5%87%BA%E7%9A%84%E7%BC%BA%E9%99%B7.html) · [线上](https://lhanman.github.io/kb/note-32c264/) · 2026-09-23 — 回测体检五法（独立记账、截断对照、已知答案、逐笔核对、成本敏感性）查出除权、强平、半分钱、零股四处缺陷

### claude-dispatch

- [dispatch 分级调度使用速查](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/claude-dispatch/dispatch%20%E5%88%86%E7%BA%A7%E8%B0%83%E5%BA%A6%E4%BD%BF%E7%94%A8%E9%80%9F%E6%9F%A5.html) · [线上](https://lhanman.github.io/kb/dispatch/) · 2026-09-22 — dispatch 插件日常用法：L0–L4 自动定级、#L 手动定级、setup 接入、脑暴、审查环节、知识库检索与沉淀、HTML 发布到文档站

### 博客

- [Personal Blog 项目概览](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/00%20-%20%E9%A1%B9%E7%9B%AE%E6%A6%82%E8%A7%88.html) · [线上](https://lhanman.github.io/kb/personal-blog/) · 2026-09-23 — 基于 Kotlin Multiplatform (KMP) + Compose Multiplatform 构建的全栈跨平台个人博客系统。
- [故障排除](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/08%20-%20%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html) · [线上](https://lhanman.github.io/kb/note-a8f9f9/) · 2026-09-23 — 确认后端运行： ./status.sh
- [使用手册](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/05%20-%20%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C.html) · [线上](https://lhanman.github.io/kb/note-909ace/) · 2026-09-23 — Android 应用：在模拟器或真机上打开
- [API 文档](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/04%20-%20API%20%E6%96%87%E6%A1%A3.html) · [线上](https://lhanman.github.io/kb/note-70c8b2/) · 2026-09-23 — Base URL（开发）： http://localhost:8080/api/v1
- [后端架构](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/01%20-%20%E5%90%8E%E7%AB%AF%E6%9E%B6%E6%9E%84.html) · [线上](https://lhanman.github.io/kb/note-2ecc84/) · 2026-09-22 — Kotlin + Ktor Server — RESTful API
- [前端架构](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/02%20-%20%E5%89%8D%E7%AB%AF%E6%9E%B6%E6%9E%84.html) · [线上](https://lhanman.github.io/kb/note-205fd1/) · 2026-09-22 — Kotlin Multiplatform — 跨平台代码共享
- [开发指南](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/06%20-%20%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97.html) · [线上](https://lhanman.github.io/kb/note-cbd676/) · 2026-03-29 — 项目包含三个 Gradle 子项目：
- [数据库设计](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/03%20-%20%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E8%AE%A1.html) · [线上](https://lhanman.github.io/kb/note-26818f/) · 2026-03-29 — 使用 Flyway 管理，迁移文件位于 backend/src/main/resources/db/migration/
- [部署指南](%E7%9F%A5%E8%AF%86%E5%BA%93/%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE/%E5%8D%9A%E5%AE%A2/07%20-%20%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97.html) · [线上](https://lhanman.github.io/kb/note-08a4b6/) · 2026-03-29 — 前端： http://localhost

### 技术笔记

- [Markdown 语法总结](%E7%9F%A5%E8%AF%86%E5%BA%93/%E6%8A%80%E6%9C%AF%E7%AC%94%E8%AE%B0/Markdown%20%E8%AF%AD%E6%B3%95%E6%80%BB%E7%BB%93.html) · [线上](https://lhanman.github.io/kb/markdown/) · 2026-03-31 — 日期：2026-03-20 标签：#技术笔记 #Markdown
