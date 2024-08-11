from celery import shared_task
import requests, base64, os
from datetime import datetime
from text_to_image.models import GeneratedImage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(BASE_DIR, 'out')
os.makedirs(out_dir, exist_ok=True)

@shared_task(name='text_to_image.tasks.generate_image')
def generate_image(prompt):
    try:
        print("Task started with params:", prompt)
        api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        headers = {
            "Authorization": f"Bearer {os.getenv('STABILITY_AI_API_KEY')}",
            "Content-Type": "application/json"
        }
        payload = {
            "text_prompts": [{"text": prompt}],
            "width": 1024,
            "height": 1024,
            "samples": 1
        }
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for i, image in enumerate(data["artifacts"]):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                file_path = os.path.join(out_dir, f"v1_txt2img_{timestamp}.png")
                with open(file_path, "wb") as f:
                    f.write(base64.b64decode(image["base64"]))
                    image_url = file_path
                    GeneratedImage.objects.create(prompt=prompt, image_url=image_url)
            return {"status": "success", "image_url": image_url}
        else:
            return {"status": "error", "message": response.json()}
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "message": str(e)}
