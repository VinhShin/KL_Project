#!/usr/bin/env python

import cv2 as cv
import numpy as np
#from skimage.feature import hog

SZ=20
bin_n = 16 # Number of bins


affine_flags = cv.WARP_INVERSE_MAP|cv.INTER_LINEAR

## [deskew]
def deskew(img):
    m = cv.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
   # img = cv.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    img = cv.warpAffine(img,M,(56, 28),flags=affine_flags)

    return img
## [deskew]

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

img = cv.imread('trainData.png',0)
imgTest = cv.imread('ww.png')
if img is None:
    raise Exception("we need the digits.png image from samples/data here !")


train_cells = [np.hsplit(row,9) for row in np.vsplit(img,4)]
# First half is trainData, remaining is testData
'''
print len(cells)
train_cells = [ i[:9] for i in cells ]
print len(train_cells)
test_cells = [ i[50:] for i in cells]
'''
######     Now training      ########################

deskewed = [list(map(deskew,row)) for row in train_cells]
hogdata = [list(map(hog,row)) for row in deskewed]
trainData = np.float32(hogdata).reshape(-1,64)
'''
responses = np.repeat(np.arange(10),250)[:,np.newaxis]
print responses
'''
responses = []
for i in range(0,9):
    responses.append(i)
responses = np.repeat(np.arange(4),9)[:,np.newaxis]
svm = cv.ml.SVM_create()
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setType(cv.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)

svm.train(trainData, cv.ml.ROW_SAMPLE, responses)
svm.save('svm_data.dat')

######     Now testing      ########################

#shin add
#test

'''
imgTest = cv.resize(imgTest, (56, 28), interpolation=cv.INTER_AREA)
x2 = np.array(imgTest)
testData = np.float32(hogdata).reshape(-1,bin_n*4)
'''
"""
deskewed = [list(map(deskew,row)) for row in imgTest]
hogdata = [list(map(hog,row)) for row in deskewed]
"""
'''
deskewed = map(deskew,imgTest)
hogdata = map(hog,deskewed)
testData = np.float32(hogdata).reshape(-1,bin_n*4)
chuso = svm.predict(testData)
print chuso
'''
imgTest = cv.imread("b.png",0)
roi = cv.resize(imgTest, (56, 28), interpolation=cv.INTER_AREA)
#roi = cv.dilate(roi, (3, 3))
 
fd = hog(roi)
testData = np.float32(fd).reshape(-1,bin_n*4)
nbr = svm.predict(testData)
print nbr

