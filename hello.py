from flask import Flask, request
import requests
from pythainlp import word_tokenize, pos_tag
text = "hello world"
app = Flask(__name__)
@app.route('/')
def index():
  return text

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST','GET','DELETE'])
def callback():
  message = request.form.get("data")
  #text = message+"finish"
  proc = word_tokenize(message, engine = 'newmm')
  tag = pos_tag(proc,engine='old')
  index() 
  return message

if __name__=="__main__":
    app.run()

