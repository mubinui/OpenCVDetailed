import cv2 as cv
import numpy as np

whiteboard = np.zeros((400, 600, 3), dtype='uint8')
whiteboard[:] = 0, 255, 0
# drawing a line
# cv.line(whiteboard, (0, 0), (600, 400), (255, 0, 0), thickness= 5)
# cv.line(whiteboard, (0,400), (600, 0), (255, 0, 0), thickness=5)
cv.circle(whiteboard, (300, 200), 100, (0, 0, 255), thickness=cv.FILLED)
# cv.circle(whiteboard, (center_x, center_y), radius, (b, g, r), thickness=2)
# Drawing a text
cv.putText(whiteboard, 'Bangladesh', (200,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
# cv.putText(img_name, 'my_text', (x,y), (cv.FONT...), Scaling =1.0, (0, 255, 0), thickness=2)
cv.imshow("CIRCLE", whiteboard)
cv.waitKey(0)

