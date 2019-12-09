<<<<<<< HEAD
# from picamera import PiCamera
# from time import sleep
import os

'''
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('picture.jpg')
camera.stop_preview()
'''


'''
    This file is not run on the Raspberry Pi but rather another device, e.g. a laptop
    Demonstrates how the Raspberry Pi can be told remotely to take a photo and then
    process the taken photo through the neural network, determining its material
    Should then return result back to the user e.g. at the laptop
'''


# Part 1: Take a photo and save as 'image.jpg'
print("[!!!] Taking Photo . . .")
# os.system("raspistill -o image.jpg")
os.system("curl http://128.197.136.204:8000/takePhoto")
print("[~~~] Photo Taken ")

# Part 2.1: Send the image over a curl request to receive results from ML
# print("[!!!] Sending photo to web server . . .")
# os.system("curl -F 'file=image.jpg' http://128.197.180.252:8000/send")

# Part 2.2: Instead of sending an image, tell server to grab taken image stored locally
print("[!!!] Processing local photo . . .")
os.system("curl http://128.197.136.204.8000/processPhoto")
print("[~~~] Returning ML results")
=======
from picamera import PiCamera
from time import sleep
import os


camera = PiCamera()
camera.start_preview()
sleep(15)
camera.capture('picture.jpg')
camera.stop_preview()



'''
    This file is not run on the Raspberry Pi but rather another device, e.g. a laptop
    Demonstrates how the Raspberry Pi can be told remotely to take a photo and then
    process the taken photo through the neural network, determining its material
    Should then return result back to the user e.g. at the laptop
'''

'''
# Part 1: Take a photo and save as 'image.jpg'
print("[!!!] Taking Photo . . .")
# os.system("raspistill -o image.jpg")
os.system("curl http://128.197.180.252:8000/takePhoto")
print("[~~~] Photo Taken ")

# Part 2.1: Send the image over a curl request to receive results from ML
print("[!!!] Sending photo to web server . . .")
# os.system("curl -F 'file=image.jpg' http://128.197.180.252:8000/send")

# Part 2.2: Instead of sending an image, tell server to grab taken image stored locally
os.system("curl http://128.197.180.252.8000/processPhoto")
print("[~~~] Returning ML results")
'''
>>>>>>> 9a0ee4467f15d6b9dccb067cdd74ece47191053a
