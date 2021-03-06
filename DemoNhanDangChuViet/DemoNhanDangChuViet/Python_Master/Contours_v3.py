﻿import sys
sys.path.append('./Mssv')
sys.path.append('./DiemSo')
from RecognitionMSSV import getMSSV
from RecognitionDiemSo import getDiemSo
from Segment_Letters import getDiemChu
from class_diem import Diem
import numpy as np
import cv2
import time

def show_wait_destroy(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)

print "..................Tach Mssv - Diem So - Diem Chu..............."
print "Du lieu duoc luu tai Python_Master/catchu/"
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
#    img = cv2.drawContours(img, [cnt], 0, (0,255,0),3)
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
if tempDiem.getMssv() != "null":
    ListDiem.append(tempDiem)
    #------------cat hinh-------------
    #roi = imgOrigan[y+2:y+height, x+5:x+width]
    #http://answers.opencv.org/question/29260/how-to-save-a-rectangular-roi/
    #cv2.imwrite("./chu_tach/roi"+str(i)+".png", roi)
    #---------------------------------
    
    #show_wait_destroy("ohyeh",img)
    
cv2.imwrite('bangdiem_contours.png',img)
#cat diem chu
i = 0
print "..................Tien Hanh Nhan Dien..............."

for diem in ListDiem:
    
    i=i+1
    if diem.mssvCnt is not None:
        x, y, width, height = cv2.boundingRect(diem.mssvCnt)
        roi = imgOrigan[y+8:y+height-8, x+15:x+width-15]
        diem.setMssv(getMSSV(roi))
        cv2.imwrite("./catchu/"+str(i)+"a.png", roi)
    if diem.diemsoCnt is not None:
        x, y, width, height = cv2.boundingRect(diem.diemsoCnt)
        roi = imgOrigan[y:y+height, x:x+width]
        #cv2.imshow("ss",roi)
        #cv2.waitKey(0)
        #print roi.shape
        #diemd = getDiemSo(roi)
       # print diemd
        diem.setDiemSo(getDiemSo(roi))
        cv2.imwrite("./catchu/"+str(i)+"b.png", roi)
    if diem.diemchuCnt is not None:
        x, y, width, height = cv2.boundingRect(diem.diemchuCnt)
        roi = imgOrigan[y:y+height, x:x+width]
        diemchu = getDiemChu(roi)
        diem.setDiemChu(diemchu)
        cv2.imwrite("./catchu/"+str(i)+"c.png", roi)
text_file = open("Output.txt", "w")
for i in range(len(ListDiem)-1,0,-1):
    diem = ListDiem[i];
    text_file.write(str(diem.getMssv())+"\t"+str(diem.getDiemSo())+"\t"+str(diem.getDiemChu())+"\n");
text_file.close()
