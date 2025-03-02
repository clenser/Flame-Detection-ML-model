from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\srbar\Desktop\Fire\runs\detect\train\weights\best.pt")  

cap = cv2.VideoCapture("http://192.168.80.195:8080/video")  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.20, iou=0.5)  

    for r in results:
        frame = r.plot() 

    cv2.imshow("Fire Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
