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

Xmssv = -1;
X2mssv = -1;

Xds = -1;
X2ds = -1;

Xdc = -1;
X2dc = -1;

def show_wait_destroy(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)
def switchDiemChu(ds):
    if len(ds) == 0:
        return "";
    switcher = {
        0: "Khong",
        1: "Mot",
        2: "Hai",
        3: "Ba",
        4: "Bon",
        5: "Nam",
        6: "Sau",
        7: "Bay",
        8: "Tam",
        9: "Chin",
        10: "Muoi",
    }
    #d1 truoc thap phan
    #d2 sau thap phan
    print ds
    d1,d2 = ds.split('.',1);

    ds1 = switcher.get(int(d1),"Null");
    ds2 = switcher.get(int(d2),"Null");

    if(ds2 == "Khong"):
        ds2 = "";
    
    
    return  ds1 + " " + ds2
    #print switcher.get(argument, "Invalid month")
def cutMssv(Origan,img,index):
    global Xmssv;
    global X2mssv;
    global Xds;
    global X2ds;
    global Xdc;
    global X2dc;


    
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
                #cv2.imshow("ss",orig)
                #cv2.waitKey(0)
                if(Xmssv == -1):
                    Xmssv = start;
                    X2mssv = end;
                tempDiem.setMssv(getMSSV(orig))
            elif(currentIndex == dsIndex):
                orig = Origan[0:Origan.shape[0],start:end];
                #cv2.imshow("aa",orig)
                #cv2.waitKey(0)
                #cv2.imwrite(str(index)+str(i)+".jpg",orig)
                tempDiem.setDiemSo(getDiemSo(orig))
                if(Xds == -1):
                    Xds = start;
                    X2ds = end;
            elif(currentIndex == dcIndex):
                orig = Origan[0:Origan.shape[0],start:end];
                #cv2.imwrite(str(index)+str(i)+".jpg",orig)
                #cv2.imshow("aa",orig)
                #cv2.waitKey(0)
                diemchu = getDiemChu(orig)
                tempDiem.setDiemChu(diemchu)
                if(Xdc == -1):
                    Xdc = start;
                    X2dc = end;
        if(start != -1 and end != -1):
            start = -1;
            end = -1;
    listDiem.append(tempDiem)
            
        
def caculator(img, index, width, heigh, avoid):

    check = -1;
    start = -1;
    end = -1;
    for i in range(index,heigh):
        if(check == -1 and img[i][100]==255):
            start = i;
            check = 1;
        elif(check == 1 and img[i][100]==0):
            end = i;
            break;
    print start,end
    if start !=-1 and end !=-1 and end-start>20:
        if avoid != 1:
            #cv2.imwrite(str(i)+".jpg",imgOrigan[start:end,0:width])
            temp = img[start+1:end-1,0:width]
            #cv2.imwrite(str(i)+".jpg",temp)
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
imgDrawing = cv2.imread('bangdiem_reshape.png');
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ret,thresh = cv2.threshold(imgray,127,255,0)
ret2,thresh = cv2.threshold(imgray,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imwrite("kk.png",thresh)

width = thresh.shape[1]
height = thresh.shape[0]
index = 0;
avoid = 1;
while(index<height):
	
    print index
    #cv2.imshow("sss",thresh)
    #cv2.waitKey(0)
    temp, index = caculator(thresh,index,width,height,avoid)
    avoid = -1;
    if index == -1:
        break;
cv2.rectangle(imgDrawing,(Xmssv,0),(X2mssv,imgDrawing.shape[0]),(0,0,255),3)
cv2.rectangle(imgDrawing,(Xds,0),(X2ds,imgDrawing.shape[0]),(0,255,0),3)
cv2.rectangle(imgDrawing,(Xdc,0),(X2dc,imgDrawing.shape[0]),(255,0,0),3)
cv2.imwrite("vunganh.jpg",imgDrawing)
'''
for item in listDiem:
    print item.getMssv()
    print item.getDiemSo()
    print item.getDiemChu()
'''
text_file = open("Output.txt", "w")

for i in range(0,len(listDiem)):

    diem = listDiem[i];
    #text_file.write(str(diem.getMssv())+"\t"+str(diem.getDiemSo())+"\t"+str(diem.getDiemChu())+"\n");
    text_file.write(str(diem.getMssv())+"\t"+str(diem.getDiemSo())+"\t"+switchDiemChu(diem.getDiemSo())+"\n");

text_file.close()

    
        
