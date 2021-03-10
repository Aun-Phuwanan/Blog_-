# สัปดาห์ 7 ธ.ค 21, 2020 ถึง ธ.ค 29, 2020  
## (อั๋น)  
# printer  
ได้เพิ่มคำสั่งในการถ่ายรูปโดยใช้คำสั่งเสียงในการสั่ง ได้ทดสอบ MQTT จาก Node-red ส่งไปที่ printer  
![image](https://user-images.githubusercontent.com/65691345/110540563-39febb80-8159-11eb-9c98-c039a0e380ae.png)  

ตัวอย่าง 
```python
import os
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    client.subscribe("module/camera/request")

def on_message(client,userdata,msg):
    message = msg.payload.decode('utf-8')
    if msg.topic == "module/camera/request":
        cmd = "python ther_pnter.py"
        os.system(cmd)
    


client = mqtt.Client()
client.username_pw_set("username",password="hcilab")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.137.188",1883,60)
client.loop_forever()
client.disconnect()
```


### Pyaudio  
ในส่วนนี้ได้เพิ่มโค้ดเข้ามาใหม่ เพื่อจะใช้การจับเสียงพูดแท่นการตั้งเวลาในการอัดเสียง โดยใช้ Library numpy ในการคำนวณหาค่าสูงสุดเพื่อหาค่าของเลเวลของเสียงแล้วนำมาใช้ในการจับเสียงพูด
```python

import math, numpy as np

data = stream.read(CHUNK, exception_on_overflow=False)
data_conv  = np.fromstring(data, dtype=np.int16)
max = np.max(data_conv)     
frames.append(data)
```




## (โก้)  
# Module Motor  
ได้เริ่มทำในส่วนของ Module Motor ได้ทำการ Publish/Subscribe ของ Module Motor  
![image](https://user-images.githubusercontent.com/65691345/110540704-64507900-8159-11eb-9f42-d062cddc763d.png)


