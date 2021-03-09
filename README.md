# FOBI คืออะไร
 FOBI คือหุ่นยนต์ที่ปฏิสัมพันธ์กับมนุษย์ได้ สามารถรับคำสั่งเสียงภาษาไทยกับมนุษย์ได้และยังสามารถเชื่อต่อกับอุปกรณ์ IoT โดยคุณสมบัติของ FOBI มีดังนี้  
 - พูดตอบโต้กับคนได้
 - หันหน้าตามคนได้
 - เล่นมุกตลกได้
 - ควบคุมอุปกรณ์ IoT ได้
 # การออกแบบและพัฒนาระบบ
 # [System Architecture](https://github.com/5A681/Blog_-/blob/main/Architechture.md)
 
 # [System Overview](https://github.com/5A681/Blog_-/blob/main/SystemOverview.md)
 
 # ขั้นตอนการพัฒนาระบบ
 # OpenCV
  เราจะใช้ OpenCV ในการใช้งานสำหรับการมองเห็นของ FOBI
  โดย เราจะทำการ ตรวจจับใบหน้าและสีผิว เพื่อระบุว่าสิ่งที่มองเห็นเป็นคนหรือไม่
  ### การติดตั้ง OpenCV
   ใน Raspberry pi นั้น เราจะใช้คำสั่ง sudo apt-get install opencv-python3 สำหรับใช้กับ python3
   และใช้ haarcascades จาก https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
   เพื่อใช้ในการตรวจจับใบหน้า ในส่วนของสีผิวเราจะแปลงสีผิว HSV ให้เป็นขาว เพื่อในการตรวจจับ
   โค้ดตัวอย่าง https://github.com/5A681/Blog_-/blob/main/FOBI_File/Eye.py
   
   # ผลของการพัฒนาระบบ
   
     
