from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# https://www.tensorflow.org/tutorials/keras/classification

"""
0	T-shirt/top
1	Trouser
2	Pullover
3	Dress
4	Coat
5	Sandal
6	Shirt
7	Sneaker
8	Bag
9	Ankle boot
"""
#assign names to the categories
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


"""shriking the images to less quality"""

#pre process the data
train_images = train_images / 255.0

test_images = test_images / 255.0


"""
defining the model and setting up layers:
first line flattens the list (2d to 1d list) and define it as the
first layer of the neural network. called the input layer

second line creates a 'dense' or fully connected layer. 
this means that each node in the input layer will have one 
connection to each node in the second 'dense' layer.
* there will be 128 neurons or nodes in the second layer
* the activation function simplifies the output of the layer 
to a smaller range (increases accuracy). relux is a basic 
activation function that will applyto pretty much anything so 
its good for us

same thing goes for third layer. its dense or fully connected.
* the softmax activation function outputs a prob of each 
possible catagory. this will be on range 0-1.
* this is out last layer, or our output layer.
10 nodes -- 10 categories. each with a prob of the 
image being one of the categories

"""

# set up the layers
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

"""

* Loss function —This measures how accurate the model is during training. 
You want to minimize this function to "steer" the model in the right 
direction.

* Optimizer —This is how the model is updated based on the data it sees 
and its loss function.

* Metrics —Used to monitor the training and testing steps. The 
following example uses accuracy, the fraction of the images that 
are correctly classified.
"""


# compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


"""
Training the neural network model requires the following steps:

* Feed the training data to the model. In this example, the training
 data is in the train_images and train_labels arrays.
* The model learns to associate images and labels.
* You ask the model to make predictions about a test set—in this
 example, the test_images array. Verify that the predictions
 match the labels from the test_labels array.

To start training, call the model.fit method—so called because it 
"fits" the model to the training data:

epochs is how many times the neural network sees any given image.
basic way to help increase accuracy

"""

model.fit(train_images, train_labels, epochs=5)

"""
open an image and see its contents
plt.imshow(train_images[7])
plt.show()

"""

"""
# test the model we have just defined
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)
"""
model.save('my_model.h5') 