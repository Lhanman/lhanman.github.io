# Lhanman 的文档

和 Claude Code 一起写下的方案、手册和调研，定稿后自动发布在 https://lhanman.github.io/ 。

## 目录结构

- `文档/<项目>/<标题>.html`：每篇文档，按项目分目录，文件名就是标题；不属于任何项目的放在 `文档/其他/`。
- `index.html`：网站目录页，可以搜索、按标签筛选。
- `catalog.json`：文档清单数据。

除文档本身外，这些文件都由 `dispatch-pages` 自动生成，不要手动修改。

## 文档清单（4 篇）

### claude-dispatch

- [grill-me 与 OpenSpec 手册](%E6%96%87%E6%A1%A3/claude-dispatch/grill-me%20%E4%B8%8E%20OpenSpec%20%E6%89%8B%E5%86%8C.html) · 2026-09-19 — grill-me 需求拷问与 OpenSpec 规格驱动开发的使用手册：安装位置、命令、流程和两者的配合
- [dispatch 分级调度手册](%E6%96%87%E6%A1%A3/claude-dispatch/dispatch%20%E5%88%86%E7%BA%A7%E8%B0%83%E5%BA%A6%E6%89%8B%E5%86%8C.html) · 2026-09-19 — dispatch 插件手册：分层方案、七条核心原理、运行过程、五个级别、模型与消耗、知识库、文档站、脑暴和上手步骤
- [分级调度方案](%E6%96%87%E6%A1%A3/claude-dispatch/%E5%88%86%E7%BA%A7%E8%B0%83%E5%BA%A6%E6%96%B9%E6%A1%88.html) · 2026-09-19 — dispatch 的设计决策记录：L0–L4 定级、路由规则、子 agent 编制、成本对比，以及业界方案调研与取舍

### 其他

- [小说 AI 改编评估](%E6%96%87%E6%A1%A3/%E5%85%B6%E4%BB%96/%E5%B0%8F%E8%AF%B4%20AI%20%E6%94%B9%E7%BC%96%E8%AF%84%E4%BC%B0.html) · 2026-09-19 — 输入书名，产出章节高光与概述、章节漫画、多角色有声剧：国内与海外模型方案的成本对比、可行性、实现方案与风险
