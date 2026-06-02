import requests

url = "http://127.0.0.1:5000/detect"

# NOTE:
# The test_images folder in this repo contains only screenshots.
# Use one of them here.
image_path = "test_images/Screenshot 2026-06-02 100408.png"

with open(image_path, "rb") as image:
    response = requests.post(
        url,
        files={"image": image}
    )

print(response.json())

