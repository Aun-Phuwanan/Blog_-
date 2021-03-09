### สัปดาห์ 5 ธ.ค 7, 2020 ถึง ธ.ค 9, 2020  
## (โก้)  
### module Brain  
เริ่มสร้าง module Brain ใน Node-red และสร้าง Subflow ในส่วนของ module Brain Subflow สามารถสร้างได้โดยไปที่ palette แล้วกดที่ Add Subflow และสร้างตาม State Diagram ที่ออกแบบไว้  
![image](https://user-images.githubusercontent.com/65691345/110538414-9b715b00-8156-11eb-8933-607736833def.png)  


### Subflow Brian_INIT  
สร้าง Subflow Brian_INIT ใน Module Brian สร้างขึ้นมาเพื่อในตั้งค่าเริ่มต้นที่จำเป็น เช่น Global.state สถานะเริ่มต้นจำเป็นต้องเป็น 0 ถ้าไม่เป็น 0 การทำงานก็จะสามารถข้ามไป State อื่น 
โดยที่ไม่รอฟงคำสั่ง msg.payload จะเป็นการส่งค่าที่ได้รับผ่าน mqtt status ไปเก็บไว้ใน ALL_INIT global.backed/listening/text จะเป็นการกำหนดต่าเริ่มต้นให้กับ text ให้ตอนแรกเป็นค่าว่างเปล่า 
global.T_1 เป็นการกำหนดเวลาเริ่มต้นให้เป็น 0 โดยที่คำส่งกำหนดค่าเริ่มต้นพวกนี้จะใช้ node ที่มีชื่อว่า change  
![image](https://user-images.githubusercontent.com/65691345/110538461-a62bf000-8156-11eb-926d-01240ee1f2ee.png)  


## (อั๋น) 
### Subflow Listening 1  
ได้เริ่มทำในส่วนของ Subflow Listening 1 ใน Module Brian  
![image](https://user-images.githubusercontent.com/65691345/110538506-b217b200-8156-11eb-8206-b7630de14038.png)  



### Speech recognition  
ในส่วนของเสียงได้เปลี่ยนจาก Library Pyaudio เป็น Speech recognition อีกครั้ง ต้องการลองปรับแก้ให้การจับเสียงให้ดีขึ้นและได้ปรับแก้ในส่วนของการเล่นไฟล์เสียง เปลี่ยนจากการใช้คำสั่ง Command-line 
เป็น Library Pyaudio เนื่องจาก Library Pyaudio สามารถเล่นไฟล์เสียงที่ทำการดัดโดย Library SOX  
![image](https://user-images.githubusercontent.com/65691345/110538545-bb088380-8156-11eb-87f5-efbfcc4e237f.png)  


### MQTT  
ติดตั้ง MQTT Mosquitto และเขียนโค้ดให้สามารถ Publish และ Subscribe เพื่อควบคุม Dynamixel  

