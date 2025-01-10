import cv2 as cv

img = cv.imread('photos/cat2.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125,175) # put blur instead of img
cv.imshow('Canny Edges', canny)

# Dilating the image 
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resizes', resized)

# Cropping
cropped = img[100:200, 200:300]
cv.imshow('Cropped', cropped)
cv.waitKey(0)