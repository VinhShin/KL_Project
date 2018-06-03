import sys
import numpy as np
import cv2
import time


def show_wait_destroy(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)
def cutMssv(Origan,img,index,ps):
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
                cv2.imwrite(str(ps)+'.jpg',orig)
                ps += 1
                #tempDiem.setMssv(getMSSV(orig))
            elif(currentIndex == dsIndex):
                orig = Origan[0:Origan.shape[0],start:end];
                #cv2.imshow("ss",orig)
                #cv2.waitKey(0)

                #cv2.imshow("aa",orig)
                #cv2.waitKey(0)
#                cv2.imwrite(str(index)+str(i)+".jpg",orig)
#                tempDiem.setDiemSo(getDiemSo(orig))
                cv2.imwrite(str(ps)+'.jpg',orig)
                ps += 1

            elif(currentIndex == dcIndex):
                orig = Origan[0:Origan.shape[0],start:end];
                #cv2.imshow("ss",orig)
                #cv2.waitKey(0)
                cv2.imwrite(str(ps)+'.jpg',orig)
                ps += 1

                #cv2.imwrite(str(index)+str(i)+".jpg",orig)
                #cv2.imshow("aa",orig)
                #cv2.waitKey(0)
                #diemchu = getDiemChu(orig)
                #tempDiem.setDiemChu(diemchu)
        if(start != -1 and end != -1):
            start = -1;
            end = -1;
    return ps
            
        
def caculator(img, index, width, heigh,ps):
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
    #print start,end
    if start !=-1 and end !=-1 and end-start>20:
        #cv2.imwrite(str(i)+".jpg",imgOrigan[start:end,0:width])
        temp = img[start+1:end-1,0:width]
        #cv2.imwrite(str(i)+".jpg",temp)
        tempOrigan = imgOrigan[start+1:end,0:width]
        #cv2.imshow("ss",temp)
        #cv2.waitKey(0)
       # cv2.imshow("ss",temp)
       # cv2.waitKey(0)
       # cv2.imshow("ss",tempOrigan)
       # cv2.waitKey(0)
        ps = cutMssv(tempOrigan,temp,i,ps)
        return ps, start, end
    elif start !=-1 and end !=-1 and end-start<20:
        return ps, start, end
    else:
        return ps, -1,-1

def catnoidung(img,imgOrigan,ps):
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #ret,thresh = cv2.threshold(imgray,127,255,0)
    ret2,thresh = cv2.threshold(imgray,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



   # cv2.imshow("ss",thresh)
   # cv2.waitKey(0)
    
    width = thresh.shape[1]
    height = thresh.shape[0]
    index = 0;

    while(index<height):
            
        #print index
        ps, temp, index = caculator(thresh,index,width,height,ps)
        
        if index == -1:
            break;
    return ps
ps = 0;
for i in range(1,23):
    #print i;
    img = cv2.imread('bangdiem_morph_line'+str(i)+'.png')
    imgOrigan = cv2.imread('bangdiem_reshape'+str(i)+'.png');
   # cv2.imshow("ss",imgOrigan)
   # cv2.waitKey(0)
    #cv2.imshow("ss",img)
    #cv2.waitKey(0)
    ps = catnoidung(img,imgOrigan,ps);
    print ps


    
        
