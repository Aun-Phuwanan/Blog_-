#  สัปดาห์ 3 พ.ย 23, 2020 ถึง พ.ย 27, 2020  
## (อั๋น)  
### Speech recognition  

เปลี่ยน Libarry บันทึกเสียงพูดเปลี่ยนจาก Library PyAudio เป็น Library Speech recognition เนื่องจากว่า Library 
นี้สามารถแปลงเป็นไฟล์เสียงและสามารถจับเสียงพูดได้และมีการแปลงจากเสียงเป็นข้อความโดยใช้ Service Google Cloud Speech ทำงานโดยบันทึกเป็นไฟล์เสียง (.wav) 
ของเสียงที่พูดส่งไฟล์เสียงไปแปลงที่ Google Cloud Speech ส่งข้อความที่แปลงได้กลับมาและเล่นไฟล์เสียงที่เก็บไว้ในเครื่อง โดยใช้ Library playsound ในการเล่นไฟล์เสียงที่เก็บไว้  
![image](https://user-images.githubusercontent.com/65691345/110537117-d96d7f80-8154-11eb-955b-804681db1181.png)  
  
ตัวอย่าง  
![image](https://user-images.githubusercontent.com/65691345/110551543-48a09f00-8168-11eb-9e3c-03120d6f5e3c.png)  
จากโค้ดตัวอย่าง Library Speech recognition สามารถจับเสียงพูดได้และแปลงเป็นข้อความได้เลย โดยที่ไม่ต้องโหลด Library ตัวอื่นมาเพิ่ม 
จากโค้ดตัวอย่างเสียงที่พูดยังได้แค่ภาษาอังกฤษเท่านั้นแต่เราสามารถเปลี่ยนเป็นภาษาไทยได้ โดยไปที่โฟลเดอร์ที่เก็บ Library/speech_recognition/__init__.py หาฟังชั่น recognize_google() แก้ที่ตัวแปลชื่อ language= "en-US" สามารถเปลี่ยนเป็น language= th-TH" ก็จะสามารถแปลงข้อความจากไฟล์เสียงที่เป็นภาษาไทยได้  

![image](https://user-images.githubusercontent.com/65691345/110552590-3889bf00-816a-11eb-8c24-e768e66f7b0b.png)  
  
### playsound  
จากตัวอย่างโค้ด Library playsound ด่านล่าง เหตุผลที่เลือกใช้ Library ตัวนี้แท่น Library pyaudio เพราะว่าโค๊ดสั้นสามารถใช้เล่นเสียงได้โดยแค่โค้ดไม่กี่บรรทัด  
  
ตัวอย่าง  
![image](https://user-images.githubusercontent.com/65691345/110554171-d41c2f00-816c-11eb-8b49-40b166d2aede.png)  



### SOX  
ได้เริ่มใช้ Library ดัดเสียงพูดจากไฟล์เสียงได้เลือกใช้ Library SOX และการอัดเสียงได้เลือกใช้ Library PyAudio ในการอัดเสียง  
![image](https://user-images.githubusercontent.com/65691345/110537081-ceb2ea80-8154-11eb-9c93-c0cb78f23c79.png)  


## (โก้)  
### OpenCV  
ในส่วนของ OpenCV ปรับให้เฟรมเรทของกล้องใน Raspberry pi ให้ได้อยู่ที่30เฟรม ก่อนหน้านี้ได้เฟรมเรทเฉลี่ยที่15เฟรมเรท จากการปรับความละเอียดลดลงครึ่งนึงจะทำให้ได้เฟรมเรทที่ดีขึ้น 
คำสั่งที่ใช้คือ cv2.set(3,width),cv2.set(3,height) โดยศึกษาจาก OpenCV  
![image](https://user-images.githubusercontent.com/65691345/110537206-f43ff400-8154-11eb-8682-05af035cafcf.png)




