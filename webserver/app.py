import os
from PIL import Image
from flask import Flask, request, abort, jsonify, send_from_directory


UPLOAD_DIRECTORY = "/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


api = Flask(__name__)


@api.route("/")
def list_files():
    return "heyo"


@api.route("/send", methods=["POST"])
def home():
    img = Image.open(request.files['file'])
    img = img.save("img.jpg") 
    myCmd = os.popen('python3 testImage.py').read()
    return myCmd


if __name__ == "__main__":
    api.run(debug=True, port=8000)

"""
from flask import Flask
app = Flask(__name__)
from flask import request
import base64
import os


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/req')
def say_hello():
  
  filter = request.args.get('filter', default = '*', type = str)
  data = base64.b64decode(filter)
  print(filter)
  file = open('img.jpg', 'w')
  file.write(data)
  file.close()

  myCmd = os.popen('python3 testImage.py').read()
  return myCmd
"""

