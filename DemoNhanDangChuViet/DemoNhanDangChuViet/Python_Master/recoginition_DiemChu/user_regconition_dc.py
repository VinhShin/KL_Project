#!/usr/bin/env python

import cv2 as cv
import numpy as np
#from skimage.feature import hog

SZ=20
bin_n = 16 # Number of bins


affine_flags = cv.WARP_INVERSE_MAP|cv.INTER_LINEAR


## [hog]
def hog(img):
    gx = cv.Sobel(img, cv.CV_32F, 1, 0)
    gy = cv.Sobel(img, cv.CV_32F, 0, 1)
    mag, ang = cv.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist
## [hog]

responses = np.repeat(np.arange(4),9)[:,np.newaxis]
svm = cv.ml.SVM_create()

svm = cv.ml.SVM_load('svm_data.dat')
imgTest = cv.imread("g.png",0)
roi = cv.resize(imgTest, (56, 28), interpolation=cv.INTER_AREA)
#roi = cv.dilate(roi, (3, 3))
 
fd = hog(roi)
testData = np.float32(fd).reshape(-1,bin_n*4)
nbr = svm.predict(testData)
print nbr

