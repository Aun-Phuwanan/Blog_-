import cv2
import numpy as np


cap = cv2.VideoCapture(0)
faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml') #นำไฟล์ Classsifier ที่ใช้ในการตัดสินใจ ว่าภาพนั้นมีหน้าคนหรือไม่
while 1:
    ret,frame = cap.read()
    faces = faces_cascade.detectMultiScale(frame,1.3,5) #นำ frame เข้าไปประมวณผลและถ้าตรงกับ Classsifier จะทำการคืนค่าตำแหน่งหน้สกลับมา
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,189,0),2) #วาดรูปสี่เหลี่ยมบนตำแหน่งของหน้า
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == 27:
        break
