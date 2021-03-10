# Node-red  
# วิธีการติดตั้ง Node-red  
ก่อนอื่นต้องทำการติดตั้ง NodeJS ก่อน โดยการพิมพ์คำสั่ง curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -  
ต่อด้วยคำสั่ง sudo apt install nodejs 
เมื่อเราติดตั้งเสร็จ ลองตรวจสอบเวอร์ชัน  
![node](https://user-images.githubusercontent.com/46487715/110566262-5d8a2c00-8182-11eb-9d2d-ea32286b6392.png)  
ต่อมาใช้คำสั่งในการติดตั้ง Node-red ใช้คำสั่ง npm install -g --unsafe-perm node-red  
เมื่อเราติดตั้งเสร็จแล้ว ลอง Run ดู  
![run](https://user-images.githubusercontent.com/46487715/110566654-ee610780-8182-11eb-89ea-d571698c955e.png)  
แล้วลองเบิด browser ดู โดยใช้ Localhost:1880  
![Runnode](https://user-images.githubusercontent.com/46487715/110566909-426bec00-8183-11eb-930f-bd115b08e656.png)  
ลองสร้างsubflow สำหรับใช้งานใน brain  
![subflow](https://user-images.githubusercontent.com/46487715/110567167-aa223700-8183-11eb-94cf-865c00ded5e6.png)  
แล้วลองสร้าง brain state
![brain](https://user-images.githubusercontent.com/46487715/110452421-beb8ed80-80f7-11eb-9e95-6e54d220d2a6.png)  
แล้วลองสร้าง Module ต่างๆ
### motor
![motor](https://user-images.githubusercontent.com/46487715/110451874-376b7a00-80f7-11eb-8f99-8a60b0a7e5c8.png)  

### ALL_INIT  
![motor](https://user-images.githubusercontent.com/65691345/110539337-b1cbe680-8157-11eb-9397-7d1fc0b79bc9.png)  

### Listening  
![talk](https://user-images.githubusercontent.com/46487715/110457692-7dc3d780-80fd-11eb-96b5-d3f30aae8b80.png) 
