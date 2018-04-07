import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
##    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original',frame)
    img = cv2.GaussianBlur(frame,(5,5),0)
    edges = cv2.Canny(img,40,100)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
