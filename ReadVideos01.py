import cv2 as cv

# reading video
capture = cv.VideoCapture("D:\Videos\Genda Phool.mp4")
# here 0 for default webcam /we can provide the path too
# We need to read the video farme to frame
# So we use while loop
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
