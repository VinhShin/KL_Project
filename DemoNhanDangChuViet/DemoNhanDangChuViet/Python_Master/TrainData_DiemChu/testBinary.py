
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('3.png',0)
img = cv2.medianBlur(img,5)
value = 200
ret,th1 = cv2.threshold(img,value,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                            cv2.THRESH_BINARY,7,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                            cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('3.png',0)
'''
cv2.imshow('ss',img)
cv2.waitKey(0)
'''
value = 220
ret,thresh1 = cv2.threshold(img,value,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,value,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,value,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,value,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,value,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""
