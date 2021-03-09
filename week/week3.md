# สัปดาห์ที่ 3  
## (อั๋น)  
### Speech recognition  

เปลี่ยน Libarry บันทึกเสียงพูดเป็นไฟล์เปลี่ยนจาก Library PyAudio เป็น Library Speech recognition เนื่องจากว่า Library 
นี้สามารถแปลงเป็นไฟล์เสียงและสามารถจับเสียงพูดได้และมีการแปลงจากเสียงเป็นข้อความโดยใช้ Service Google Cloud Speech ทำงานโดยบันทึกเป็นไฟล์เสียง (.wav) 
ของเสียงที่พูดส่งไฟล์เสียงไปแปลงที่ Google Cloud Speech ส่งข้อความที่แปลงได้กลับมาและเล่นไฟล์เสียงที่เก็บไว้ในเครื่อง โดยใช้ Library playsound ในการเล่นไฟล์เสียงที่เก็บไว้  
![image](https://user-images.githubusercontent.com/65691345/110537117-d96d7f80-8154-11eb-955b-804681db1181.png)  


### SOX  
ได้เริ่มใช้ Library ดัดเสียงพูดจากไฟล์เสียงได้เลือกใช้ Library SOX และการอัดเสียงได้เลือกใช้ Library PyAudio ในการอัดเสียง  
![image](https://user-images.githubusercontent.com/65691345/110537081-ceb2ea80-8154-11eb-9c93-c0cb78f23c79.png)  


## (โก้)  
### OpenCV  
ในส่วนของ OpenCV ปรับให้เฟรมเรทของกล้องใน Raspberry pi ให้ได้อยู่ที่30เฟรม ก่อนหน้านี้ได้เฟรมเรทเฉลี่ยที่15เฟรมเรท จากการปรับความละเอียดลดลงครึ่งนึงจะทำให้ได้เฟรมเรทที่ดีขึ้น 
คำสั่งที่ใช้คือ cv2.set(3,width),cv2.set(3,height) โดยศึกษาจาก OpenCV  
![image](https://user-images.githubusercontent.com/65691345/110537206-f43ff400-8154-11eb-8682-05af035cafcf.png)




