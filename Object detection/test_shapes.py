import os
from ultralytics import YOLO
import cv2

# ---------- Paths ----------
weights_path = "C:\\Users\\ATHARV\\OneDrive\\Desktop\\CombinedDataset\\runs\\detect\\final_gpu_model_best\\weights\\best.pt"
image_path = "C:\\Users\\ATHARV\\Pictures\\insta\\IMG_20250419_191745207_HDR~2.jpg"
# ---------- Check files ----------
if not os.path.exists(weights_path):
    raise FileNotFoundError(f"Model weights not found: {weights_path}")

if not os.path.exists(image_path):

    raise FileNotFoundError(f"Input image not found: {image_path}")

# ---------- Load model ----------
model = YOLO(weights_path)

# ---------- Run prediction ----------
results = model.predict(
    source=image_path,
    conf=0.5,      # confidence threshold
    save=False     # set True if you want to save the image
)

# ---------- Show results ----------
result_img = results[0].plot()  # get image with bounding boxes
cv2.imshow("YOLO Prediction", result_img)
cv2.waitKey(0)  # wait for any key press
cv2.destroyAllWindows()

# ---------- Keep console open ----------
input("Press Enter to exit...")

