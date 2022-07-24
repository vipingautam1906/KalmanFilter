from kalmanfilter import KalmanFilter
import cv2
kf = KalmanFilter()

img = cv2.imread('blue_background.webp')
ball_Current = [(100,100), (250,100), (300,100), (350,100), (400,100), (450,100), (500,100), (550,100), (600,100), (650,100)]



for point in ball_Current:
    cv2.circle(img, point, 10, (0,0,255),-1)
    # predictions made by kalman filter..based on previous points...
    # then we show these..
    # we see after a while they converges or go closer to true values..
    predict = kf.predict(point[0],point[1])
    cv2.circle(img,predict,10, (10,150,255),-1)

for i in range(10):
    predict = kf.predict(predict[0], predict[1])
    cv2.circle(img,predict,10,(20,220,0),4)

cv2.imshow("img",img)
cv2.waitKey(0)