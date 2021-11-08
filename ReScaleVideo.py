import cv2 as cv


# Re-formatting video
def re_scale_frame(frame, scale=0.10):
    width = int(frame.shape[1] * scale * 2)
    height = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("D:\Videos\Genda Phool.mp4")
while True:
    isTrue, frame = capture.read()
    re_scale = re_scale_frame(frame)
    cv.imshow("Video", re_scale)
    # Frame wise showing
    # Quiting condition
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
        # When q is pressed the video will disappear

capture.release()
cv.destroyAllWindows()
