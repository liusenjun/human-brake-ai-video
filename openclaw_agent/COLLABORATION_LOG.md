# Collaboration Log — Human Brake Plan

> Key technical decisions, problem-solving events, and workflow discoveries.
> Written from the AI agent's perspective, in English.

---

## 2026-04-21 — Wan 2.2 I2V Breakthrough

### Problem Discovered
All 19 shot videos generated so far were essentially black/blank.

**Root Cause**: We were using T2V models (text-to-video) for I2V tasks (image-to-video). T2V models don't understand image input — they only respond to text prompts.

**Discovery**: Wan 2.2 requires a dedicated I2V model (`wan2.2_ti2v_5B_fp16.safetensors`) separate from the T2V model. We only had the T2V model.

### Solution
- Downloaded `wan2.2_vae.safetensors` (1.31 GB) and `wan2.2_ti2v_5B_fp16.safetensors` (9.31 GB) from HuggingFace
- Rebuilt the ComfyUI workflow using the correct node chain:
  ```
  UNETLoader → wan2.2_ti2v_5B_fp16
  VAELoader → wan2.2_vae
  CLIPLoader → umt5_xxl_fp8_e4m3fn_scaled (type="wan")
  Wan22ImageToVideoLatent → VAEDecode → CreateVideo → SaveVideo
  ```
- Batch-submitted all 19 shots
- All 19 videos generated successfully (1-2MB each, valid video content)

### Correct Wan 2.2 I2V Parameters
- KSampler: steps=25, cfg=1.0, sampler="euler", scheduler="normal"
- ModelSamplingSD3: shift=1.0
- CreateVideo: fps=15.0

---

## 2026-04-21 — LTX 2.3 Investigation

### Models Status
All LTX 2.3 model files were corrupted due to interrupted qBittorrent downloads.
- Gemma text encoder: corrupted sparse file
- UMT5 text encoder: meta tensor error on load
- Qwen 3B: wrong tokenizer

### venetanji/ltx2-comfy-v915 Discovery
Found an alternative approach using GGUF quantized models:
- `ltx-2.3-22b-dev-Q4_K_M.gguf` (13.34 GB) — not yet downloaded
- venetanji's approach uses `DualCLIPLoader` (not `LTXAVTextEncoderLoader`)
- venetanji uses a custom VAE from `venetanji/ltx2-video-vae` (not standard LTX2 VAE)

### Louis's Contribution
Louis downloaded `ltx-2.3-22b-dev.safetensors` (46.15 GB) directly from HuggingFace — massive file, major effort.

### LTX 2.3 I2V Bug Found
VAE was not connected to `LTXVImgToVideoConditionOnly` — only to `LTXVTiledVAEDecode`. Fixed by connecting VAE to both nodes simultaneously.

**Result**: Workflow produces output but content is chaotic noise (no diffusion sampling happening without a working text encoder).

---

## 2026-04-21 — qBittorrent WebUI Failure

qBittorrent v5.1.4 on Windows: WebUI completely non-functional.
- Port 8080 never listens
- qBittorrent process exits immediately when launched with torrent file as argument
- Louis can see torrent status in the desktop app but cannot remote-control it

### Workaround Needed
Manual intervention in qBittorrent GUI required, or download from HuggingFace directly.

---

## 2026-04-20 — FLUX Storyboard Images

Generated 19 storyboard images (shot01–shot19) using FLUX via ComfyUI.

**Prompt style**: Hong Kong noir, tea restaurant, U盘handoff scene, warm lighting, cinematic.

Images served as the basis for all subsequent I2V video generation.

---

## 2026-04-20 — ComfyUI Workflow Scripts

Created batch processing scripts for ComfyUI:
- `batch_wan_i2v.py` — submits multiple I2V jobs programmatically
- `folder_list.json` — ComfyUI folder listing
- `test_wan_i2v_workflow.json` — test workflow for Wan 2.2 I2V
- `wan_i2v_jobs.json` — job queue configuration

---

## 2026-04-21 — Repo Restructure

The GitHub repo structure was redesigned to reflect the actual collaboration model:

**Old structure**: Credits-based, with `credits/` wrapper and per-person subfolders.

**New structure**: Flat per-member folders at root level, with shared resources (script/, workflows/, audio/, voice/, videos/) at the top.

**Decision made with Louis**: Each member has their own folder, shared resources are at root. Folders are not force-uniform — each person organizes within their folder as needed.

---

## Key Technical Learnings

1. **T2V ≠ I2V**: These are different model types. Using a T2V model for I2V tasks produces black/blank output.
2. **LTX 2.3 text encoders are fragile**: All three encoders (Gemma, UMT5, Qwen) failed in different ways. venetanji's DualCLIPLoader approach may be more robust.
3. **ComfyUI startup matters**: Using `--quick-test-for-ci` flag crashes the UI. Proper startup via `install_comfy.bat` is required.
4. **VAE connections are critical**: In LTX 2.3, the VAE must connect to both the conditioning node AND the decode node simultaneously.

---

## What's Outstanding (as of 2026-04-21)

- [ ] LTX 2.3 text encoder fix (need working Gemma or UMT5)
- [ ] qBittorrent models torrent completion
- [ ] KLing 3.0 production video generation (Act 1)
- [ ] Acts 2-4 visuals (黄奕舒, 辛怡静, 朱智立)
- [ ] Music and voice acting
- [ ] Final edit

---

*Log maintained by Xiao Zhi (小志) · OpenClaw AI Agent*
