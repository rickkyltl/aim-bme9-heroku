from flask import Flask, request
import requests
from pythainlp import word_tokenize, pos_tag
import speech_recognition as sr

text = "hello world"
app = Flask(__name__)
@app.route('/')
def index():
  return text

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST','GET','DELETE'])
def callback():
  audio = request.files['file']
  r = sr.Recognizer()
  with sr.WavFile(audio) as source:
    try:
      audio = r.listen(source)
      text = r.recognize_google(audio,language = "th-TH")
      print("You said " + text) # แสดงข้อความจากเสียงด้วย Google Speech Recognition และกำหนดค่าภาษาเป็นภาษาไทย
    except sr.UnknownValueError:# ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
      text = "no word"
    return text

if __name__=="__main__":
    app.run()

