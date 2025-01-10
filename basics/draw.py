import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the img a certain color
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=2)
cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=cv.FILLED) #thickness=-1

cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('circle', blank)


# 4. Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,250,0), thickness=2)
cv.imshow('text', blank)
cv.waitKey(0)

