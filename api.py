from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)

# Load YOLO model once when API starts
model = YOLO("yolov8n.pt")


@app.route("/detect", methods=["POST"])
def detect_phone():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    results = model(image)

    phone_detected = False
    confidence = 0.0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            class_name = model.names[cls]
            if class_name == "cell phone" and conf > 0.60:
                phone_detected = True
                confidence = max(confidence, conf)

    return jsonify({
        "phone_detected": phone_detected,
        "confidence": round(confidence, 2),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

