import cv2

gst_pipeline = (
    "udpsrc port=5000 caps=\"application/x-rtp, media=video, encoding-name=H264, payload=96\" ! "
    "rtpjitterbuffer ! rtph264depay ! h264parse ! nvv4l2decoder ! nvvidconv ! videoconvert ! appsink"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Failed to open video stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break

    cv2.imshow("Jetson ML Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break

cap.release()
cv2.destroyAllWindows()