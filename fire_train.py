from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8s.pt")  # Using YOLOv8s for training
    epochs = 85  # Total number of training epochs

    # Train the model
    model.train(data=r"C:\Users\srbar\Desktop\Fire\dataset\data.yaml", #path to data.yaml file
                epochs=epochs, imgsz=640, batch=8, device="cuda", workers=0)

if __name__ == "__main__":  # Prevent multiprocessing issues on Windows
    train_model()
