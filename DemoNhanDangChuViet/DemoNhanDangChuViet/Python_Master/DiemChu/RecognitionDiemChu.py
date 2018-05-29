#!/usr/bin/env python

import cv2 as cv
import numpy as np
#from skimage.feature import hog

SZ=20
bin_n = 16 # Number of bins


affine_flags = cv.WARP_INVERSE_MAP|cv.INTER_LINEAR
chuso = ["hai","ba","bon","nam","sau","bay","tam","chin","muoi","nam"]


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
def recognition(img):
    if img.shape[0] <= 0 or img.shape[1] <= 0:
        return ""
    svm = cv.ml.SVM_create()
    svm.setKernel(cv.ml.SVM_LINEAR)
    svm.setType(cv.ml.SVM_C_SVC)
    svm.setC(2.67)
    svm.setGamma(5.383)
    
    svm = cv.ml.SVM_load('DiemChu/svm_data.dat')
#    svm = cv.ml.SVM_load('svm_data.dat')
    #print img.shape
    #cv.imshow("ss",img)
    #cv.waitKey(0)
    
    roi = cv.resize(img, (56, 28), interpolation=cv.INTER_AREA)
    fd = hog(roi)
    testData = np.float32(fd).reshape(-1,bin_n*4)
    nbr = svm.predict(testData)[1]
    return chuso[int(nbr[0][0])]

#print recognition(cv.imread("q.png"))
