import os
from PIL import Image
from flask import Flask, request, abort, jsonify, send_from_directory


UPLOAD_DIRECTORY = "/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


api = Flask(__name__)

@api.route("/send", methods=["POST"])
def home():
    img = Image.open(request.files['file'])
    img = img.save("img.jpg") 
    myCmd = os.popen('python3 testImage.py').read()
    return myCmd


if __name__ == "__main__":
    api.run(debug=True, port=8000)