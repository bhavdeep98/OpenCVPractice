import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
##    lower_red = np.array([30,50,50])
##    upper_red = np.array([155,125,180])
##    
##    mask = cv2.inRange(hsv, lower_red, upper_red)
##    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8)
#1
    erosion = cv2.erode(hsv,kernel,iterations = 1)
#2
    dilation = cv2.dilate(hsv,kernel,iterations = 1)
#3
    opening = cv2.morphologyEx(hsv, cv2.MORPH_OPEN, kernel)
#4
    closing = cv2.morphologyEx(hsv, cv2.MORPH_CLOSE, kernel)
#5
    gradient = cv2.morphologyEx(hsv, cv2.MORPH_GRADIENT, kernel)
#6
    tophat = cv2.morphologyEx(hsv, cv2.MORPH_TOPHAT, kernel)
#7
    blackhat = cv2.morphologyEx(hsv, cv2.MORPH_BLACKHAT, kernel)


    cv2.imshow('Original',hsv)
##    cv2.imshow('Mask',mask)

    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation',dilation)
    
    cv2.imshow('Opening',opening)
    cv2.imshow('Closign',closing)

    cv2.imshow("Gradient", gradient)

    cv2.imshow("tophat",tophat)
    cv2.imshow("blackhat",blackhat)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
