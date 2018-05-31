import sys
sys.path.append('./Mssv')
sys.path.append('./DiemSo')
from RecognitionMSSV import getMSSV
from RecognitionDiemSo import getDiemSo
from Segment_Letters import getDiemChu
from class_diem import Diem
import numpy as np
import cv2
import time

listDiem = [];

def show_wait_destroy(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)
def cutMssv(Origan,img,index):
    mssvIndex = 2;
    dsIndex = 6;
    dcIndex = 7;
    #cv2.imshow("aa",Origan)
    #cv2.waitKey(0)
    currentIndex = 0;
    start = -1;
    end = -1;
    block = -1;
    print "vao.................................................................."
    tempDiem = Diem("null","null","null",-1,-1,-1)
    for i in range(10,img.shape[1]):
        #print img.shape
        if(block == -1 and img[5][i]==255):
            block = 1;
            currentIndex += 1;
            start = i;
        if(block == 1 and img[5][i]==0):
            end = i;
            block = -1
        if((currentIndex == mssvIndex or currentIndex == dsIndex or currentIndex == dcIndex)
           and start!=-1 and end !=-1):
            #cv2.imshow("aa",orig)
            #cv2.waitKey(0)
            if(currentIndex == mssvIndex):
                orig = Origan[0+8:Origan.shape[0]-8,start+15:end-15];
                tempDiem.setMssv(getMSSV(orig))
            elif(currentIndex == dsIndex):
                orig = Origan[0:Origan.shape[0],start:end];
                #cv2.imshow("aa",orig)
                #cv2.waitKey(0)
                cv2.imwrite(str(index)+str(i)+".jpg",orig)
                tempDiem.setDiemSo(getDiemSo(orig))
            elif(currentIndex == dcIndex):
                orig = Origan[0:Origan.shape[0],start:end];
                #cv2.imwrite(str(index)+str(i)+".jpg",orig)
                #cv2.imshow("aa",orig)
                #cv2.waitKey(0)
                diemchu = getDiemChu(orig)
                tempDiem.setDiemChu(diemchu)
        if(start != -1 and end != -1):
            start = -1;
            end = -1;
    listDiem.append(tempDiem)
            
        
def caculator(img, index, width, heigh):
    #cv2.imshow("aa",img)
    #cv2.waitKey(0)
    check = -1;
    start = -1;
    end = -1;
    for i in range(index,heigh):
        if(check == -1 and img[i][10]==255):
            start = i;
            check = 1;
        elif(check == 1 and img[i][10]==0):
            end = i;
            break;
    print start,end
    if start !=-1 and end !=-1 and end-start>20:
        cv2.imwrite(str(i)+".jpg",imgOrigan[start:end,0:width])
        temp = img[start+1:end-1,0:width]
        cv2.imwrite(str(i)+".jpg",temp)
        tempOrigan = imgOrigan[start+1:end,0:width]
        #cv2.imshow("ss",temp)
        #cv2.waitKey(0)
        cutMssv(tempOrigan,temp,i)
        return start, end
    elif start !=-1 and end !=-1 and end-start<20:
        return start, end
    else:
        return -1,-1
print "..................Tach Mssv - Diem So - Diem Chu..............."
print "Du lieu duoc luu tai Python_Master/catchu/"
img = cv2.imread('bangdiem_morph_line.png')
imgOrigan = cv2.imread('bangdiem_reshape.png');

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ret,thresh = cv2.threshold(imgray,127,255,0)
ret2,thresh = cv2.threshold(imgray,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)




width = thresh.shape[1]
height = thresh.shape[0]
index = 0;

while(index<height):
	
    print index
    temp, index = caculator(thresh,index,width,height)
    
    if index == -1:
        break;
'''
for item in listDiem:
    print item.getMssv()
    print item.getDiemSo()
    print item.getDiemChu()
'''
text_file = open("Output.txt", "w")

for i in range(0,len(listDiem)):

    diem = listDiem[i];
    text_file.write(str(diem.getMssv())+"\t"+str(diem.getDiemSo())+"\t"+str(diem.getDiemChu())+"\n");
text_file.close()

    
        
