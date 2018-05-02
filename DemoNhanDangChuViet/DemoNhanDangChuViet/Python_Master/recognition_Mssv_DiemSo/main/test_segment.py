import cv2

img = cv2.imread('105.png')
height = img.shape[0]
width = img.shape[1]
img = cv2.resize(img, dsize =(150, int(150*height/width)), interpolation = cv2.INTER_AREA)
(h, w) = img.shape[:2]
image_size = h*w
mser = cv2.MSER_create()
mser.setMaxArea(image_size/2)
mser.setMinArea(10)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting to GrayScale
_, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("aa",bw)
cv2.waitKey(0)
regions, rects = mser.detectRegions(bw)

# With the rects you can e.g. crop the letters
for (x, y, w, h) in rects:
    cv2.rectangle(img, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
    cv2.imshow("aa",img)
    cv2.waitKey(0)

cv2.imshow("aa",img)
cv2.waitKey(0)
    
