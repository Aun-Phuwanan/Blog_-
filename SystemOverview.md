![System Overview](https://user-images.githubusercontent.com/46487715/109979637-ae88c300-7d31-11eb-89a2-efba68d0a19a.png) 
# Raspberry Pi ตัวที่ 1   
### ทำหน้าที่ Run Node-red และควบคุม Hardware ที่ประกอบไปด้วย Microphone,Speaker,Camera และ servo  
### Microphone
Saramonic Blink 500 B1 Digital Camera-Mount Wireless Omni Lavalier Microphone System
![Microphone](https://user-images.githubusercontent.com/46487715/110540059-99100080-8158-11eb-997d-2acbfc5e8ee9.jpg)  
 **Features**

- Dual Channel Transmitter

- Built in rechargeable lithium battery

- Working distance: 30m (with obstacle)

- Carrier Frequency: 2.4GHz

- Signal to noise ratio: ≥70dB

- Reference audio input: -30~42dBv(MIC input, 0dB attenuation)

- Frequency response: 20Hz~16kHz

- Distortion: ≤0.1%

- Voice delay：≤6ms
### Speaker  
### Camera
Raspberry Pi Camera V2 (8MP)
![pica](https://user-images.githubusercontent.com/46487715/110543451-eaba8a00-815c-11eb-85f1-d68f00ee2ef2.jpg)
**Specification**

- Sensor: Sony IMX219
- Sensor Resolution: 32480 x 2464 (8 megapixels)
- Sensor Image Area: 3.69 x 2.81 mm
- Pixel Size: 1.12um x 1.12um
- Optical Size: 1/4”
- Video:Dimension: 25mm x 23mm x 9mm / 0.98” x 0.90” x 0.35”
- 1920 x 1080 (1080p), 30 fps
- 1280 x 720 (720p), 60 fps
- 640 x 480 (480p), 90 fps
 
Weight: (Camera board + attached cable): 3.4g
### Servo  
dynamixel ax-12A
![Dynamixel](https://user-images.githubusercontent.com/46487715/110541907-f7d67980-815a-11eb-9746-f65368126baa.jpeg)  
**Specifications**
- Baud Rate	7843 bps ~ 1 Mbps
- Weight	53.5g(AX-12, AX-12+), 54.6g(AX-12A)
- Dimensions (W x H x D)	32mm x 50mm x 40mm 1.26 X 1.97 X 1.57 [inch]
- Resolution	0.29 [°]
- Running Degree	0 [°] ~ 300 [°]
- Endless Turn
- Motor	Cored
- Gear Ratio	254 : 1
- Stall Torque	1.5 N*m (at 12V, 1.5A)
- No Load Speed	59rpm (at 12V)
- Operating Temperature	-5 [°C] ~ +70 [°C]
- Input Voltage	9.0 ~ 12.0V (Recommended : 11.1V)
- Command Signal	Digital Packet
- Protocol Type	Half Duplex Asynchronous Serial Communication
- (8bit, 1stop, No Parity)
- Physical Connection	TTL Level Multi Drop Bus
- ID	254 ID (0~253)
- Feedback	Position, Temperature, Load, Input Voltage, etc
- Gear Material	Engineering Plastic(Full)
- Case Material	Engineering Plastic(Front, Middle, Back)
# Node-red
## ประกอบไปด้วย Module ดังนี้  
### 1.Brain ทำหน้าที่ในการควบคุมสถานะต่างๆของ FOBI ให้เป็นลำดับขั้นตอน  
### 2.Motor ทำหน้าที่ในการควบคุมการหมุนของ Servo  
### 3.Listenin ทำหน้าที่ในการฟังคำสั่งหรือคำพูดต่างๆของมนุษย์  
### 4.ALL_INIT ทำหน้าที่เก็บค่าเริ่มต้นต่างๆไว้  

# Raspberry Pi ตัวที่ 2  
### ทำหน้าที่ ควบคุม LED และ Printer



# การทำงานของ Brain  
 การทำงานของ Brain นั้น เราได้ทำเป็น Diagram ดังนี้  
 ![Brain](https://user-images.githubusercontent.com/46487715/110239785-547b3e00-7f7b-11eb-8561-b4a6c58fd64d.PNG)
 การทำงานของ State Diagram มีดังนี้  
   1.เมื่อ FOBI เริ่มทำงาน จะทำได้แค่เพียงมองไปมาหรือมองตามคนเท่านั้นจะไม่สามารถพูดได้ จนกว่าจะได้รับคำสั่งให้เริ่มทำงาน  
   2.เมื่อ FOBI ได้รับคำสั่งเริ่มทำงาน  FOBI จะสวัสดี และถ้ามีคนอยู่โดยที่ FOBI มองเห็น จะไปยัง State ของ Listening  
   3.เมื่ออยู่ใน State ของ Listening แล้วจะรอฟังคำสั่งต่างๆจาก User  
   4.ถ้า User ไม่พูดเกินกว่าเวลาที่กำหนด  FOBI จะถามคำถาม  
   5.ถ้า User พูดแต่คำเดิมซ้ำๆ FOBI จะแสดงกริยาท่าทางว่ารำคาญ  
   6.ถ้ามองไม่เห็นหน้าของ User เป็นเวลา 10 วินาทีแล้วกลับมาเห็นอีกครั้งFOBIจะสวัสดีอีกครั้ง
 ### การทำงานใน Node-red
 ![brain](https://user-images.githubusercontent.com/46487715/110452421-beb8ed80-80f7-11eb-9e95-6e54d220d2a6.png) 

# การทำงานของ Motor
 จะคอยรับคำสั่งจาก backend Eye โดยตรง เพื่อทำการหมุนโดยทันที่เมื่อเห็นคนโดยไม่มีเงื่อนไขใดๆ  
 แต่ถ้า backend Eye มองไม่เห็น ก็จะได้รับคำสั่งจาก Brain แทนในการหมุนเพื่อมองหาคน  
 
 # การทำงานใน Node-red
 ![Motor](https://user-images.githubusercontent.com/46487715/110451874-376b7a00-80f7-11eb-8f99-8a60b0a7e5c8.png)
 
 โค้ดการทำงานของ Motor https://github.com/5A681/Blog_-/blob/main/FOBI_File/FobiDynamixel.py

# การทำงานของ Listening  
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
