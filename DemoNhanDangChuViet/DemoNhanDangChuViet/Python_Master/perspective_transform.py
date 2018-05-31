from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import sys

#image = cv2.imread("./bangdiem/bangdiem19.png")
#imageOrigan = cv2.imread("./bangdiem/bangdiem19.png")
print sys.argv
print "..............................Tiến hành điều chỉnh biên ảnh..........."
image = cv2.imread(sys.argv[1])
imageOrigan = cv2.imread(sys.argv[1])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200)

#cv2.imshow("test",edged)
#cv2.waitKey(0)

#edged = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
#                                cv2.THRESH_BINARY, 3, -2)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
docCnt = None

if len(cnts) > 0:
 # săp xếp các contour tìm được
 # theo thứ tự lớn tới bé
 cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
 # loop over the sorted contours
 for c in cnts:
  # approximate contour
  peri = cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, 0.02 * peri, True)
  # nếu approximated contour lớn hơn 4 điểm
  # thì nó chính là 4 góc của bài trắc nghiệm
  if len(approx) == 4:
      docCnt = approx
      image = cv2.drawContours(image, [docCnt], 0, (0,255,0), 3)
      #break
#paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(imageOrigan, docCnt.reshape(4, 2))
'''
cv2.imshow("test",image)
cv2.waitKey(0)
cv2.imshow("test",gray)
cv2.waitKey(0)
'''
cv2.imwrite("bangdiem_reshape.png",warped);
