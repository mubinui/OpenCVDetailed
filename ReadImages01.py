import cv2 as cv

# imread() for reading the image
img = cv.imread('D:\Pictures\cat.jpg')
img01 = cv.imread("D:\Pictures\large_cat.jpg") # Need to rescale
cv.imshow('Cat', img)
# imshow() takes the name and image matrix parameter
cv.waitKey(0)
