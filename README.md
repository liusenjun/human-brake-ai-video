# Human Brake Plan

> AI Short Film Project | Hong Kong Noir | Science Fiction

---

## About

**Human Brake Plan** is an experimental AI short film, inspired by the screenplay of [Chen Qiufan (陈秋芳)](https://en.wikipedia.org/wiki/Chen_Qiufan). The story follows Robin, a character drawn into a night-time U盘handoff in a Sham Shui Po tea restaurant, which escalates into a desperate chase across the streets of Hong Kong.

The film is told across four interconnected acts — each a chapter in Robin's city-wide pursuit, and each produced by a different team member:

**Act 1 · 深水埗暗线 (The Sham Shui Po Connection)** — In a late-night tea restaurant, Robin meets an informant to receive a USB drive containing data about "the brake" — a device that could bring down the city's surveillance grid. Before the exchange completes, a shooter guns down the informant. Robin seizes the U盘 and crashes through the glass into the night.

**Acts 2-3 · 香港追逐 (The Hong Kong Chase)** — A high-speed pursuit unfolds across the city's dense streets: wet-market alleys, the Cross-Harbour Tunnel, a fruit wholesale stall, the bustling Mong Kok temple street market, and a narrow electronics district where Robin deploys an EMP pulse to disable pursuing vehicles. The chase climaxes at a unfinished West Kowloon overpass, where Robin launches her motorcycle into the void above Victoria Harbour.

**Act 4 · 货轮对决 (The Cargo Ship Finale)** — Robin lands on a moving cargo ship in the middle of the harbour. As police lights fade on the distant shore, she turns to face her pursuers with a defiant gesture — the brake is in her hands, and the game has only just begun.

The project is an experiment in collaborative AI filmmaking: each act uses a different combination of AI tools (FLUX, Stable Diffusion, KLing 3.0, HunyuanVideo, Suno), with prompt engineering as the shared skill tying every stage together.

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
| **Louis Huang（黄柳森）** | Project Lead | Act 1: script, storyboard, repo management |
| **Huang Yishu (黄奕舒)** | Contributor | Act 2-3: asset generation, chase scene visuals |
| **Jing Xin (辛怡静)** | Contributor | Act 2-3: chase scene visuals, audio generation |
| **Leo Zhu (朱智立)** | Director | Act 4: chase finale, editing, director's vision |
| **Xiao Zhi (小志)** | AI Agent | Workflow design, prompt engineering, technical research |

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

## AI Collaboration

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
