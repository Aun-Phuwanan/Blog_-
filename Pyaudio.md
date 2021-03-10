# Pyaudio
ศึกษาเกี่ยวกับ Library ที่ใช้บันทึกไฟล์เสียงจากการพูดและได้เลือกใช้ Library PyAudio เพื่อเอาเสียงพูดบันทึกเป็นไฟล์เสียง (.wav)
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

จากตัวอย่างจะเห็นได้ว่าได้ทำการทดลองบันทึกเสียง 5 วินาที บันทึกเป็นไฟล์ output.wav หากต้องการมากกว่า 5 วิ สามารถปรับได้ที่ 
RECORD_SECONDS 
  
# ทำจับเสียงพูด

เพื่อจะใช้การจับเสียงพูดแท่นการตั้งเวลาในการอัดเสียง โดยใช้ Library numpy ในการคำนวณหาค่าสูงสุดเพื่อหาค่าของเลเวลของเสียงแล้วนำมาใช้ในการจับเสียงพูด

```python
import math, numpy as np

data = stream.read(CHUNK, exception_on_overflow=False)
data_conv  = np.fromstring(data, dtype=np.int16)
max = np.max(data_conv)     
frames.append(data)

```

