import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while (True):
    retval, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 150, 60])
    upper_red = np.array([179, 255, 180])

    mask = cv2.inRange(hsv,lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
