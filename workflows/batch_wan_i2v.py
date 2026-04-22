import sys, requests, json, time
sys.path.insert(0, r"C:\Users\user.V915-31\.openclaw\workspace\skills\comfyui\scripts")
from core import WorkflowGraph, upload_image

COMFY_URL = "http://localhost:8188"
SHOTS = [
    {"shot": 1, "prompt": "The camera gazes across a Sham Shui Po back alley at night, neon signs in crimson and electric blue light glowing on stone brick walls. Narrow street alley, dry ground, atmospheric Hong Kong night scene, cinematic, 8K", "duration": 5},
    {"shot": 2, "prompt": "A middle-aged Hong Kong woman in a crisp uniform stands at the Teahouse entrance, gesturing brightly, sincere warm smile, greeting guests under warm amber light. Background shows the warm interior of the Teahouse. Cinematic, 8K", "duration": 5},
    {"shot": 3, "prompt": "An old ceiling fan rotates slowly in lazy circles, its blades catching warm tungsten light, casting dappled shadows in the crowded Teahouse interior. Stable shot, cinematic, 8K", "duration": 5},
    {"shot": 4, "prompt": "Robin moves through the cramped Teahouse with predatory precision, each footfall deliberate, weight shifting fluidly. Silver streaked short hair, black leather jacket. Her figure looms in warm amber light, creating a sense of oppression. Cinematic, fluid motion, 8K", "duration": 8},
    {"shot": 5, "prompt": "Foreground elements: a plate of dry-fried beef Hor Fun sending up a thin curl of steam, a glass of iced milk tea with condensation. Robin''s figure enters frame from the left, moving with agility. Cinematic, 8K", "duration": 8},
    {"shot": 6, "prompt": "Over-the-shoulder from directly behind Robin''s right shoulder as she settles into a seat across from Uncle Fat. Table has iced milk tea and pineapple bun. Warm yellow high-saturation lighting, cinematic, 8K", "duration": 7},
    {"shot": 7, "prompt": "A top-down extreme close-up: Uncle Fat''s weathered hand, thick fingers, a chunky silver ring on the ring finger, picking up the iced milk tea. Movement slow and steady, cinematic, 8K", "duration": 6},
    {"shot": 8, "prompt": "A reverse-angle bottom-up reveal: Robin''s hand descends into frame and presses flat over the USB drive on the table. Fingers long and strong, black leather jacket cuff visible. Cinematic, 8K", "duration": 5},
    {"shot": 9, "prompt": "A wide static shot from inside the Teahouse, customers continue to eat noodles, drink tea, converse. External dialogue muffled by water filtration. Low-frequency ambient chaos, tense atmosphere, 8K", "duration": 5},
    {"shot": 10, "prompt": "An extreme close-up of the wet plate glass window. Outside: the blue-black of a Sham Shui Po wet night, neon signs reflected on the glass. Cinematic, 8K", "duration": 4},
    {"shot": 11, "prompt": "Ultra slow-motion: a bullet traces a path through the air inside the Teahouse toward Uncle Fat''s wet temple. Bullet trajectory crystal clear, warm amber Teahouse lights in background. Cinematic, 8K", "duration": 3},
    {"shot": 12, "prompt": "Side medium shot: Uncle Fat''s head snaps to the wet from the impact, not a dramatic fall but a simple forward collapse onto the table. Blood spatters on the wall. Cold blue dominant, cinematic, violent aesthetic, 8K", "duration": 3},
    {"shot": 13, "prompt": "Extreme close-up of Robin''s eyes: pupils dilating, the whites of her eyes catching the warm light, subtle expression shifts. Internal turmoil, external calm. Cinematic, 8K", "duration": 5},
    {"shot": 14, "prompt": "Extreme close-up: Robin''s hand darts forward and snatches the USB drive from the table with surgical precision. Clean and efficient movement. Cinematic, 8K", "duration": 3},
    {"shot": 15, "prompt": "Robin surges up from her seat, the movement explosive but controlled, her body coiling and releasing, black leather jacket catching the light. Cinematic, 8K", "duration": 5},
    {"shot": 16, "prompt": "Exterior low angle: Robin tumbles through the shattered window frame onto the wet street outside, glass fragments scattered around, surrounded by a mix of deep blue and warm yellow light. Cinematic, 8K", "duration": 4},
    {"shot": 17, "prompt": "Side close-up: Robin swings onto a modified motorcycle, the kind favored by Hong Kong street riders. Black leather jacket gleaming in the night, silver streaked hair wet. Cinematic, 8K", "duration": 5},
    {"shot": 18, "prompt": "Extreme close-up of Robin''s wet hand twisting the motorcycle throttle grip, knuckles white with maximum force. Background neon lights blur past. Cinematic, 8K", "duration": 4},
    {"shot": 19, "prompt": "Tracking shot: Robin''s motorcycle tears through the wet Sham Shui Po night, a black bolt of motion through crimson and electric blue neon, puddles reflecting shattered light. Cinematic, 8K", "duration": 10},
]
NEGATIVE = "blurry, low quality, watermark, distorted, still frame, static, flickering"
VAE = "wan_2.1_vae.safetensors"
CLIP = "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
BASE_IMAGE = r"C:\Users\user.V915-31\Documents\ComfyUI\input\robin_flux_20260420"
FPS = 15

def submit_wf(workflow):
    r = requests.post(COMFY_URL + "/prompt", json={"prompt": workflow}, timeout=30)
    if r.status_code != 200:
        print("Failed: " + str(r.status_code))
        return None
    return r.json().get("prompt_id")

def build_wf(prompt, shot_num, image_filename, length_frames=19):
    g = WorkflowGraph()
    clip = g.node("CLIPLoader", clip_name=CLIP, type="wan", device="default")
    vae = g.node("VAELoader", vae_name=VAE)
    cond_pos = g.node("CLIPTextEncode", text=prompt, clip=clip)
    cond_neg = g.node("CLIPTextEncode", text=NEGATIVE, clip=clip)
    img_node = g.node("LoadImage", image=image_filename)
    wan_out = g.node("WanFirstLastFrameToVideo", positive=cond_pos, negative=cond_neg, vae=vae, width=1280, height=720, length=length_frames, batch_size=1, start_image=img_node[0])
    decoded = g.node("VAEDecode", samples=wan_out[2], vae=vae)
    video = g.node("CreateVideo", images=decoded, fps=FPS)
    g.node("SaveVideo", video=video[0], filename_prefix="shot" + str(shot_num).zfill(2) + "_wan", format="auto", codec="auto")
    return g.to_dict()

print("Uploading images...")
image_map = {}
for shot in SHOTS:
    snum = shot["shot"]
    img_path = BASE_IMAGE + "\\shot" + str(snum).zfill(2) + ".png"
    try:
        server_img = upload_image(img_path)
        image_map[snum] = server_img
        print("  Shot " + str(snum) + ": " + server_img)
    except Exception as e:
        print("  Shot " + str(snum) + ": UPLOAD FAILED - " + str(e))
        image_map[snum] = None

print("\nSubmitting " + str(len(SHOTS)) + " shots...")
job_ids = {}
for shot in SHOTS:
    snum = shot["shot"]
    if image_map[snum] is None:
        continue
    length_frames = max(5, int(shot["duration"] * FPS / 4))
    wf = build_wf(shot["prompt"], snum, image_map[snum], length_frames)
    job_id = submit_wf(wf)
    if job_id:
        job_ids[snum] = job_id
        print("  Shot " + str(snum) + ": " + job_id + " (length=" + str(length_frames) + ")")
    time.sleep(0.3)

print("\nSubmitted " + str(len(job_ids)) + " jobs")
with open(r"C:\Users\user.V915-31\.openclaw\workspace\wan_i2v_jobs.json", "w") as f:
    json.dump(job_ids, f, indent=2)
print("Saved to wan_i2v_jobs.json")
