import numpy as np 
import cv2

#cap = cv2.VideoCapture('funny-2-second-video.mp4')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.cv2.COLOR_BGR2HSV)
    cv2.imshow('Video frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()