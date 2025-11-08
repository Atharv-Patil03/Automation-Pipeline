import cv2

gst_recv=(
    'udpsrc port =5001 caps="application/x-rtp, media=video, encoding-name=H264, payload=96" ! '
    'rtph26depay ! avdec_h264 ! videoconvert ! appsink'
)


cap = cv2.VideoCapture(gst_recv, cv2.CAP_GSTREAMER)


while True: 
    ret, frame = cap.read()
    if not ret:
        continue

    
    cv2.imshow("Jetson Stream", frame)

    if cv2.waitKey(1) == 27:
        break

