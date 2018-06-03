import sys
sys.path.append('./Mssv')
sys.path.append('./DiemSo')
from class_diem import Diem
import numpy as np
import cv2
import time

def show_wait_destroy(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)

img = cv2.imread('bangdiem_morph_line.png')
imgOrigan = cv2.imread('bangdiem_reshape.png');
#tang do day
kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ret,thresh = cv2.threshold(imgray,127,255,0)
ret2,thresh = cv2.threshold(imgray,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
temp, contours,hierarchy = cv2.findContours(thresh, 1, 2)
#cv2.imwrite("gru2.png",thresh)
#ve toan bo
#img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
# ve 1 phan
diemchu_col = contours[2]# cot diem chu
diemso_col = contours[3]
massv_col = contours[7]
#lay vi tri


width = img.shape[1]
ps_mssv = width*0.111
ps_ds = width*0.689
ps_dc = width*0.778

i = 0;
index = 0;
list_dc = [];
list_ds = [];
list_mssv = [];
#cai nay de choi - bật lên để hiện thị.
#img = imgOrigan;
check = 0# dung de kiem tra xem mssv, dc, ds co cung 1 hang ko
checkChange = -1 # dung de kiem tra check co bi thay doi ko
tempDiem = Diem("null","null","null",-1,-1,-1)
ListDiem = []
img = imgOrigan.copy()

for cnt in contours:
    #img = cv2.drawContours(img, [cnt], 0, (0,255,0),3)
    #print "-_-"
    #print tempDiem.mssv
    x, y, width, height = cv2.boundingRect(cnt)
    #add vào list điểm chữ
    if(check > y and check < y + height):
        tempChange = -1# ko bi thay doi
    else:#khac
        tempChange = 1
        ListDiem.append(tempDiem)
        tempDiem = Diem("null","null","null",-1,-1,-1)
        check = y + (height/2)    
    if(x < ps_dc and x+width > ps_dc):
        tempDiem.setDiemChu(time.time())
        tempDiem.setCntDiemChu(cnt)
        img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
    #add vào list điểm số
    elif(x < ps_ds and x+width > ps_ds):
        tempDiem.setDiemSo(time.time())
        tempDiem.setCntDiemSo(cnt)
        img = cv2.drawContours(img, [cnt], 0, (255,0,0), 3)
    #add vào list mssv
    elif(x < ps_mssv and x+width > ps_mssv):
        tempDiem.setMssv(time.time())
        tempDiem.setCntMssv(cnt)
        img = cv2.drawContours(img, [cnt], 0, (0,0,255), 3)
    i=i+1

    
cv2.imwrite('bangdiem_contours.png',img)
