from ultralytics import YOLO

model = YOLO("C:\\Users\\ATHARV\\OneDrive\\Desktop\\Object detection\\YOLO\\runs\\detect\\train8\\weights\\best.pt")

model.predict(source=0, conf=0.5, show=True)  # 0 = default webcam

