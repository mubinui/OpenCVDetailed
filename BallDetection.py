import cv2 as cv
capture = cv.VideoCapture(0)
tracker = cv.TrackerCSRT_create()
success, img = capture.read()
boundbox = cv.selectROI("RED BALL TRACKER",img,False)
tracker.init(img,boundbox)
def draw(img,boundbox):
    X,Y,Z,H= int(boundbox[0]),int(boundbox[1]),int(boundbox[2]),int(boundbox[3])
    cv.rectangle(img,(X,Y),((X+Z),(Y+H)),(0,225,0),3,1)
    cv.putText(img, 'Tracker',(75,50),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
while True:
    time = cv.getTickCount()
    success, img = capture.read()

    success,boundbox = tracker.update(img)
    print(boundbox)
    if success:
        draw(img,boundbox)
    fps = cv.getTickFrequency()/(cv.getTickCount()-time)
    cv.putText(img,str(int(fps)),(75,400), cv.FONT_HERSHEY_SIMPLEX,0.7, (0, 0,255), 2)
    cv.imshow("Tracking ball", img)

    if cv.waitKey(1) & 0xff == ord('q'):
        break