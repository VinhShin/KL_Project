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
for i in range(0,11):
    print "i " + str(i)
    images.extend(getImage(str(i)))


for i in range(0,len(images)):
    d=(20,20)
    images[i]=cv2.resize(images[i],d,interpolation=cv2.INTER_AREA)
#height = sum(image.shape[0] for image in images)
#width = max(image.shape[1] for image in images)
height = 20 * 40
width = 20 * 50
output = numpy.zeros((height,width,3))

y = 0
x = 0
i = 0

print "000000000000000000"
print len(images)
print width, height
for image in images:

    
    i += 1
    h,w,d = image.shape

    output[y:y+h,x:x+w] = image
    #cv2.imshow("ss",output)
    #cv2.waitKey(0)
    x += w

    if i > 49 :
        i = 0
        x = 0
        y += h
    
cv2.imwrite("MSSV_Train.png", output)
