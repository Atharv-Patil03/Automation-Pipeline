# detect_on_mat.py
import time
import cv2
import numpy as np
from ultralytics import YOLO

# -------- CONFIG ----------
MODEL_PATH = "best.pt"
VIDEO_SOURCE = 0       # your webcam or phone camera URL
WHITE_MIN_AREA_RATIO = 0.05
SHOW = True
# --------------------------

# Load YOLO model
model = YOLO(MODEL_PATH)

def find_biggest_white_contour(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # More strict white detection to avoid false whites
    lower_white = np.array([0, 0, 230])
    upper_white = np.array([180, 12, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # clean mask
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None, mask

    frame_area = frame.shape[0] * frame.shape[1]
    biggest = max(contours, key=cv2.contourArea)

    if cv2.contourArea(biggest) < WHITE_MIN_AREA_RATIO * frame_area:
        return None, mask

    # approx polygon
    peri = cv2.arcLength(biggest, True)
    approx = cv2.approxPolyDP(biggest, 0.03 * peri, True)
    return approx, mask


def is_box_inside(contour, bbox):
    x1, y1, x2, y2 = bbox
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    return cv2.pointPolygonTest(contour, (cx, cy), False) >= 0


def draw_contour_and_bboxes(frame, contour, detections):
    if contour is not None:
        cv2.drawContours(frame, [contour], -1, (0,255,0), 3)

    for det in detections:
        x1,y1,x2,y2,conf,cls = det
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
        cv2.putText(frame, f"{cls} {conf:.2f}", (x1, y1-8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)


def run():
    cap = cv2.VideoCapture(VIDEO_SOURCE)

    if not cap.isOpened():
        print("ERROR: Cannot open video source:", VIDEO_SOURCE)
        return

    # ✅ Prevent webcam buffer buildup (VERY IMPORTANT)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # ✅ Resize frame for speed
        frame = cv2.resize(frame, (960, 540))

        # ✅ Find the white mat
        contour, mask = find_biggest_white_contour(frame)

        if contour is None:
            if frame_count % 50 == 0:
                print("No mat detected.")
            time.sleep(0.01)
            continue

        # ✅ Faster YOLO inference (smaller input)
        results = model(frame, imgsz=320)[0]

        yolo_boxes = []
        for box in results.boxes:
            xyxy = box.xyxy[0].cpu().numpy()
            conf = float(box.conf[0].cpu().numpy())
            cls_id = int(box.cls[0].cpu().numpy())

            x1,y1,x2,y2 = map(int, xyxy)
            yolo_boxes.append((x1,y1,x2,y2,conf,cls_id))

        # ✅ Filter detections
        kept = []
        for (x1,y1,x2,y2,conf,cls_id) in yolo_boxes:
            if conf < 0.7:   # strong filter
                continue
            if is_box_inside(contour, (x1,y1,x2,y2)):
                kept.append((x1,y1,x2,y2,conf,str(cls_id)))

        if frame_count % 100 == 0:
            print("Detections:", kept)

        # ✅ Show only the frame (no slow hstack)
        if SHOW:
            draw_contour_and_bboxes(frame, contour, kept)
            cv2.imshow("frame", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        # ✅ Slight slowdown for terminal (keeps smooth video)
        time.sleep(0.01)

    cap.release()
    cv2.destroyAllWindows()


if _name_ == "_main_":
    run()