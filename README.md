Mobile Phone Detection Using YOLOv8

Project Overview

This project detects mobile phone usage in real-time using YOLOv8 and OpenCV. The system is designed for interview monitoring and cheating detection applications.

Features

- Real-time mobile phone detection
- YOLOv8 object detection
- JSON output generation
- Confidence threshold filtering
- Multi-frame persistence tracking
- Flask API integration
- Static image testing support

Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy
- Flask

Project Structure

Mobile-Phone-Detection-YOLOv8/

├── detect.py

├── test.py

├── api.py

├── requirements.txt

├── README.md

├── output.json

├── sample_results/

│   ├── result1.jpg

│   ├── result2.jpg

│   ├── result3.jpg

│   └── output.json

└── test_images/

├── phone1.jpg

├── phone2.jpg

└── phone3.jpg

Installation

Create virtual environment:

py -3.13 -m venv venv

Activate:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Running Webcam Detection

python detect.py

Press Q to exit.

Running Image Test

python test.py

This script loads an image from test_images/ and returns JSON output without requiring a webcam.

Running Flask API

python api.py

Endpoint:

POST /detect

Example Response:

{
"phone_detected": true,
"confidence": 0.91
}

2-Second Persistence Tracking

The system does not immediately flag a phone when it appears in a single frame.

A timer starts when a phone is first detected.

If the phone remains visible continuously for more than 2 seconds, the system marks it as suspicious activity.

Benefits:

- Reduces false alarms
- Ignores brief accidental appearances
- Improves reliability for interview monitoring

Handling Edge Cases

Partial Visibility

YOLOv8 can detect partially visible phones when enough visual features are present.

Low Resolution

Confidence threshold (0.60) prevents weak detections from being incorrectly classified.

False Positives

Objects such as remotes and wallets may occasionally resemble phones.

The confidence filter reduces such errors.

Sample Results Folder

The sample_results folder contains:

- Detection screenshots
- JSON output examples
- Test evidence for project validation

Sample JSON Output

{
"phone_detected": true,
"confidence": 0.91
}

Future Enhancements

- Face tracking
- Eye gaze monitoring
- Streamlit dashboard
- Cloud deployment
- Multi-camera support

Author

Narendra

AI/ML Internship Project
