import cv2
cv2.namedWindow("output", cv2.WINDOW_NORMAL)

from kalmanfilter import KalmanFilter
from orange_detector import OrangeDetector

cap = cv2.VideoCapture('orange.mp4')

kf = KalmanFilter()
od = OrangeDetector()

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    x, y, x2, y2 = od.detect(frame)
    cx = int((x+x2)/2)
    cy = int((y+y2)/2)

    predictions = kf.predict(cx, cy)
    cv2.circle(frame, (cx, cy), 20, (255, 0, 0), -1)
    cv2.circle(frame, (predictions[0], predictions[1]), 20, (0, 0, 255), 4)
    cv2.circle(frame, (predictions[0], predictions[1]), 20, (0, 0, 255), 4)
    cv2.imshow("output",frame)
    key = cv2.waitKey(100)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()