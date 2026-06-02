from ultralytics import YOLO
import cv2
import json
from pathlib import Path

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Resolve paths relative to this file so it works no matter where you run it from
ROOT_DIR = Path(__file__).resolve().parent
TEST_IMAGES_DIR = ROOT_DIR / "test_images"

# Prefer phone1.jpg if it exists; otherwise fall back to the first image found in test_images/
preferred = TEST_IMAGES_DIR / "phone1.jpg"
if preferred.exists():
    image_path = preferred
else:
    candidates = sorted(
        [p for p in TEST_IMAGES_DIR.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp"}]
    )
    if not candidates:
        print(f"Error: No test images found in: {TEST_IMAGES_DIR}")
        raise SystemExit(1)
    image_path = candidates[0]

# Read image
image = cv2.imread(str(image_path))
if image is None:
    print(f"Error: Image not found or unreadable: {image_path}")
    raise SystemExit(1)

# Run detection
results = model(image)

phone_detected = False
confidence = 0.0

# Check detections
for result in results:
    for box in result.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        class_name = model.names[cls]

        if class_name == "cell phone" and conf > 0.60:
            phone_detected = True
            confidence = max(confidence, conf)

# Create output
output = {
    "phone_detected": phone_detected,
    "confidence": round(confidence, 2),
    "image_used": str(image_path.name),
}

# Print JSON output
print(json.dumps(output, indent=4))

# Save JSON file next to the script output
with open(ROOT_DIR / "output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print(f"\nResult saved to {(ROOT_DIR / 'output.json').as_posix()}")

