from diffusers import StableDiffusionPipeline
import torch
import os


# 1. Setup output folder
os.makedirs("generated_images", exist_ok=True)

# 2. Read prompts
with open("prompts.txt", "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f if line.strip()]

if len(prompts) < 30:
    raise ValueError("⚠️ Task 2 requires at least 30 prompts in prompts.txt!")

# 3. Load Stable Diffusion model
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

# 4. Generate images
for idx, prompt in enumerate(prompts, start=1):
    filename = f"{idx:02d}.png"
    filepath = os.path.join("generated_images", filename)
    print(f"[{idx}/{len(prompts)}] Generating: {prompt}")

    try:
        image = pipe(prompt).images[0]
        image.save(filepath)
        print(f"  ✅ Saved: {filepath}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
        

