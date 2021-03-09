# OpenCV
## การติดตั้ง OpenCV
   ใน Raspberry pi นั้น เราจะใช้คำสั่ง sudo apt-get install opencv-python3 สำหรับใช้กับ python3  
   ![opencv](https://user-images.githubusercontent.com/46487715/110500618-fa6daa80-812b-11eb-9609-9f23f039b1d3.png)  
   ในกรณีนี้ผมได้ติดตั้งเอาไว้แล้ว ถ้าติดตั้งเอาไว้แล้วมันจะขึ้น version บอก อย่างในกรณีนี้คือ Version 4.2
## การทำ Skin Detection  
 ### ขั้นตอนที่ 1
   เราจะทำการหาค่า hsv_min และ hsv_max เพื่อหาค่าสีของสีผิวและในตอนนี้เราก็จะใช้ OpenCV ที่เราได้ติดตั้งไว้มาใช้งาน และในกรณีนี้เราจะใช้ Trackbar เพื่อให้งายในการหาค่าสีผิว  
   
   และใช้ haarcascades จาก https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
   
