import cv2 as cv
import numpy as np


lower_red = np.array([0, 150, 150])
upper_red = np.array([10, 255, 255])

# Capturing webcam footage
webcam_video = cv.VideoCapture(0)

while True:
    success, video = webcam_video.read()

    img = cv.cvtColor(video, cv.COLOR_BGR2HSV)

    mask = cv.inRange(img, lower_red, upper_red)

    mask_contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Finding contours in mask image


    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv.contourArea(mask_contour) > 500:
                x, y, w, h = cv.boundingRect(mask_contour)
                cv.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle

    cv.imshow("mask image", mask) # Displaying mask image

    cv.imshow("window", video) # Displaying webcam image

    cv.waitKey(1)