import cv2 as cv
import numpy as np

img = cv.imread("D:\Pictures\RedBall.jpg")

cv.imshow('CAT', img)


# Translation [Shifting an Image X and Y axis up-down-left-right]

def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)


# -x --> left  +x -> Right
# -y _--> up   -y --> Down

# Rotation
def rotating(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (height, width)
    return cv.warpAffine(img, rotMat, dimensions)


#Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("RESIZED",resized)

translated = translate(img, 50, 50)
cv.imshow("Translated", translated)

rotated = rotating(img, 45)
# negative angle gives clock wise rotation
cv.imshow("ROTATED", rotated)


cv.waitKey(0)
#