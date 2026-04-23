# Human Brake Plan

> AI Short Film Project | Hong Kong Noir

---

## About

**Human Brake Plan** is an experimental AI short film, inspired by the screenplay of [Chen Qiufan (陈秋芳)](https://en.wikipedia.org/wiki/Chen_Qiufan). The story follows Robin, a character caught in a night-time U盘handoff in a Hong Kong Sham Shui Po tea restaurant, which escalates into a chase across the city.

The project explores the full AI filmmaking pipeline: **script → storyboard → image-to-video → editing**.

---

## 🎬 Final Output

> The final video will be embedded here once complete.

**Link:** [Coming Soon]()

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
| **Louis Huang（黄柳森）** | Project Lead | Act 1: script, storyboard, overall coordination |
| **Huang Yishu (黄奕舒)** | Contributor | Act 2-3: chase scene visuals |
| **Jing Xin (辛怡静)** | Contributor | Act 2-3: chase scene visuals |
| **Leo Zhu (朱智立)** | Contributor | Act 4: chase finale |
| **Xiao Zhi (小志)** | AI Agent | Workflow design, prompt engineering, video generation |

---

## How We Work

### 协作流程

1. **剧本创作** — 由 Louis 负责第一幕的剧本改编和整理
2. **分镜设计** — 根据剧本生成 19 个镜头的分镜图（使用 FLUX）
3. **提示词工程** — 为每个镜头撰写 AI 视频生成提示词（KLing 3.0）
4. **视频生成** — 通过 KLing 3.0 生成各镜头视频（本地 ComfyUI 工作流测试）
5. **剪辑合成** — 合成最终成片

> 📸 [图片占位：工作流程示意图]

### 各 Act 制作流程

- **Act 1（Louis）** — 剧本 → 分镜图 → 提示词 → KLing 视频生成
- **Act 2-3（黄奕舒 + 辛怡静）** — 追逐场景视觉制作
- **Act 4（朱智立）** — 追逐尾声制作
- **AI 协作（小志）** — 通过 Discord 实时协助，全程记录在 [openclaw_agent/](openclaw_agent/)

> 📸 [图片占位：Discord 协作截图 / 工作流截图]

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
└── voice/              ← Shared: voice acting
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

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed step-by-step instructions (in Chinese).

---

## License

MIT License

---

*Human Brake Plan · 2026*
