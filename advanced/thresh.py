'''Thresholding is a technique in image processing used to convert a grayscale image 
into a binary image by applying a threshold value. Pixels with intensity values above 
or below the threshold are set to a specific value (typically black or white).'''

import cv2 as cv

img = cv.imread('photos/cat2.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # threshold value = 150
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # threshold value = 150
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding

'''Adaptive thresholding divides the image into small regions and calculates 
the threshold for each region based on the local properties 
(e.g., mean or Gaussian-weighted sum of pixel intensities in that region).'''

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)