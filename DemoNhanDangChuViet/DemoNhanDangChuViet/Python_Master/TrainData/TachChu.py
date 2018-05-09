from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

import cv2

def greater(a, b):
    momA = cv2.moments(a)
    if momA['m10'] == 0:
        return 0
    (xa,ya) = int(momA['m10']/momA['m00']), int(momA['m01']/momA['m00'])

    momB = cv2.moments(b)
    if momB['m10'] == 0:
        return 0
    (xb,yb) = int(momB['m10']/momB['m00']), int(momB['m01']/momB['m00'])
    if xa>xb :
        return 1

    if xa == xb:
        return 0
    else:
        return -1
def splict(img,index):
    height = img.shape[0]
    width = img.shape[1]
    start = -1;
    end = -1;
    for i in range(0, width):
        check = 1
        for j in range(0, height/2):
            if(start == -1 and img[j][i]==255):
                check = 0
                start = i;
                end = -1
                break;
            elif(start != -1 and img[j][i] == 255):
                check = 0
                break;
        if check == 1:
            #print "aa"
            end = i;
            check = -1
        if end != -1 and start != -1:
            #print start
            #print end
            temp = img[0:height,start:end]
            #cv2.imshow("aaa",temp)
            #cv2.waitKey(0)
            cv2.imwrite("./catchu/mssv/xuly/"+str(index)+".png",temp)
            print index
            index = index + 1
            start = -1;
            end = -1;
    return index;
def removeSpace(img,index):
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
    print "vo"
    return splict(img,index)                

def getMSSV(im,index):
    mssv = ""
    height = im.shape[0]
    width = im.shape[1]
    im = cv2.resize(im, dsize =(250, int(250*height/width)), interpolation = cv2.INTER_AREA)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)

    image_threshold = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
    #cv2.imshow("ohyeh",image_threshold)
    #cv2.waitKey(0)
    return removeSpace(image_threshold,index)
'''

img = cv2.imread("./catchu/mssv/"+str(7)+"a.png")
index = getMSSV(img,1)
'''    
index = 0
for i in range(1,222):
    img = cv2.imread("./catchu/mssv/"+str(i)+"a.png")
    print "------------------- : " + str(i)
    if img is None:
        continue;
    index = getMSSV(img,index)
