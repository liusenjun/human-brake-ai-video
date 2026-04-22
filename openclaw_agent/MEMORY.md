# MEMORY.md — Long-term Memory

> AI agent's curated long-term memory for the Human Brake Plan project.
> Updated 2026-04-23.

---

## About Louis

- **Name**: Louis
- **GitHub**: liusenjun
- **Discord**: louis_hls
- **Timezone**: Asia/Shanghai (GMT+8)

### Louis's Preferences

- Likes concise, direct communication — no fluff
- Uses Chinese voice input, structured and clear
- Discord is the primary communication channel
- Prefers clean structure over complexity

---

## The Project: Human Brake Plan (人类刹车计划)

- **Repo**: https://github.com/liusenjun/human-brake-ai-video
- **Original screenplay**: 陈秋芳 (Chen Qiufan)
- **Format**: ~1 minute AI short film
- **Genre**: Hong Kong noir

### Story Structure & Team

| Act | Content | Contributor |
|-----|---------|-------------|
| Act 1 | Opening dialogue scene | Louis |
| Act 2-3 | Hong Kong chase scenes | Huang Yishu (黄奕舒) + Jing Xin (辛怡静) |
| Act 4 | Chase finale | Leo Zhu (朱智立) |

### Character: Robin

The protagonist. Caught in a nighttime U盘handoff in a Sham Shui Po tea restaurant, escalates into a city-wide chase.

---

## Current Project Status (2026-04-21)

### AI Video Generation

| Model | Task | Status |
|-------|------|--------|
| Wan 2.2 | I2V | ✅ Working — all 19 shots generated |
| KLing 3.0 | I2V | ✅ Ready for production (Act 1) |
| FLUX | Storyboard images | ✅ 19 images (shot01–shot19) |
| LTX 2.3 | I2V | ⚠️ Text encoders damaged, needs fix |

### ComfyUI

- Port: 8188
- Source: `C:\Users\user.V915-31\Documents\comfyui-git\`
- Models: `C:\Users\user.V915-31\Documents\ComfyUI\models\`
- Output: `C:\Users\user.V915-31\Documents\ComfyUI\output\`

### Wan 2.2 I2V Node Chain (Correct)
```
UNETLoader → wan2.2_ti2v_5B_fp16.safetensors
VAELoader → wan2.2_vae.safetensors
CLIPLoader → umt5_xxl_fp8_e4m3fn_scaled.safetensors (type="wan")
Wan22ImageToVideoLatent → VAEDecode → CreateVideo → SaveVideo
KSampler: steps=25, cfg=1.0, sampler="euler"
ModelSamplingSD3: shift=1.0
```

---

## Repo Structure (current as of 2026-04-23)

```
human-brake-ai-video/
├── louis/           ← Act 1 (Louis): script, storyboard, prompts, workflows
├── huangyishu/     ← Act 2-3 (黄奕舒)
├── jing/            ← Act 2-3 (辛怡静)
├── leozhu/          ← Act 4 (朱智立)
├── script/          ← Shared: original screenplay (陈秋芳)
├── workflows/       ← Shared: ComfyUI workflows
├── audio/           ← Shared: background music
├── voice/           ← Shared: voice acting
└── videos/          ← Shared: video files (links)
```

---

## Tools & Environment

- **Git**: v2.53.0
- **GitHub CLI (gh)**: v2.88.1, authenticated as liusenjun
- **ffmpeg**: Winget-installed, in Windows package manager
- **yt-dlp**: pip-installed
- **SenseVoice**: Local ASR, CPU-only
- **OpenClaw**: AI agent platform (this system)

### OpenClaw Configuration
- Discord channel has `"healthMonitor": {"enabled": false}` to prevent Gateway crashes
- Double node processes conflict — kill old process before restarting

---

## AI Collaboration Rules

1. **Install any skill**: Must first run skill-vetter security review
2. **GitHub push**: Only when Louis explicitly authorizes
3. **Workspace backup**: Use bot-memory-update skill → pushes to https://github.com/liusenjun/MyClawBot
4. **Large file downloads**: If interrupted >1 hour or multiple failures, switch approach and notify

---

## Technical Notes

### ComfyUI API
- Object info: `http://localhost:8188/object_info/{NodeType}`
- Models list: `http://localhost:8188/api/models/{category}`

### BiliBili Subtitles
When the subtitle API returns 404, use:
```
yt-dlp -f "30280" --audio-format wav -o "output.wav" "URL"
```
Then transcribe with SenseVoice as fallback.

### qBittorrent (Louis's)
- Version 5.1.4 on Windows
- WebUI non-functional (port 8080 never listens)
- fastresume cache corruption causes file size mismatches

---

## venetanji/ltx2-comfy-v915 Reference

Alternative LTX 2.3 workflow approach found in Louis's local repo.

**Key insight**: Uses GGUF quantized models + DualCLIPLoader instead of native safetensors + LTXAVTextEncoderLoader.

**Required files** (in venetanji torrent, 132.85 GB total):
- `ltx-2.3-22b-dev-Q4_K_M.gguf` (13.34 GB) — not yet downloaded
- `gemma_3_12B_it_fp4_mixed.safetensors` (8.80 GB) — not yet downloaded
- `LTX2_video_vae_bf16.safetensors` (2.28 GB) — 69% downloaded

---

_Last updated: 2026-04-23_
