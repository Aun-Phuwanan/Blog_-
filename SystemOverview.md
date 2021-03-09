![System Overview](https://user-images.githubusercontent.com/46487715/109979637-ae88c300-7d31-11eb-89a2-efba68d0a19a.png) 
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
  1.Listening จะคอยรับข้อความจาก backend/listening/text เมื่อมีการส่งข้อมูลมาที่ Module Listening 
  2.จะมีการเช็คว่าเจอหน้าหรือไม่ ถ้าเจอจะทำขั้นตอนต่อไปแต่ถ้าไม่เจอข้อความที่ส่งมาจะหายและไม่มีการทำขั้นตอนต่อไป
  3. ทุกครั้งที่มีการพูดและผ่านเงื่อนไขเช็คสถานะ FOBI จะมีการ Set ค่า check_talk มีค่าเท่ากับ 1 โดย Set ไว้เป็นค่า Global
  4. ฟังชั่นมีการสับข้อความออกมาเป็นข้อความที่เรา Set ไว้ 
  5. ค้นหาคำสั่งเสร็จส่วนที่หนึ่ง จะมีการตรวจข้อความที่สับไว้ว่ามีคำสั่งที่เป็นคำสั่งเปิดไฟหรือไม่ถ้ามีจะไปที่ฟังก์ชั่นและทำการค้นหาสีว่ามีการพูดถึงสีอะไรบ้างเมื่อค้นหารเสร็จจะทำการส่งข้อความไปที่ Module Brain แต่ถ้าไม่มีคำสั่งเปิดไฟจะส่งไปข้อความไปที่ Module Brain จะไม่มีการเข้าไปที่ฟังก์ชั่น
  6. เมื่อมีการค้นหานคำสั่งเสร็จส่วนที่สอง จะมีการ Set ค่า payload เป็น 2 และจะมีการ set สถานะฟังและ Set สถานะ FOBI เท่ากับ msg.payload และส่งข้อความไปที่ status 
   
  
   ### การทำงานใน Node-red
  ![Listening](https://user-images.githubusercontent.com/46487715/110457692-7dc3d780-80fd-11eb-96b5-d3f30aae8b80.png)
  
ลิงค์ตัวอย่างการทำงานของ FOBI   
 https://drive.google.com/file/d/1U_sY8gIvmVyEVGUNKW4nwyWe5BRMISXs/view?usp=sharing
