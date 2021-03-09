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
brain จะทำหน้าที่คอยรับค่าจาก backend หรือ ค่าที่อยู่ใน ALL_INIT เพื่อนำค่าต่างๆมาใช้ในการตัดสินใจ  
เช่น การได้รับค่าจาก backend Eye มาเพื่อตัดสินใจเมื่อมีคน และได้รับคำสั่งก็จะทำงานตามคำสั่งที่ได้รับ  
ในทางกลับกัน backend Eye มองไม่เห็น ก็จะไม่ทำตามคำสั่ง

# การทำงานของ Motor
 จะคอยรับคำสั่งจาก backend Eye โดยตรง เพื่อทำการหมุนโดยทันที่เมื่อเห็นคนโดยไม่มีเงื่อนไขใดๆ  
 แต่ถ้า backend Eye มองไม่เห็น ก็จะได้รับคำสั่งจาก Brain แทนในการหมุนเพื่อมองหาคน  
 โค้ดการทำงานของ Motor https://github.com/5A681/Blog_-/blob/main/FOBI_File/FobiDynamixel.py

# การทำงานของ Listening  
  Listening จะคอยรับคำสั่งจากมนุษย์และจะแปลงไฟล์เสียงเป็นไฟล์ Text เพื่อส่งไปให้ Brain ตัดสินใจในการทำงาน
  โค้ดการทำงานของ Listening https://github.com/5A681/Blog_-/blob/main/FOBI_File/Listening.py
  
ลิงค์ตัวอย่างการทำงานของ FOBI   
 https://drive.google.com/file/d/1U_sY8gIvmVyEVGUNKW4nwyWe5BRMISXs/view?usp=sharing
