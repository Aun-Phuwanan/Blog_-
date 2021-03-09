# สัปดาห์ 7 ธ.ค 21, 2020 ถึง ธ.ค 29, 2020  
## (อั๋น)  
# printer  
ในส่วนของการพูดนั้นได้เปลี่ยน Library มาใช้ pyaudio เหมือนเดิมเนื่องจากเสียงที่จับได้บ้างและจับไม่ได้บ้างทำให้เกินปัญหาและได้อัดเสียงเพื่อใช้ในการเล่นไฟล์เสียงในการถามตอบและได้เพิ่มคำสั่งถ่ายรูป  
![image](https://user-images.githubusercontent.com/65691345/110540532-2fdcbd00-8159-11eb-9c04-f1a5e6045837.png)  


### Speech recognition  
ในส่วนของเสียงได้เปลี่ยนจาก Library Speech recognition เป็น Library Pyaudio อีกครั้ง เพราะว่าเมื่อเลิกพูดแต่มีเสียงแค่นิดเดียวก็จะยังจับเสียงต่อไม่บันทึกไฟล์เสียงให้แต่ Library Pyaudio 
สามารถปรับแต่งอะไรได้ง่ายกว่า Library Speech recognition และเปลี่ยนจากการใช้ Library Pyaudio เป็นคำสั่ง Command-line เหมือนเดิมเนื่องจากคำสั่ง Command-line สั้นละเรียกใช้สะดวกกว่า Library Pyaudio  
![image](https://user-images.githubusercontent.com/65691345/110540674-5c90d480-8159-11eb-9891-2b3ec163ac48.png)



ทดสอบ MQTT จาก Node-red ส่งไปที่ printer  

![image](https://user-images.githubusercontent.com/65691345/110540563-39febb80-8159-11eb-9c98-c039a0e380ae.png)  

## (โก้)  
# Module Motor  
ได้เริ่มทำในส่วนของ Module Motor ได้ทำการ Publish/Subscribe ของ Module Motor  
![image](https://user-images.githubusercontent.com/65691345/110540704-64507900-8159-11eb-9f42-d062cddc763d.png)


