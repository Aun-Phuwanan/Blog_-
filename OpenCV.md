# OpenCV
## การติดตั้ง OpenCV
   ใน Raspberry pi นั้น เราจะใช้คำสั่ง sudo apt-get install opencv-python3 สำหรับใช้กับ python3  
   ![opencv](https://user-images.githubusercontent.com/46487715/110500618-fa6daa80-812b-11eb-9609-9f23f039b1d3.png)  
   ในกรณีนี้ผมได้ติดตั้งเอาไว้แล้ว ถ้าติดตั้งเอาไว้แล้วมันจะขึ้น version บอก อย่างในกรณีนี้คือ Version 4.2
## การทำ Skin Detection  
 ### ขั้นตอนที่ 1
   เราจะทำการหาค่า hsv_min และ hsv_max เพื่อหาค่าสีของสีผิวและในตอนนี้เราก็จะใช้ OpenCV ที่เราได้ติดตั้งไว้มาใช้งาน และในกรณีนี้  
   เราจะใช้ Trackbar เพื่อให้งายในการหาค่าสีผิวตามโค้ดตัวอย่าง  
   ![Trackbฟr](https://user-images.githubusercontent.com/46487715/110504429-bd0b1c00-812f-11eb-9a09-dd4bea416998.png)  
   **บรรทัดที่ 4** หน้าwindowของ Trackbar และจะต้องใส่ชื่อของ window นั้นด้วย   
   **บรรัดที่ 7-12** จะเป็นการสร้าง Trackbar ทั้งหมด 6 Trackbar paramete ที่ต้องใส่คือ ชื่อ Trackbar,window,ค่าต่ำสุด,ค่าสูงสุด  
    และฟังก์ชันที่ต้องการเรียกเมื่อค่าเปลี่ยน  
   **บรรทัดที่ 14** เป็นการเปิดการใช้งาน camera ตัวที่ 0(ตัวแรก)   
   **บรรทัดที่ 18** เป็นการรับภาพที่ได้ไปเก็บไว้ในตัวแปร frame  
   **บรรทัดที่ 19** เป็นการแปลงสีภาพจาก BGR เป็น hsv ภาพที่ถูกแปลงสีเก็บไว้ที่ตัวแปร hsv  
   **บรรทัดที่ 20-25** จะเป็นการนำค่า min และ max ที่ได้จากการเปลี่ยน ไปเก็บไว้ในตัวแปร min,max ของhsv  
   **บรรทัดที่ 27** นำค่า hsv_minไปเก็บไว้ในตัวแปรอาเรย์ lower  
   **บรรทัดที่ 28** นำค่า hsv_maxไปเก็บไว้ในตัวแปรอาเรย์ upper  
   **บรรทัดที่ 29** นำภาพ hsv เทียบค่าสี lowerและupper ไปเก็บไว้ในตัวแป รmask  
   **บรรทัดที่ 31** เป็นการแสดงภาพปกติ  
   **บรรทัดที่ 31** เป็นการแสดงภาพที่ผ่านการแปลงสี  
   
   โปรแกรมจะ Loop ไปจนกว่า key จะเท่ากับ 27 หรือกด esc  
   #### ตัวอย่างที่ทำได้
   ![Skin](https://user-images.githubusercontent.com/46487715/110509831-1f1a5000-8135-11eb-915d-988ab59b03c4.png)  
   
   และใช้ haarcascades จาก https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
   
