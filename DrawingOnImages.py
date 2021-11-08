import cv2 as cv
import numpy as np


# blank image
# Here 3 is the numbers of color channel
blank = np.zeros((500, 500,3), dtype='uint8')
# For white image
# blank[:] = 255, 255, 255
# blank[:] = 0, 255, 0 [b,g,r]
blank[:] = 0, 0, 255


cv.imshow("BLANK", blank)

# Not blank
img = cv.imread('D:\Pictures\cat.jpg')
# Color code matrix
cv.imshow('CAT', img)
cv.waitKey(0)

