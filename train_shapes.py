from ultralytics import YOLO

def main():
    # Load the model (start from pretrained or your last run)
    model = YOLO("runs/detect/train/weights/last.pt")  # or "yolov8n.pt"

    # Train the model
    model.train(
        data="shapes_yolo_dataset/data.yaml",
        epochs=30,
        imgsz=256,
        batch=16,
        device=0,          # Use GPU
        half=True,         # Mixed precision = faster training
        workers=0,         # <- Important for Windows multiprocessing!
        name="train3"      # new run name
    )

if __name__ == "__main__":
    main()
