# สัปดาห์ 1 พ.ย 9, 2020 ถึง พ.ย 13, 2020  
### Dynamixel
ได้เริ่มศึกษา Dynamixel AX-12+ ได้ใช้ Library pyax12 ในภาษา python และได้ลง OS Rasberry pi ได้ศึกษา Dynamixel AX-12+ แต่ละคำสั่งบน Library pyax12 และศึกษา U2D2 ใช้ร่วมกับ Dynamixel AX-12+ หลังจากได้เล่นไท่กี่วัน พี่ที่แล็ปให้เปลี่ยนตัว Library ของ Dytnamixel จาก Library pyax12 เป็น Libarry DynamixelSDK เนื่องจากครั้งก่อนพี่เขาบอกว่าเจอปัญหา Document ของตัว Libarry DynamixelSDK มีให้อ่านเยอะมาก   
![Dynamicxel](https://user-images.githubusercontent.com/65691345/110531681-72e56300-814e-11eb-90ae-605311880719.jpg)  
![Raspberrypi](https://user-images.githubusercontent.com/65691345/110531684-737df980-814e-11eb-9c4c-1402dca0e141.jpg)  
![U2D2](https://user-images.githubusercontent.com/65691345/110531668-6f51dc00-814e-11eb-8d1e-13e9499c181f.PNG)  
### OpenCV
ในส่วนของ OpenCV จะมีฮาร์ดแวร์แค่กล้องตัวเดียว  
![Camera](https://user-images.githubusercontent.com/65691345/110531680-724ccc80-814e-11eb-821e-cec329755c4c.jpg)

โดยการมองเห็นของ FOBI เราจะใช้ Python-OpenCV Library ในการทำโดยจาก OpenCV และ data จาก haarcascades โดยการทำงานจะมีการถ่ายรูปและเมื่อได้รูปเสร็จเราจะนำไฟล์ภาพนั้น ไปเข้าประมวณผลว่ามีค่าใกล้เคียงกับหน้าบุคคลหรือไม่ โดยคำสั่งตัวอย่างจะมีดังนี้  

1. image = cv2.imread(imagePath) คำสั่งนี้จะเป็นการอ่านภาพเข้ามาแล้วเก็บไว้ยังตัวแปร image  
2. faceCascade = cv2.CascadeClassifier(cascPath) คำสั่งนี้จะเป็นการนำ weight ที่ใช้ในการเทียบหน้าบุคคลเข้ามาเก็บไว้ในตัวแปร faceCascade  
3. faces = faceCascade.detectMultiScale(image,faceCascade)  
4. คำสั่งนี้จะเป็นการเปรียบเทียบว่าภาพที่เรานำเข้าไป(image)และ data ที่ใช้เทียบ(faceCascade)  
5. ถ้าเป็นหน้าบุคคลจะคือค่าตำแหน่งเป็น parameter 4 ตัว คือ x,y,widht และ height แต่ถ้าไม่เจอจะไม่มีการคืนค่าใดๆ  
 
จากนั้นเราก็สามารถนำตำแหน่งที่เราได้รับไปใช้ในการทำงานต่างๆของระบบเราได้แล้ว  
![System](https://user-images.githubusercontent.com/65691345/110531683-737df980-814e-11eb-86c2-42a6d7be38ed.PNG)
