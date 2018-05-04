from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

import cv2

#clf = joblib.load('./recognition_mssv/train_digit.pkl')
clf = joblib.load('train_digit.pkl')

def getMSSV(im):
    mssv = ""
    height = im.shape[0]
    width = im.shape[1]
    im = cv2.resize(im, dsize =(200, int(200*height/width)), interpolation = cv2.INTER_AREA)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)

    #ret, image_threshold = cv2.threshold(im_gray, 91, 255, cv2.THRESH_BINARY_INV)
    image_threshold = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)

    temp, contours, hierarchy = cv2.findContours(image_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #tim max length của cnt => loai bo tat ca cac cnt < max/2
    maxCnt = contours[0]
    for cnt in contours:
        if(cv2.arcLength(maxCnt,True)<cv2.arcLength(cnt,True)):
            maxCnt = cnt;
        im = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
        cv2.imshow("ss",im)
        cv2.waitKey(0)
    lengthCnt = cv2.arcLength(maxCnt,True)/2
    result_CNT = []#result is list include all contour needed
    for cnt in contours:
        if(cv2.arcLength(cnt,True)>lengthCnt):
            result_CNT.append(cnt);
    rectangles = [cv2.boundingRect(ctr) for ctr in result_CNT]
    for rect in rectangles:
        # Desenare dreptunghi
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
        region_of_interest = image_threshold[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
        roi = cv2.resize(region_of_interest, (28, 28), interpolation=cv2.INTER_AREA)
        roi = cv2.dilate(roi, (3, 3)) 
        fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
        nbr = clf.predict(np.array([fd], 'float64'))
        mssv += str(int(nbr[0]));
    return mssv
getMSSV(cv2.imread("5c.png"))
