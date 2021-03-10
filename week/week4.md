# สัปดาห์ 4 พ.ย 30, 2020 ถึง ธ.ค 4, 2020  
## (อั๋น)  

### Play Command-line   
จากตัวอย่างโค้ดด้านล่างได้เปลี่ยนจาก Library Playsound เป็นการใช้คำสั่ง Command-line เล่นไฟล์เสียงแท่น Library Playsound ไม่สามารถเปิดไฟล์เสียงที่แปลงโดย Library SOX และเหตุผลที่ไม่เลือกใช้ Library Pyaduio เพราะการเรียกใช้งานแบบการใช้คำสั่ง Command-line สะดวกกว่าการเรียกใช้ Library pyaudio  
  
ตัวอย่าง  
```python
import os

cmd = "Play {}".format("Hello.wav")
os.system(cmd)
```



### PyAudio  
การอัดเสียงได้เปลี่ยนจาก Library Speech recognition เป็น Library PyAudio เนื่องจากบางครั้งเสียงที่จับได้บ้างไม่ได้บ้าง ในส่วนของการแปลงเป็นข้อความยังใช้ในส่วนของ
Library Speech recognition
![image](https://user-images.githubusercontent.com/65691345/110537707-9eb81700-8155-11eb-8d81-9962b958ed4c.png)  

ตัวอย่าง  
```python
import pyaudio
import wave
import os
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
text = ""

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")
r = sr.Recognizer()
with sr.AudioFile("output.wav") as source:   
audio = r.record(source)
try:    
    text = r.recognize_google(audio)

except Exception as e:
     print("bb")

if text == "สวัสดี":
    cmd = "Play {}".format(Hello.wav)
    os.system(cmd)

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
```
จากโค้ดตัวอย่างจะเห็นว่า Library pyaudio เป็นตัวบันทึกไฟล์เสียง 5 วินาที และ Library Speech recognition แปลงไฟล์เสียงเป็นข้อความถ้าสิ่งที่พูดเป็นคำว่า **"สวัสดี"** 
ก็จะเข้าเงื่อนไขและมีการเล่นไฟล์เสียง Hello.wav ผ่านคำสั่ง Command-line โดยใช้ Library OS ในการเรียกใช้งาน 

## (โก้)  
### State diagram  
State Diagram นี้จะทำงานอยู่ภายใต้ Brian Module ของ Node-red โดยการทำงานของState Diagram นี้ คือ เมื่อ FOBI ไม่ได้รับคำสั่งใดๆ FOBI จะแค่ฟัง (Listening) และแค่มองตามคนเพียงแค่นั้น (Looking) 
โดยจะสลับทำอยู่แค่ 2 State นี้แค่นั้น แต่ถ้าเมื่อไรได้รับคำสังเริ่มการทำงานจากเสียงคน FOBI จะทักทายคนในทันทีแล้วจะไปมองหาคน ถ้าไม่เจอหรือคนหลุดไปจะทำการมองหาคนไปเรื่อยๆและถ้าเจอคนโดยเวลาผ่านไป 10 วินาที 
FOBI จะทักทายอีกครั้งแล้วจะเข้าสู่ State การทำงานที่รอฟังเพื่อทำงานต่างๆตามคำสั่ง แต่ถ้าคนหลุดออกจากการมองเห็นของ FOBI ในช่วงนี้ FOBI ก็จะกลับไปมองหาคน แต่ถ้าไม่หลุด 
FOBI จะยังทำงานรอฟังเสียงคำสั่งจากคน แต่ถ้าเจอคนอยู่แต่ไม่พูดเกิน 15 วินาที โฟบี้ก็จะเริ่มถามคำถาม(Question)เพื่อให้คนตอบ เมื่อถามเสร็จก็จะรอฟังคำตอบ (Listening) 
และเมื่อได้รับคำตอบจะทำการเฉลย (Answer) แล้วก็รอฟังคำสั่งต่อไป แต่ถ้าคนพูดแต่อย่างเดิมซ้ำๆ จะทำให้ FOBI รำคานและพูดในเชิงรำคานออกมา(annoyed) นอกจากนี้คำสั่งที่เหลือก็จะเป็น เปิดไฟ-ปิดไฟ 
เปลี่ยนสีไฟ และเล่นเพลงจากไฟล์เพลงที่มีอยู่  
![image](https://user-images.githubusercontent.com/65691345/110537813-c7401100-8155-11eb-938d-34a39db5450e.png)



