from ultralytics import YOLO
import cv2
import json
import time

# Load YOLO model
model = YOLO("yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

phone_detected = False
confidence = 0
start_time = None

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    current_phone = False

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            label = model.names[cls]

            if label == "cell phone" and conf > 0.60:

                current_phone = True
                confidence = conf

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Phone {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Track phone visibility
    if current_phone:

        if start_time is None:
            start_time = time.time()

        duration = time.time() - start_time

        if duration >= 2:

            phone_detected = True

            output = {
                "phone_detected": True,
                "confidence": round(confidence, 2)
            }

            print(json.dumps(output))

            with open("output.json", "w") as f:
                json.dump(output, f, indent=4)

            cv2.putText(
                frame,
                "Suspicious Activity Detected",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

    else:
        start_time = None
        phone_detected = False

    cv2.imshow("Mobile Phone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()