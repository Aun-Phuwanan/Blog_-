# FOBI คืออะไร
 FOBI คือหุ่นยนต์ที่ปฏิสัมพันธ์กับมนุษย์ได้ สามารถรับคำสั่งเสียงภาษาไทยกับมนุษย์ได้  
 และยังสามารถเชื่อต่อกับอุปกรณ์ IOT 
 
 # [System Architecture](https://github.com/5A681/Blog_-/blob/main/Architechure.md)
 ![System Architecture](https://user-images.githubusercontent.com/46487715/110239521-e1bd9300-7f79-11eb-9537-cebca6c4992a.png)
 # [System Overview](https://github.com/5A681/Blog_-/blob/main/README.md)
 ![System Overview](https://user-images.githubusercontent.com/46487715/109979637-ae88c300-7d31-11eb-89a2-efba68d0a19a.png) 
 # OpenCV
  เราจะใช้ OpenCV ในการใช้งานสำหรับการมองเห็นของ FOBI
  โดย เราจะทำการ ตรวจจับใบหน้าและสีผิว เพื่อระบุว่าสิ่งที่มองเห็นเป็นคนหรือไม่
  ### การติดตั้ง OpenCV
   ใน Raspberry pi นั้น เราจะใช้คำสั่ง sudo apt-get install opencv-python3 สำหรับใช้กับ python3
   และใช้ haarcascades จาก https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
   เพื่อใช้ในการตรวจจับใบหน้า ในส่วนของสีผิวเราจะแปลงสีผิว HSV ให้เป็นขาว เพื่อในการตรวจจับ
   โค้ดตัวอย่าง https://github.com/5A681/Blog_-/blob/main/FOBI_File/Eye.py
   
     