# OpenCV
### การติดตั้ง OpenCV
   ใน Raspberry pi นั้น เราจะใช้คำสั่ง sudo apt-get install opencv-python3 สำหรับใช้กับ python3
   และใช้ haarcascades จาก https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
   เพื่อใช้ในการตรวจจับใบหน้า ในส่วนของสีผิวเราจะแปลงสีผิว HSV ให้เป็นขาว เพื่อในการตรวจจับ
   โค้ดตัวอย่าง https://github.com/5A681/Blog_-/blob/main/FOBI_File/Eye.py
