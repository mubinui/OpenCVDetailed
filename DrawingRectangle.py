import cv2 as cv
import numpy as np

blank = np.zeros((600, 600, 3), dtype='uint8')
blank[:] = 255, 255, 255
# cv.imshow("WHITEBOARD", blank)
# Drawing a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[1]//2), (0, 255, 0), thickness=cv.FILLED)
# cv.rectangle(img_name, (x0, y0), (x1, y1), (r, g, b), thickness = 2/filed/-1)
cv.imshow ('RECTANGLE', blank)
cv.waitKey(0)
