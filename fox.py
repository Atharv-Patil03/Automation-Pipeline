import cv2 

cap = cv2.VideoCapture("udp://@:5000")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    