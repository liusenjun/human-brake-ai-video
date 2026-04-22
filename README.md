# Human Brake Plan

> AI Short Film Project | 1-Minute AI Video | Hong Kong Noir

---

## About

**Human Brake Plan** is an experimental AI short film (~1 minute), inspired by the screenplay of [Chen Qiufan (陈秋芳)](https://en.wikipedia.org/wiki/Chen_Qiufan). The story follows Robin, a character caught in a night-timeU盘handoff in a Hong Kong Sham Shui Po tea restaurant, which escalates into a chase across the city.

The project explores the full AI filmmaking pipeline: **script → storyboard → image-to-video → editing**.

---

## Story Structure

The original screenplay is divided into four acts:

| Act | Content | Contributor |
|-----|---------|-------------|
| Act 1 | Opening dialogue scene | **Louis** |
| Act 2-3 | Hong Kong chase scenes | **Huang Yishu** + **Jing Xin** |
| Act 4 | Chase finale | **Leo Zhu** |

---

## Team

| Name | Role | Contribution |
|------|------|-------------|
| **Louis** | Project Lead | Act 1: script, storyboard, overall coordination |
| **Huang Yishu (黄奕舒)** | Contributor | Act 2-3: chase scene visuals |
| **Jing Xin (辛怡静)** | Contributor | Act 2-3: chase scene visuals |
| **Leo Zhu (朱智立)** | Contributor | Act 4: chase finale |
| **Xiao Zhi (小志)** | AI Agent | Workflow design, prompt engineering, video generation |

---

## AI Collaboration

This project uses **OpenClaw** AI Agent **Xiao Zhi (小志)** as a technical collaborator. All collaboration happens through **Discord**.

Xiao Zhi handles:
- ComfyUI workflow design
- Prompt engineering (KLing 3.0, FLUX, Wan 2.2, LTX 2.3)
- Python/PowerShell scripting for batch video generation
- Technical research on AI video models

---

## Repository Structure

```
human-brake-ai-video/
├── louis/              ← Act 1 (Louis)
│   ├── script/         ← Act 1 scripts
│   ├── storyboard/     ← Act 1 storyboard images
│   ├── prompts/        ← Act 1 video prompts
│   └── workflows/      ← Act 1 workflows
│
├── huangyishu/        ← Act 2-3 (黄奕舒)
├── jing/               ← Act 2-3 (辛怡静)
├── leozhu/             ← Act 4 (朱智立)
│
├── script/             ← Shared: original screenplay (陈秋芳)
├── workflows/          ← Shared: ComfyUI workflows
├── audio/              ← Shared: background music
├── voice/              ← Shared: voice acting
└── videos/            ← Shared: video files (links only)
```

> Each team member manages their own folder. Shared resources are at the root level.

---

## Tech Stack

**AI Video Generation**
- KLing 3.0 — image-to-video (main production tool)
- FLUX — storyboard image generation
- Wan 2.2 — local I2V testing (ComfyUI)
- LTX 2.3 — local I2V testing (ComfyUI)

**Tools**
- ComfyUI — node-based video workflow
- OpenClaw — AI agent collaboration platform
- Discord — real-time team communication
- GitHub — project version control

---

## Current Progress

- [x] Script (陈秋芳 original + Act 1 breakdown)
- [x] 19 storyboard images (FLUX, Act 1)
- [x] KLing 3.0 prompt document (Act 1)
- [x] Wan 2.2 I2V test videos
- [ ] KLing 3.0 Act 1 video generation
- [ ] Act 2-4 visuals
- [ ] Music & voice acting
- [ ] Final edit

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed step-by-step instructions (in Chinese).

---

## License

MIT License

---

*Human Brake Plan · 2026*
