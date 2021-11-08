import cv2 as cv


# Lets create a function for re-scaling the image
def reScaleFrame(frame, scale=0.10):
    width = int(frame.shape[1]*scale*2)
    height = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("D:\Pictures\large_cat.jpg")
# cv.imshow('Cat',img)


frame_resized = reScaleFrame(img)
cv.imshow("Cat",frame_resized)
cv.waitKey(0)

