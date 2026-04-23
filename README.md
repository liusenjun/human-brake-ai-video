# Human Brake Plan

> AI Short Film Project, Hong Kong Noir, Science Fiction

## About

**Human Brake Plan** is an experimental AI short film, inspired by the screenplay of [Chen Qiufan (陈秋芳)](https://en.wikipedia.org/wiki/Chen_Qiufan).

A late-night USB drive handoff in a Sham Shui Po tea restaurant — interrupted by a single gunshot. Robin seizes the drive and runs, leading police through the dense streets and neon-lit alleys of Hong Kong on a modified motorcycle, until she disappears off the edge of a West Kowloon overpass into the night.

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
| **Louis Huang（黄柳森）** | Contributor | script, storyboard, repo management |
| **Huang Yishu (黄奕舒)** | Contributor | asset generation, storyboard, chase scene visuals |
| **Jing Xin (辛怡静)** | Contributor | chase scene visuals, audio generation |
| **Leo Zhu (朱智立)** | Project Lead | script, chase finale, editing, director's vision |
| **Xiao Zhi (小志)** | AI Agent | Workflow design, prompt engineering, video generation, technical research |

---

## How We Work

**Production Pipeline:**

> Script → Character Reference → Prompt Engineering → Storyboard → AI Reference Images → AI Video → Audio → Editing → Final Output

Prompt engineering is the shared skill that ties every stage together. Each act uses a different set of AI tools to execute this pipeline.

### 各 Act 制作流程

- **Act 1（Louis）** — 剧本 → 分镜图（FLUX）→ 提示词 → KLing 3.0 / Wan 2.2 视频生成
- **Act 2-3（黄奕舒 + 辛怡静）** — 剧本延续 → 分镜 → 参考图（Stable Diffusion v1.5）→ HunyuanVideo 1.5 I2V 视频生成 → Suno 配乐 → 配音剪辑
- **Act 4（朱智立）** — 追逐尾声制作
- **AI 协作（小志）** — 通过 Discord 实时协助，全程记录在 [openclaw_agent/](openclaw_agent/)

> 📸 [图片占位：Discord 协作截图 / 工作流截图]

---

## AI Agent Collaboration

This project uses **OpenClaw** AI Agent **Xiao Zhi (小志)** as a technical collaborator, working alongside the team in real-time through **Discord** voice and text.

Unlike a passive assistant, Xiao Zhi takes initiative — researching models, debugging workflows, and proposing solutions without being asked. The collaboration model is closer to a junior technical partner than a chatbot.

**What Xiao Zhi handles:**
- ComfyUI workflow design and debugging
- Prompt engineering (KLing 3.0, FLUX, Wan 2.2, LTX 2.3)
- Python/PowerShell scripting for batch processing
- Technical research on AI video models and tools
- Repository structure and documentation

**Key technical contributions:**
- Discovered and resolved T2V vs I2V model mismatch causing black output in Wan 2.2
- Designed the correct Wan 2.2 I2V node chain (UNETLoader → VAELoader → Wan22ImageToVideoLatent → VAEDecode → CreateVideo)
- Researched and documented LTX 2.3, venetanji/ltx2-comfy-v915 workflows
- Set up ComfyUI batch processing scripts for multi-shot video generation

All collaboration records are preserved in [openclaw_agent/](openclaw_agent/).

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
└── assets/             ← Shared: character reference sheets
```

> Each team member manages their own folder. Shared resources are at the root level.

---

## Tech Stack

**AI Video Generation**
- KLing 3.0 — image-to-video (main production tool)
- FLUX — storyboard image generation
- Wan 2.2 — local I2V testing (ComfyUI)
- HunyuanVideo 1.5 — local I2V (腾讯混图, ComfyUI)
- LTX 2.3 — local I2V testing (ComfyUI)
- Stable Diffusion v1.5 — reference image generation

**AI Music**
- Suno — background music generation

**Tools**
- ComfyUI — node-based video workflow
- OpenClaw — AI agent collaboration platform
- Discord — real-time team communication
- GitHub — project version control

---

## License

MIT License

---

*Human Brake Plan · 2026*
