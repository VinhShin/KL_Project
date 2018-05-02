"""
import cv2
import numpy as np
import glob
import itertools
import xlsxwriter

folder="./*.png"
files = list(glob.glob (folder))
imgs = []
for i in files:
    abc=cv2.imread(i,0)
    d=(16,16)
    abc1=cv2.resize(abc,d,interpolation=cv2.INTER_AREA)
    r,c=abc1.shape
    width, height = abc1.shape
    arr = np.ravel(abc1)
    imgs.append(arr) 

cv2.imwrite("trainData.png",imgs)
"""
import cv2
import numpy
import glob
import os

def getImage(dir_):
    dir = "./"+dir_+"/"# current directory
    ext = ".png" # whatever extension you want

    pathname = os.path.join(dir, "*" + ext)
    images = [cv2.imread(img) for img in glob.glob(pathname)]
    print "len " + str(len(images))
    return images

images = []
for i in range(0,10):
    print "i " + str(i)
    images.extend(getImage(str(i)))


for i in range(0,len(images)):
    d=(56,28)
    images[i]=cv2.resize(images[i],d,interpolation=cv2.INTER_AREA)
#height = sum(image.shape[0] for image in images)
#width = max(image.shape[1] for image in images)
height = 28 * 4
width = 56 * 9
output = numpy.zeros((height,width,3))

y = 0
x = 0
i = 0

print "000000000000000000"
print width, height
for image in images:

    
    i += 1
    h,w,d = image.shape
    print "ssss"
    print y+h
    print x+w
    output[y:y+h,x:x+w] = image
    x += w

    if i > 8 :
        i = 0
        x = 0
        y += h
    
cv2.imwrite("test.png", output)
