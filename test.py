import cv2
import numpy as np
cap = cv2.VideoCapture(0)
last_mean = 0
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = np.abs(np.mean(gray) - last_mean)
    if result > 0.3:
        print(result)
    last_mean= np.mean(gray)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()