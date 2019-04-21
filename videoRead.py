import cv2

cap = cv2.VideoCapture('videoName')
#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
#tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerTLD_create()
#tracker = cv2.TrackerMedianFlow_create()

# Get tracker name
tracker_name = str(tracker).split()[0][1:]

# init i counter
i = 0

# Start from specific frame
while(i<725):
    ret, frame = cap.read()
    i=i+1
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)


while(cap.isOpened()):
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int, roi))
    if success:
        p1 = (x,y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
    else:
        cv2.putText(frame, "Failure to Detect Tracking!!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)
    # Display tracker type on frame
    cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3)
    cv2.imshow(tracker_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()