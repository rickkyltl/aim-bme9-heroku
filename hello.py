from flask import Flask, request
import requests
text = "hello world"
app = Flask(__name__)
@app.route('/')
def index(text):
  return text

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST'])
def callback():
  message = request.get()
  index(message+"finish") 
  return '',200

if __name__=="__main__":
    app.run()

