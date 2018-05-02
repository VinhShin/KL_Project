
import numpy as np
import cv2


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
cv2.imwrite('contours1.png',erosion)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('contours2.png',imgray)

#ret,thresh = cv2.threshold(imgray,127,255,0)
ret2,thresh = cv2.threshold(imgray,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('contours3.png',thresh)
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
'''
x, y, width, height = cv2.boundingRect(diemchu_col)
ps_dc = x + (width/2) # vi tri x nay la cua diem chu
print ps_dc
x, y, width, height = cv2.boundingRect(diemso_col)
ps_ds =  x + (width/2)
x, y, width, height = cv2.boundingRect(massv_col)
ps_mssv = x + (width/2)
'''

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
for cnt in contours:
    print i;
#    img = cv2.drawContours(img, [cnt], 0, (0,255,0),3)
    x, y, width, height = cv2.boundingRect(cnt)
    #add vào list điểm chữ

    if(x < ps_dc and x+width > ps_dc):
        img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
        list_dc.append(i);
        print "day la o diem chu" + str(index)
   
    #add vào list điểm số
    elif(x < ps_ds and x+width > ps_ds):
        img = cv2.drawContours(img, [cnt], 0, (255,0,0), 3)
        list_ds.append(i);
        print "day la o diem so" + str(index)
    #add vào list mssv
    elif(x < ps_mssv and x+width > ps_mssv):
        img = cv2.drawContours(img, [cnt], 0, (0,0,255), 3)
        list_mssv.append(i);
        print "day la o mssv" + str(index)
    #------------cat hinh-------------
    #roi = imgOrigan[y+2:y+height, x+5:x+width]
    #http://answers.opencv.org/question/29260/how-to-save-a-rectangular-roi/
    #cv2.imwrite("./chu_tach/roi"+str(i)+".png", roi)
    #---------------------------------
    i=i+1
    #show_wait_destroy("ohyeh",img)
    
cv2.imwrite('bangdiem_contours.png',img)
print list_dc
#cat diem chu

for item in list_dc:
    x, y, width, height = cv2.boundingRect(contours[item])
    roi = imgOrigan[y:y+height, x:x+width]
    cv2.imwrite("./catchu/dc/"+str(item)+".png", roi)
    #nguon: http://answers.opencv.org/question/29260/how-to-save-a-rectangular-roi/
#cat diem so
for item in list_ds:
    x, y, width, height = cv2.boundingRect(contours[item])
    roi = imgOrigan[y:y+height, x:x+width]
    cv2.imwrite("./catchu/ds/"+str(item)+".png", roi)
    #nguon: http://answers.opencv.org/question/29260/how-to-save-a-rectangular-roi/
#cat ma so sinh vien
for item in list_mssv:
    x, y, width, height = cv2.boundingRect(contours[item])
    roi = imgOrigan[y:y+height, x:x+width]
    cv2.imwrite("./catchu/mssv/"+str(item)+".png", roi)
    #nguon: http://answers.opencv.org/question/29260/how-to-save-a-rectangular-roi/

#img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
#show_wait_destroy("ohyeh",img)
#cells = [np.hsplit(row,100) for row in np.vsplit(img, 50)]


"""
import cv2
import numpy as np

img = cv2.imread('temp.png')
ret,thresh = cv2.threshold(img,127,255,0)

temp, contours,hierarchy = cv2.findContours(thresh, 1, 2)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imwrite('contours.png',img)
"""
