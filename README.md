# Task 2 — Image Generation with Pretrained Models

## Model Used
- **Model:** Stable Diffusion v1.5  
- **Checkpoint:** `runwayml/stable-diffusion-v1-5`  
- **Source:** [Hugging Face Model Card](https://huggingface.co/runwayml/stable-diffusion-v1-5)  
- **License:** CreativeML Open RAIL-M  

## Files
- `task2_image_generation.py` — main inference script
- `prompts.txt` — list of prompts (≥ 30)
- `generated_images/` — output images
- `generation_summary.csv` — mapping of prompt → filename
- `inference_notes.md` — environment setup and execution steps
- `failure_analysis.md` — discussion of artefacts and failures

## Safety Statement
- No copyrighted, NSFW, or sensitive prompts were used.  
- Only descriptive, creative, and neutral prompts were included.  
- Safety filters inherent in the Stable Diffusion pipeline were respected.  

## Example Artefacts / Failures
1. *"A robot chef cooking breakfast"* → Robot hands had extra fingers.  
2. *"An astronaut riding a horse on Mars"* → Horse proportions looked distorted.  
3. *"A cyberpunk street market at night"* → Some signs had gibberish text.  
4. *"A futuristic city skyline at sunset"* → Overexposed sun, blurry details.  
5. *"A dragon flying over a medieval castle"* → Wings melted into clouds.  

## Deliverables
- Python code  
- Prompt list (≥ 30)  
- 30+ generated images  
- Example artefacts documented  
- Safety statement included  
