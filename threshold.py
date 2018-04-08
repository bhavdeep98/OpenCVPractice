import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, thresholdToZero = cv2.threshold(grayscaled, 9, 255, cv2.THRESH_TOZERO)
## TOZERO means the lower values than threshhold
## will have dradient values like TRUNC
## but the upper bound will have absolute values  
retval, threshold = cv2.threshold(grayscaled, 9, 255, cv2.THRESH_BINARY)

cv2.imshow('original',img)
cv2.imshow('thresholdToZero',thresholdToZero)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
