from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
import time


import cv2

def cutSpace(img,index):
    # cat tu tren xuong
    height = img.shape[0]
    width = img.shape[1]
    end = height
    start = 0
    for i in range(2*height/3,height):
        countSpace = 0;
        count255Pixel = 0;
        for j in range(0,width):
            if img[i][j] == 255:
                countSpace = 1;
        if countSpace == 0:# gap chu
            end = i;
            break;

   # cat tu duoi len
    height = img.shape[0]
    width = img.shape[1]
    for i  in range(2*height/3,0,-1):
        countSpace = 0;
        count255Pixel = 0;
        for j in range(0,width):
            if img[i][j] == 255:
                countSpace = 1;
                count255Pixel = count255Pixel + 1;
        if countSpace == 0:# gap chu
            start = i;
            break;
    img = img[start: end,0:width]
    cv2.waitKey(0)
    cv2.imwrite("./Train_V2/"+str(index)+".png",img);
    


def extract_letter(img_thre,index):
    height = img_thre.shape[0]
    width = img_thre.shape[1]
    start = -1
    end = -1
    count = 0
    for i in range(0,width):
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
        if count > 12 or i == width-1:
            if i == width -1 and end ==-1:
                end = i
            if end == -1 or start ==-1 or end - start < 10:
                break;
            count = 0;
            temp = img_thre[0:height, start:end]
            cutSpace(temp,index)
            index += 1;
            start = -1
            end = -1
    return index;
'''
while(1):
    img_name = raw_input("show name of image -_-: ")
    im = cv2.imread(str(img_name)+'.png')
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)
    img_thre = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
    extract_letter(img_thre)
'''
index = 0
for i in range(1,187):
    img = cv2.imread("./catchu/diemchu/"+str(i)+"c.png")
    if img is None:
        continue;
    print "......."+str(index)
    cv2.imshow("aaa",img)
    cv2.waitKey(0)
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)
    img_thre = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
    index = extract_letter(img_thre,index)    
