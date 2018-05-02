from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

import cv2

clf = joblib.load('./model/digits_clf.pkl')
print '=> Clasificatorul a fost incarcat'

#im = cv2.imread('./image/digit-reco.jpg')
im = cv2.imread('./image/37.png')
#shin add

height = im.shape[0]
width = im.shape[1]
print("\n Resizing Image........")
im = cv2.resize(im, dsize =(200, int(200*height/width)), interpolation = cv2.INTER_AREA)



im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_gray = cv2.GaussianBlur(im_gray, ksize=(5, 5), sigmaX=0)

cv2.imshow("Final classification", im_gray)
cv2.waitKey()

#ret, image_threshold = cv2.threshold(im_gray, 91, 255, cv2.THRESH_BINARY_INV)
image_threshold = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)

cv2.imshow("Final classification", image_threshold)
cv2.waitKey()

temp, contours, hierarchy = cv2.findContours(image_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
        result_CNT.append(cnt);
#        contours.remove(cnt)

        
'''

'''
rectangles = [cv2.boundingRect(ctr) for ctr in result_CNT]
for rect in rectangles:
    print "shin co dep choai"
    print rect
    # Desenare dreptunghi
    cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
    leng = int(rect[3])# * 1.5)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    print "ohyeh"
    print int(rect[3])
    print int(rect[2])
    print int(rect[1])
    print int(rect[0])
    print "hha"
    print pt1;
    print pt2;
    print leng
    cv2.imshow("ahuhu", im)
    cv2.waitKey()
#    region_of_interest = image_threshold[pt1:pt1 + leng, pt2:pt2 + leng]
    region_of_interest = image_threshold[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
    cv2.imshow("Final classification", region_of_interest)
    cv2.waitKey()
    roi = cv2.resize(region_of_interest, (28, 28), interpolation=cv2.INTER_AREA)
    roi = cv2.dilate(roi, (3, 3))
 
    fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    nbr = clf.predict(np.array([fd], 'float64'))
    print "nhandien: " + str(nbr[0])
    
#cv2.imshow("Final classification", im)
#cv2.waitKey()
