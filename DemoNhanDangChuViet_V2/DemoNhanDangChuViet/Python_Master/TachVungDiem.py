import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt


#img = cv2.imread('./bangdiem1/bangdiem2.png')
#imgOrign = cv2.imread('./bangdiem1/bangdiem2.png')
#print img
img = cv2.imread(sys.argv[1])
imgOrign = cv2.imread(sys.argv[1])
'''
# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
'''

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img,(3,3),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms
'''
cv2.imshow("1",th1)
cv2.waitKey(0)
cv2.imshow("1",th2)
cv2.waitKey(0)
'''

#cv2.imshow("1",th3)
#cv2.waitKey(0)
start = -1;
end = -1;
count = 0;
# loai bo duong ke ngoai (neu co)
th3 = th3[0:th3.shape[0],5:th3.shape[1]-5]
#cv2.imwrite("aaaaa.jpg",th3)
for i in range(0,th3.shape[0]):
    isBlack = -1;
    for j in range(0,th3.shape[1]):
        if(th3[i][j]==0):
            isBlack = 1;
            break;
    #print isBlack
    if(start == -1 and isBlack == 1):
       # print "......................."
        start = i;
        count = 1;
    if(count > 500 and isBlack == -1):
        #print "sao vay"
        end = i;
    if(start != -1 and end != -1):
        #print "da vao"
        #temp = imgOrign[start-3:end+3,0:th3.shape[1]]
        #cv2.imshow("a",temp)
        #cv2.imwrite("imgAfterProcessing.jpg",temp)
        #cv2.waitKey(0)
        print "Ket thuc"
        break;
    if(isBlack == -1):#hang trang
        start = -1
        count = 0;
    if(count > 0):
        count += 1;
    print str(start) + " - " + str(end)
   
  #  print count
left = -1;
right = -1;
count = 0;
for i in range(0,th3.shape[1]):
    isBlack = -1
    for j in range(start,end):
        if(th3[j][i]==0):
            isBlack = 1;
            if count > 0:
                count += 1;
            break;
    if(left == -1 and isBlack == 1):
        count = 1;
        left = i;
    if(left != -1 and isBlack == -1):
        right = i;
    if(left != -1 and right != -1 and count > 10):
        temp = imgOrign[start-3:end+3,left-3:right+3]
#        temp = imgOrign[start-3:end+3,left-3:right+10]
#        temp = imgOrign[start-10:end+3,left-10:right+10]
        cv2.imwrite("imgAfterProcessing.jpg",temp)
        break;
    if (isBlack == -1):
        count = 0;
        left = -1;
        right = -1;


    
    


