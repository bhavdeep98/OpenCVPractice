import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
##    lower_red = np.array([30,150,50])
##    upper_red = np.array([255,255,180])
##    
##    mask = cv2.inRange(hsv, lower_red, upper_red)
##    res = cv2.bitwise_and(frame,frame, mask= mask)

##    kernel = np.ones((15,15),np.float32)/225
##    smoothed = cv2.filter2D(hsv,-1,kernel)

    blur = cv2.blur(hsv,(13,13))
    cv2.imshow('Original',frame)
    cv2.imshow('Averaging',blur)

    blur = cv2.GaussianBlur(hsv,(13,13),0)
    cv2.imshow('Gaussian Blurring',blur)

    median = cv2.medianBlur(hsv,13)
    cv2.imshow('Median Blur',median)

    bilateral = cv2.bilateralFilter(hsv ,13,75,75)
    cv2.imshow('bilateral Blur',bilateral)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
