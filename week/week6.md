# สัปดาห์ 6 ธ.ค 14, 2020 ถึง ธ.ค 18, 2020  
## (อั๋น)  
### Module Listening  
ได้เริ่มทำในส่วนของ Module Listening ได้ทำการ Publish/Subscribe ของ Module Listening  
![image](https://user-images.githubusercontent.com/65691345/110539872-5b12dc80-8158-11eb-8cc9-c27fbbba6a2c.png)  


## (โก้)  
### Module ALL_INIT  
ในส่วนของ Module ALL_INIT จะเป็นการเก็บข้อมูลไว้ ชนิดของGlobal   
![image](https://user-images.githubusercontent.com/65691345/110539926-6d8d1600-8158-11eb-8843-0dcb7f9372cb.png)


### Open CV  
เขียนโค้ดเพื่อตรวจจับใบหน้าบุคคลและสีผิวและส่งข้อมูลผ่าน MQTT Mosquitto เพื่อใช้ควบคุม Dynamixel จากภาพด้านล่าง ตอนนี้เราจะแยกการทำงานออกเป็นคนละ Module 
การส่งตำแหน่งของหน้าบุคคล จะใช้ MQTT เป็นตัวสื่อสารระหว่าง Module  
![image](https://user-images.githubusercontent.com/65691345/110539978-7f6eb900-8158-11eb-854c-cc5240caab7d.png)  



### Subflow Brian_say  
สร้าง Subflow Brian_say ใน Module Brian  
![image](https://user-images.githubusercontent.com/65691345/110540040-944b4c80-8158-11eb-9f55-443c2c409c9f.png)  


### Subflow Brian_looking  
สร้าง Subflow Brian_looking ใน Module Brian  
![image](https://user-images.githubusercontent.com/65691345/110540082-a1683b80-8158-11eb-9c88-6499cb531f07.png)  



