from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
import time

import cv2

def cutSpace(img):
    print " ggg"
    start = -1
    # cat tu tren xuong
    height = img.shape[0]
    width = img.shape[1]
    for i  in range(0,height):
        countSpace = 0;
        count255Pixel = 0;
        for j in range(0,width):
            if img[i][j] == 255:
                countSpace = 1;
                count255Pixel = count255Pixel + 1;
        if start !=-1 and count255Pixel > 3:# gap chu
            cv2.imshow("a",img)
            cv2.waitKey(0)
            img = img[start:height,0:width]

            cv2.imshow("b",img)
            cv2.waitKey(0)
            start = -1
            break;
        else:
            start = i;
   # cat tu duoi len
    height = img.shape[0]
    width = img.shape[1]
    for i  in range(height-1,0,-1):
        print "ss"
        countSpace = 0;
        count255Pixel = 0;
        for j in range(0,width):
            if img[i][j] == 255:
                countSpace = 1;
                count255Pixel = count255Pixel + 1;
        if start !=-1 and count255Pixel > 3:# gap chu
            print "cat dx ui ma ta -_-"
            print start
            print height
            img = img[0:height - (height-start+1),0:width]
            cv2.imshow("c",img)
            cv2.waitKey(0)
      #      print time.time()
            cv2.imwrite(str(round(time.time()))+".png",img);
            break;
        else:
            start = i

#im = cv2.imread('./image/digit-reco.jpg')
im = cv2.imread('9.png')
#shin add
'''
height = im.shape[0]
width = im.shape[1]
print("\n Resizing Image........")
im = cv2.resize(im, dsize =(1000, int(1000*height/width)), interpolation = cv2.INTER_AREA)
'''



im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow("Final classification", im_gray)
cv2.waitKey()
im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)
cv2.imshow("Final classification", im_gray)
cv2.waitKey()
#ret, image_threshold = cv2.threshold(im_gray, 91, 255, cv2.THRESH_BINARY_INV)
img_thre = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
#ret,img_thre = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
# loai bo contour nho

'''
temp, contours, hierarchy = cv2.findContours(img_thre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#tim max length của cnt => loai bo tat ca cac cnt < max/2
maxCnt = contours[0]
for cnt in contours:
    if(cv2.arcLength(maxCnt,True)<cv2.arcLength(cnt,True)):
        maxCnt = cnt;
    im = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
    cv2.imshow("Final classification", im)
    cv2.waitKey()
lengthCnt = cv2.arcLength(maxCnt,True)/2
result_CNT = []#result is list include all contour needed
for cnt in contours:
    if(cv2.arcLength(cnt,True)>lengthCnt):
        cv2.drawContours(img_thre, [cnt], -1, (0,255,255), -1)
        result_CNT.append(cnt);
#        contours.remove(cnt)



'''
cv2.imshow("Final classification", img_thre)
cv2.waitKey()
"""
temp, contours, hierarchy = cv2.findContours(image_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#tim max length của cnt => loai bo tat ca cac cnt < max/2

for cnt in contours:
    print "oh yeyeye"
    print cnt
    print cv2.contourArea(cnt);
    im = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
    cv2.imshow("oh yeh",im);
    cv2.waitKey(0)
"""

height = img_thre.shape[0]
width = img_thre.shape[1]
start = -1
end = -1
count = 0

for i  in range(0,width):
    check = 1;
     # phai du 30 pixel 0 moi cat
    for j in range(0,height):
        if start == -1 and img_thre[j][i] == 255:
            start = i;
            check = 0;#la diem dau => ko phai diem cuoi
            break;# tim thay diem bat dau => out
        elif img_thre[j][i] == 255:#=> ko phai khoang cach
            check = 0;
            end = -1
            break;
    if check == 1 and start !=-1:
        if end == -1:
            end = i;
        count = count + 1
    if count > 5:
        count = 0;
        print "oh yeh"
        print start
        print i - start;
        temp = img_thre[0:height, start:end]
        cutSpace(temp)
        #cv2.imwrite(str(i)+".png",temp);
        start = -1

