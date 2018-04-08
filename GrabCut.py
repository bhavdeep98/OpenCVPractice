import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial2.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (550,70,350,550)
##cv2.rectangle(img,(550,70),(900,620),(0,0,255),2)
##cv2.imshow('image',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
blur = cv2.GaussianBlur(img,(13,13),0)

plt.imshow(blur)
plt.colorbar()
plt.show()
