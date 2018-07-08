from flask import Flask, request
import requests
text = "hello world"
app = Flask(__name__)
@app.route('/')
def index():
  return text

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST','GET','DELETE'])
def callback():
  #message = request.get()
  #text = message+"finish"
  index() 
  return 'finish'

if __name__=="__main__":
    app.run()

