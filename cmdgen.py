import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
HEADERS = {"Authorization": "Bearer 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"}

async def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        return None
