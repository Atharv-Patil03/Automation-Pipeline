import cv2

gst_pipeline = (
    "udpsrc port=5000 caps=\"application/x-rtp, media=video, encoding-name=H264, payload=96\" ! "
    "rtpjitterbuffer latency=100 ! rtph264depay ! h264parse ! "
    "avdec_h264 ! videoconvert ! appsink sync=false"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("❌ Failed to open video stream")
    exit()

while True: 
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    print("✅ Frame shape:", frame.shape)  # Should be (480, 640, 3)
    cv2.imshow("Jetson Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()