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
def splict(img):
    #cv2.imshow("ohyeh",img)
    #cv2.waitKey(0)
    mssv = ""
    height = img.shape[0]
    width = img.shape[1]
    start = -1;
    end = -1;
    for i in range(0, width):
        check = 1
        for j in range(0, height):
            if(start == -1 and img[j][i]==255):
                check = 0
                start = i;
                end = -1
                break;
            elif(start != -1 and img[j][i] == 255):
                check = 0
                break;
        if check == 1 or i == width-1:
            #print "aa"
            end = i;
            if end-start<10:
                end = -1
            check = -1
        if end != -1 and start != -1:
            #print start
            #print end
            temp = img[0:height,start:end]
            if temp.shape[1] > 35:#truong hop bi noi => cat ra
                mssv_temp = recognition(temp[0:height,0:temp.shape[1]/2])
                mssv += str(int(mssv_temp))
                mssv_temp = recognition(temp[0:height,temp.shape[1]/2:temp.shape[1]])
                mssv += str(int(mssv_temp))
            else:
                #print temp.shape
                mssv_temp = recognition(temp)
                #print mssv_temp
                mssv += str(int(mssv_temp))
                #cv2.imshow("ohyeh",temp)
                #cv2.waitKey(0)
            start = -1;
            end = -1;
    return mssv;
def removeSpace(img):
    height = img.shape[0]
    width = img.shape[1]
    start_h = -1
    end_h = -1
    start_w = -1
    end_w = -1
    for i in range(height/2,0,-1):
        check = 0;#
        for j in range(0,width):
            if(img[i][j]==255):
                check = 1;
                break;
        if check == 0:
            start_h = i
            break;
    for i in range(height/2,height):
        check = 0;#
        for j in range(0,width):
            if(img[i][j]==255):
                check = 1;
                break;
        if check == 0:
            end_h = i
            break;
    img = img[start_h:end_h,0:width]
    height = img.shape[0]
    width = img.shape[1]
    for i in range(0,width):
        check = 0;#
        for j in range(0,height/2):
            if(img[j][i]==255):
                start_w = i
                check = 1;
                break;
        if check == 1:
            break;
    for i in range(width-1,0,-1):
        check = 0;#
        for j in range(0,height/2):
            if(img[j][i]==255):
                check = 1;
                end_w = i;
                break;
        if check == 1:
            break;
    
    img = img[0:height,start_w:end_w]
    #cv2.imshow("ohyeh",img)
    #cv2.waitKey(0)
    return splict(img)     
def getMSSV(im):
    mssv = ""
    height = im.shape[0]
    width = im.shape[1]
    im = cv2.resize(im, dsize =(250, int(250*height/width)), interpolation = cv2.INTER_AREA)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)

    image_threshold = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
    #cv2.imshow("ohyeh",image_threshold)
    #cv2.waitKey(0)
    return removeSpace(image_threshold)
#print getMSSV(cv2.imread("7a.png"))
