# Human Brake Plan / 人类刹车计划

> AI Short Film Project | 1-Minute AI Video | Hong Kong Noir Style

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/liusenjun/human-brake-ai-video)](https://github.com/liusenjun/human-brake-ai-video/stargazers)

---

## 项目概述 / Project Overview

**人类刹车计划** 是一部实验性 AI 短片项目，时长约 1 分钟，风格参考《宝可梦礼宾部》的温暖叙事与香港黑色电影的视觉张力结合。故事发生在一个深夜的香港深水埗茶餐厅，核心角色罗宾在一次 U 盘 交接任务中遭遇突袭，展现出非凡的应变与战斗能力。

本项目探索 AI 在电影制作中的应用边界：**剧本 → 分镜 → 图生视频 → 剪辑** 全流程的 AI 协作工作流。

---

## 团队成员 / Team

| 成员 | 角色 | 简介 |
|------|------|------|
| **Louis** | 项目主导 / Project Lead | 负责剧本创作、分镜设计、整体统筹 |
| **小志** | AI 技术搭档 / AI Agent | OpenClaw AI Agent，通过自然语言协作完成工作流设计、提示词工程、视频生成 |
| **[队友信息待补充]** | [待补充] | [待补充] |

---

## AI 协作方式 / AI Collaboration

本项目使用 **[OpenClaw](https://github.com/openclaw/openclaw)** 平台构建的 AI Agent **小志** 作为技术搭档。

### 什么是 OpenClaw AI Agent？

OpenClaw 是一个 AI Agent 运行时平台，支持通过自然语言与 AI 协作完成复杂任务。在本项目中，AI Agent（小志）扮演了以下角色：

- **工作流设计**：设计 ComfyUI 视频生成节点链
- **提示词工程师**：为 KLing 3.0、FLUX 等模型撰写结构化提示词
- **自动化脚本工程师**：编写 Python/PowerShell 脚本批量处理视频生成任务
- **技术调研员**：分析模型文件、调试报错、研究 LTX 2.3 等新模型的技术细节

### 协作模式

所有协作通过 **Discord** 实时完成：

1. Louis 描述需求和创意方向
2. 小志 分析技术可行性并给出方案
3. 小志 编写脚本、执行工作流、生成结果
4. Louis 审核输出并反馈调整意见

这种模式让人从重复性技术工作中解放出来，专注于创意决策。

---

## 目录结构 / Repository Structure

```
human-brake-ai-video/
├── script/                    ← 剧本
│   ├── screenplay_v3.0.docx    ← 完整剧本（含分镜表）
│   └── kling_guide_v3.0.pdf ← KLing 3.0 使用指南
├── storyboard/                ← 分镜资料
│   └── images/               ← 19 张分镜图（FLUX 生成）
│       ├── shot01.png ~ shot19.png
│       └── ...
├── prompts/                  ← 提示词工程
│   └── kling_prompts_bearbug_act1.docx  ← KLing 3.0 视频生成提示词文档
├── workflows/                ← 技术工作流
│   └── *.json                ← ComfyUI Workflow JSON 文件
├── videos/                   ← 视频成品（仅链接，不上传大文件）
│   └── README.md             ← 视频存放说明
├── credits/                  ← 贡献者目录
│   └── README.md             ← 贡献说明
├── CONTRIBUTING.md            ← 队友贡献指南
└── README.md
```

---

## 技术栈 / Tech Stack

### AI 视频生成

| 模型 | 用途 | 说明 |
|------|------|------|
| **KLing 3.0** | 图生视频 | 快手可灵，主体一致性增强，15 秒生成 |
| **FLUX** | 图像生成 | 分镜图生成，高饱和、电影感 |
| **Wan 2.2** | 图生视频 | ComfyUI，本地 I2V 测试 |
| **LTX 2.3** | 图生视频 | ComfyUI，Lightricks 开源模型 |

### 工作流工具

| 工具 | 用途 |
|------|------|
| **ComfyUI** | 本地 AI 视频生成节点工作流 |
| **OpenClaw** | AI Agent 协作平台 |
| **Discord** | 实时协作通讯 |
| **GitHub** | 协作文档与版本管理 |

---

## 当前进展 / Current Progress

- ✅ 剧本 3.0 完成（第一幕，深水埗暗线）
- ✅ 19 张分镜图生成（FLUX）
- ✅ 19 个镜头的 KLing 3.0 提示词文档
- ✅ Wan 2.2 I2V 本地测试视频生成
- 🔄 KLing 3.0 视频片段生成中
- ⏳ LTX 2.3 工作流优化中

---

## 如何参与 / How to Contribute

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细的操作步骤。无论你是负责角色设计、配乐、音效还是其他工作，都可以在本 repo 中找到属于你的贡献位置。

---

## 许可证 / License

MIT License - 欢迎自由使用，但请注明出处。

---

*人类刹车计划 · Human Brake Plan · 2026*
