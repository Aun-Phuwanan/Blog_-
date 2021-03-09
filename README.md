# Raspberry Pi ตัวที่ 1   
### ทำหน้าที่ Run Node-red และควบคุม Hardware,Microphone,Speaker,Camera และ servo  

# Node-red
## ประกอบไปด้วย Module ดังนี้  
### 1.Brain ทำหน้าที่ในการควบคุมสถานะต่างๆของ FOBI ให้เป็นลำดับขั้นตอน  
### 2.Motor ทำหน้าที่ในการควบคุมการหมุนของ Servo  
### 3.Listenin ทำหน้าที่ในการฟังคำสั่งหรือคำพูดต่างๆของมนุษย์  
### 4.ALL_INIT ทำหน้าที่เก็บค่าเริ่มต้นต่างๆไว้  

# Raspberry Pi ตัวที่ 2  
### ทำหน้าที่ ควบคุมสถานะต่างๆของ FOBI  


# การทำงานของ Brain  
 การทำงานของ Brain นั้น เราได้ทำเป็น Diagram ดังนี้  
 ![Brain](https://user-images.githubusercontent.com/46487715/110239785-547b3e00-7f7b-11eb-8561-b4a6c58fd64d.PNG)
 การทำงานของ State Diagram มีดังนี้  
 1.เมื่อ FOBI เริ่มทำงาน จะทำได้แค่เพียงมองไปมาหรือมองตามคนเท่านั้นจะไม่สามารถพูดได้ จนกว่าจะได้รับคำสั่งให้เริ่มทำงาน
 2.เมื่อ FOBI ได้รับคำสั่งเริ่มทำงาน  FOBI จะสวัสดี และถ้ามีคนอยู่โดยที่ FOBI มองเห็น จะไปยัง State ของ Listening
 3.เมื่ออยู่ใน State ของ Listening แล้วจะรอฟังคำสั่งต่างๆจาก User
 4.ถ้า User ไม่พูดเกินกว่าเวลาที่กำหนด  FOBI จะถามคำถาม
 5.ถ้า User พูดแต่คำเดิมซ้ำๆ FOBI จะแสดงกริยาท่าทางว่ารำคาญ
 ### การทำงานใน Node-red
 ![brain](https://user-images.githubusercontent.com/46487715/110452421-beb8ed80-80f7-11eb-9e95-6e54d220d2a6.png) 

# การทำงานของ Motor
 จะคอยรับคำสั่งจาก backend Eye โดยตรง เพื่อทำการหมุนโดยทันที่เมื่อเห็นคนโดยไม่มีเงื่อนไขใดๆ  
 แต่ถ้า backend Eye มองไม่เห็น ก็จะได้รับคำสั่งจาก Brain แทนในการหมุนเพื่อมองหาคน  
 
 # การทำงานใน Node-red
 ![Motor](https://user-images.githubusercontent.com/46487715/110451874-376b7a00-80f7-11eb-8f99-8a60b0a7e5c8.png)
 
 โค้ดการทำงานของ Motor https://github.com/5A681/Blog_-/blob/main/FOBI_File/FobiDynamixel.py

# การทำงานของ Listening  
  Listening จะคอยรับข้อความจาก backend/listening/text เพื่อมาคัดแยกข้อความว่าเป็นข้อความชนิดใดเมื่อคัดแยกข้อความเสร็จแล้วถึงจะส่งไปให้ Module Brain 
  
ลิงค์ตัวอย่างการทำงานของ FOBI   
 https://drive.google.com/file/d/1U_sY8gIvmVyEVGUNKW4nwyWe5BRMISXs/view?usp=sharing
