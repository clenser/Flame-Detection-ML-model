# YOLO v8-Based Flame Detection Project

## Overview
This project implements a fire detection system using **YOLO v8** deep learning model to detect flames in real-time. It processes video feeds from an IP camera or ESP32-CAM and provides alerts when fire is detected.

## Features
- **Real-Time Fire Detection** using a trained YOLO v8 model.
- **Live Video Stream Processing** from an IP camera or ESP32-CAM.
- **Buzzer Alerts** using Arduino and PyFirmata2.
- **ESP-NOW Communication** for wireless alerts (optional).

## Hardware Components
- **ESP32-CAM** (or Mobile IP Camera for live streaming)
- **Laptop/PC** (for running YOLO v8 model)
- **Arduino Uno** (for buzzer control)
- **Buzzer** (for fire alert sound)

## Software Requirements
- **Python 3.x** (for YOLO v8 and communication scripts)
- **PyTorch & Ultralytics YOLOv8**
- **OpenCV** (for image processing)
- **PyFirmata2** (for controlling Arduino buzzer alerts)
- **ESP-NOW Library** (for wireless communication, if used)
- **Arduino IDE** (for microcontroller programming)

## Installation & Setup
### 1. Install Dependencies
```sh
pip install ultralytics opencv-python numpy pyfirmata2
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
pip install -e .
```

### 2. Setup YOLO v8 Model
- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/sreemantabarman/flame-dataset-candlelightermatch-stick-flames/data) and prepare it for training.
- Train a custom YOLO v8 model for fire detection or use a pre-trained model.
- Place the model weights (e.g., `fire_model.pt`) in the project directory.
- Train a custom YOLO v8 model for fire detection or use a pre-trained model.
- Place the model weights (e.g., `fire_model.pt`) in the project directory.

### 3. Configure IP Camera / ESP32-CAM
- For an IP camera, set up the RTSP or MJPEG stream.
- For ESP32-CAM, use Arduino IDE to flash the streaming code.

### 4. Run Fire Detection & Alert System
```sh
python detect_fire.py --model fire_model.pt --camera rtsp://your_ip_stream
```

## Working Mechanism
1. **Fire Detection**: The YOLO v8 model processes the video feed to detect flames.
2. **Buzzer Alerts**: An Arduino-controlled buzzer beeps when fire is detected.
3. **Wireless Alert (Optional)**: ESP-NOW can send fire detection notifications to other devices.

## Future Improvements
- Improve fire detection accuracy with more training data.
- Implement real-time cloud monitoring.
- Integrate SMS or email alerts.

## Credits
- Developed by Sreemanta Barman
- YOLO v8 by **Ultralytics**
- Open-source contributions & community support

## License
This project is licensed under the MIT License.

