from Recognition import recognition
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

import cv2

def greater(a, b):
    momA = cv2.moments(a)        
    (xa,ya) = int(momA['m10']/momA['m00']), int(momA['m01']/momA['m00'])

    momB = cv2.moments(b)        
    (xb,yb) = int(momB['m10']/momB['m00']), int(momB['m01']/momB['m00'])
    if xa>xb :
        return 1

    if xa == xb:
        return 0
    else:
        return -1

def cutSpace(img):
    start = -1
    # cat tu tren xuong
    height = img.shape[0]
    width = img.shape[1]
    start = -1
    end = -1
    for i  in range(0,width):
        for j in range(0,height):
            if img[j][i] == 255:
                start = i;
                break;
        if start != -1:
            break;
    for i  in range(width-1,0,-1):
        for j in range(0,height):
            if img[j][i] == 255:
                end = i
                break;
        if end != -1:
            break;

    img = img[0:height,start:end]

    return img
    
def cut(img):
    '''
    for i in range(0,img.shape[1]):
        for j in range(0,img.shape[0]):
            if img.shape[j][i]==255:
       '''
    cv2.imshow("ohyeh",img)
    cv2.waitKey(0)
    img = cutSpace(img)
    cv2.imshow("ohyeh",img)
    cv2.waitKey(0)
    start = 0
    lenght = 19
    while(1):
        temp = img[0:img.shape[1],start:start+lenght]
        cv2.imwrite(str(start)+".png",temp);
        start = start + lenght
        if(start > img.shape[1]):
            break;

def getMSSV(im):
    mssv = ""
    height = im.shape[0]
    width = im.shape[1]
    im = cv2.resize(im, dsize =(300, int(300*height/width)), interpolation = cv2.INTER_AREA)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)

    #ret, image_threshold = cv2.threshold(im_gray, 91, 255, cv2.THRESH_BINARY_INV)
    image_threshold = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
    #cut(image_threshold)
    temp, contours, hierarchy = cv2.findContours(image_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #tim max length của cnt => loai bo tat ca cac cnt < max/2
    maxCnt = contours[0]
    for cnt in contours:
        if(cv2.arcLength(maxCnt,True)<cv2.arcLength(cnt,True)):
            maxCnt = cnt;
        im = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
        #cv2.imshow("ohyeh",im)
        #cv2.waitKey(0)
    lengthCnt = cv2.arcLength(maxCnt,True)/3
    result_CNT = []#result is list include all contour needed
    for cnt in contours:
        if(cv2.arcLength(cnt,True)>lengthCnt):
            result_CNT.append(cnt);
    #sap xep trai -> phai
    result_CNT.sort(greater)
    rectangles = [cv2.boundingRect(ctr) for ctr in result_CNT]
    for rect in rectangles:
        # Desenare dreptunghi
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
        region_of_interest = image_threshold[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
#        cv2.imshow("ohyeh",region_of_interest)
#        cv2.waitKey(0)
        ms = recognition(region_of_interest)
        print ms
        mssv += str(int(ms));
    return mssv
#print getMSSV(cv2.imread("5c.png"))
