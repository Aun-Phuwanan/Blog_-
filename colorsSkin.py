import cv2
import numpy as np

cv2.namedWindow('Track')
def track(x):
    print(x)
cv2.createTrackbar('h min','Track',0,179,track)
cv2.createTrackbar('h max','Track',0,179,track)
cv2.createTrackbar('s min','Track',0,255,track)
cv2.createTrackbar('s max','Track',0,255,track)
cv2.createTrackbar('v min','Track',0,255,track)
cv2.createTrackbar('v max','Track',0,255,track)

cap = cv2.VideoCapture(0)


while 1:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('h min','Track')
    h_max = cv2.getTrackbarPos('h max','Track')
    s_min = cv2.getTrackbarPos('s min','Track')
    s_max = cv2.getTrackbarPos('s max','Track')
    v_min = cv2.getTrackbarPos('v min','Track')
    v_max = cv2.getTrackbarPos('v max','Track')

    lower_blue = np.array([h_min,s_min,v_min])
    upper_blue = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == 27:
        break
