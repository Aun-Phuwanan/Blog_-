import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while 1:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0,42,82])
    upper_blue = np.array([24,255,255])


    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for c in contours:
            if cv2.contourArea(c) <=500 :
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 188,255), 1)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == 27:
        break
