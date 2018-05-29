from RecognitionDS import recognition
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
sizeScale = 100;
def getDiemSo(im):
    
    #cv2.imwrite("memay.png", im)
    imtemp = im.copy()
    global sizeScale
    diemso = ""
    height = imtemp.shape[0]
    width = imtemp.shape[1]
    imtemp = cv2.resize(imtemp, dsize =(sizeScale, int(sizeScale*height/width)), interpolation = cv2.INTER_AREA)

    im_gray = cv2.cvtColor(imtemp, cv2.COLOR_BGR2GRAY)
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
    lengthCnt = cv2.arcLength(maxCnt,True)/3
	#loai bo gia tri ko can thiet
    for cnt in contours:
        if(cv2.arcLength(cnt,True)<lengthCnt):
             image_threshold = cv2.drawContours(image_threshold, [cnt], 0, (0,0,0), -1)
    result_CNT = []#result is list include all contour needed
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    #chi lay 2 contours lon nhat
    if len(contours)>2:
        result_CNT.append(contours[0])
        result_CNT.append(contours[1])

    #sap xep trai -> phai
    result_CNT.sort(greater)
    rectangles = [cv2.boundingRect(ctr) for ctr in result_CNT]
    for rect in rectangles:
        # Desenare dreptunghi
        cv2.rectangle(imtemp, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
        region_of_interest = image_threshold[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
        #cv2.imshow("ohyeh",region_of_interest)
        #cv2.waitKey(0)
        ms = recognition(region_of_interest)
        if(len(diemso)==1):
            diemso += "."+str(int(ms))
        else:
            diemso += str(int(ms));
    #if(len(diemso)>2):
    #    sizeScale = 100
    #    return getDiemSo(im)
    #print diemso
    return diemso
#img = cv2.imread("memay.png");

#print getDiemSo(img)
