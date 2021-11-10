import cv2 as cv
import numpy as np

img = cv.imread("D:\Pictures\RedBall.jpg")
cv.imshow('Cats', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#Sobal
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("Sobal",combined_sobel)
#Canny
canny = cv.Canny(gray, 125, 175)
cv.imshow("CANNY",canny)
cv.waitKey(0)