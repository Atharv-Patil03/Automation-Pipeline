import cv2
 
url = ""
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("❌ Failed to open video stream")
   

while True: 
    ret, frame = cap.read()
    if not ret:
       
        continue

    cv2.imshow("Thermal Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()