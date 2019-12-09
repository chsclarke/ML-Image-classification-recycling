<<<<<<< HEAD
# ME360 Final Project

Flask webserver that recieves a jpg photo and returns a classification.

repository for ME360 Final Project -- currently in progress. Roughly 90% accuracy at this point.
=======
# ME360 Final Project

Flask webserver that recieves a jpg photo and returns a classification.

repository for ME360 Final Project -- currently in progress. Roughly 90% accuracy at this point.

## Motion Detection
We need a tool that would automatically detect that there is a new object within the trash bin as we cannot expect the user to manually send a command to the Raspberry Pi to begin the classification every time there is a new item. 

We had two different approaches to this tool implementation. We could either:
1. Use some sensor to detect motion (e.g. an Ultrasonic, LIDAR, or IR Sensor) or
2. Use some existing implementation utilizing the Python Camera Module to detect motion

We decided to go with approach 2 as we did not want to introduce unnecessary parts to the project design if possible. However, choosing this approach possessed its own slew of problems as setting up an existing implementation completely depends on the available guides showing how to use the library and whether the implementation had been deprecated or not.

Our first choice was user FutureShark's [Raspberry Pi Motion Detection repository](https://gist.github.com/FutureSharks/ab4c22b719cdd894e3b7ffe1f5b8fd91). This was intended to be a simple example, but we encountered many installation issues when attempting to set up the repository. The main issues were:

- Even with the library PiCamera installed on both the host system (using sudo apt) and on the virtual environment (using pip3), we obtained the error "Picamera module not found" The solution to this was installing picamera with a very specific command as seen below:
	- ` sudo pip3 install "picamera[array]"
- The next issue we faced was Python could not find the OpenCV installed libraries. Similar to the picamera issue, the dependencies were installed but the Host/Virtual Environment could not find any of the installed OpenCV libraries. More time than we were willing to spend was required to figure out how to use this particular example, so we decided to move onto another exisiting example online.

Our second choice was a tutorial from The Zan Show called ["Tutorial 15: Detect Motion using Pi Camera"](http://thezanshow.com/electronics-tutorials/raspberry-pi/tutorial-15). This tutorial uses work from Brian Flakes as he created a module the tutorial uses and imports into its scripts to conduct simple motion detection in Python. The main challenges faced in this implementation were:

1. This tutorial was published in 2015 and was not updated since then as the author believed the main principles were still relevant. However, the program was designed in Python 2 while our entire code repository was programmed using Python 3.
2. Once the code was modified to use Python 3, we were able to successfully run the program which detected motion and then took 5 pictures. However, in our implementation, we will only need one picture. 
>>>>>>> 9a0ee4467f15d6b9dccb067cdd74ece47191053a
