# สัปดาห์ 10 ม.ค 25, 2020 ถึง ม.ค 29, 2020  
## (โก้)  
### Face & Skin Detection และ Dynamixel  
ใช้ Node-red เพื่อควบคุม module Motor,Brain ด้วย MQTT ในตอนนี้เราจะนำ Node-red เข้ามา เพื่อให้สามารถแก้ไขState การทำงานได้ง่ายขึ้น เพียงแค่การลากเส้นเป็นลำดับขั้นการทำงานเท่านั้น 
โดยปกติแล้วเราจะสั่งงานผ่าน Backend แค่อย่างเดียว ในตอนนี้เราจึงเขียน backend เพื่อรับคำสั่งจาก Fronted ให้แก้ไขได้ง่ายขึ้น  
![image](https://user-images.githubusercontent.com/65691345/110542441-9cf15200-815b-11eb-9aeb-b17ff27c5bc9.png)  

ตัวอย่าง  
![image](https://user-images.githubusercontent.com/65691345/110542507-b4c8d600-815b-11eb-8ae5-3421a50efd86.png)  



## (อั๋น)
### Module Brian  
แก้ในส่วนของ module brian เห็นหน้าแล้วไม่มีเสียงทักทายเพิ่มในส่วนการส่งข้อมูลไปที่ talk เพื่อให้มีการทักทายเมื่อเจอหน้า จากข้างบน ตอนนี้เราแค่สร้าง node MQTT Publish 
ขึ้นมาและส่งคำขอไปยัง Talking Module ก็จะสามารถพูดคำต่างๆตาม ID  
![image](https://user-images.githubusercontent.com/65691345/110542296-7501ee80-815b-11eb-8dba-6dc1da2c078e.png)  
![image](https://user-images.githubusercontent.com/65691345/110542317-7a5f3900-815b-11eb-81d0-55ef02e5ed11.png)  



ตัวอย่าง  
![image](https://user-images.githubusercontent.com/65691345/110542379-8ba84580-815b-11eb-908d-60e93fd507de.png)  
