import cv2 as cv

img = cv.imread("D:\Pictures\RedBall.jpg")
cv.imshow('CAT', img)

# # Converting image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# # blurring an image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# # blurring scale here (7,7) we can put higher or lower
# cv.imshow("Blurred", img)
# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edge', canny)
# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# we can increase iterations and the dilated
cv.imshow("Dilated", dilated)
# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)
# Resize
# resized = cv.resize(img, (500, 500))
resized =  cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# interpolation = cv.INTER_AREA/INTER_CUBIC/INTER_LINEAR
cv.imshow('Resized', resized)
# Cropping an Image
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
