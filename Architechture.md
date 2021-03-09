# System Architechture
![System Architecture](https://user-images.githubusercontent.com/46487715/110530814-73312e80-814d-11eb-8921-5c0c2cb3b4b4.png)
## User Layer  
 ### ประกอบด้วย 1.Talking 2.Face  
## Hardware Layer
 ### ประกอบด้วย 1.Camera 2.Microphone 3.Speaker 4.Servo 5.LED 6.Printer  
## Service Layer  
 ### ประกอบด้วย Google Service  
## Controller Layer  
 ### ประกอบด้วย 1.Brain 2.Listening 3.Motor 4.Question
 
 # การทำงาน  
 - เมื่อ user พูด Microphone จะได้รับเสียงแล้วส่งไปยัง Service Google Cloud Speech เพื่อแปลงเสียงเป็นข้อความแล้วนำไปประมวณผลที่ Controller Listening Module ถ้าได้รับคำสั่งให้เป็นการพูดก็จะส่งต่อไปยัง speakerและกลับไปหา user
 - เมื่อ user พูด Microphone จะได้รับเสียงแล้วส่งไปยัง Service Google Cloud Speech เพื่อแปลงเสียงเป็นข้อความแล้วนำไปประมวณผลที่ Controller Listening Module ถ้าได้รับคำสั่งให้เป็นการแสดงผลหลอด LED ก็จะทำการแสดงผลเป็น ไฟและกลับไปหาuser ที่เป็นผู้มองเห็น
 - เมื่อ user พูด Microphone จะได้รับเสียงแล้วส่งไปยัง Service Google Cloud Speech เพื่อแปลงเสียงเป็นข้อความแล้วนำไปประมวณผลที่ Controller Listening Module ถ้าได้รับคำสั่งเป็นการถ่ายรูป เมื่อถ่ายรูปเสร็จก็จะปริ้นรูปภาพ โดยแดสงผลกลับไปหา user
 - เมื่อ camera เจอ user ก็จะส่งตำแหน่งไปยังControler Motor Module แล้วก็จะส่งไปยัง servo เพื่อหมุนตาม user

