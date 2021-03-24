# Speech recognition  
## การติดตั้ง Speech recognition  
ใน Raspberry pi นั้น เราจะใช้คำสั่ง pip install SpeechRecognition สำหรับใช้กับ python3  
![image](https://user-images.githubusercontent.com/65691345/112327883-62a1bc00-8ce8-11eb-82c7-a2f82ef02931.png)  

## Audio File to Text


**ตัวอย่าง**
```python
import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile("output.wav") as source:   
    audio = r.record(source)
try:    
    text = r.recognize_google(audio)
    print(text)

except Exception as e:
    print(e)
```
