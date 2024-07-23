import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

image_bytes = query({
    "inputs": "angkor wat 4k hd with purple sky v5",
})

# Save the image bytes to a file
with open("kak.png", "wb") as f:
    f.write(image_bytes)

