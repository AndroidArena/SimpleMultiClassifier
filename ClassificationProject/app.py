# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:56:23 2020

@author: Dinesh
"""

# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

app = Flask(__name__)



@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index6.html")


@app.route('/prediction', methods=['POST', 'GET'])
@cross_origin()
def predictions():
    # Initialising the CNN
    classifier = Sequential()
    
    # Step 1 - Convolution
    classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
    
    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    
    # Adding a second convolutional layer
    classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    
    
    # Step 3 - Flattening
    classifier.add(Flatten())
    
    # Step 4 - Full connection
    classifier.add(Dense(units = 128, activation = 'relu'))
    
    classifier.add(Dense(units = 3, activation = 'sigmoid'))
    
    # Compiling the CNN
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    # Part 2 - Fitting the CNN to the images
    
    
    train_datagen = ImageDataGenerator(rescale = 1./255,
                                       shear_range = 0.2,
                                       zoom_range = 0.2,
                                       horizontal_flip = True)
    
    test_datagen = ImageDataGenerator(rescale = 1./255)
    training_set = train_datagen.flow_from_directory('/Users/Dinesh/Documents/jupyter_projects/ineuron/webscrappper_text - master/HerokuFlaskDemo - master/firstFlask/FruitsImages',
                                                     target_size = (64, 64),
                                                     batch_size = 32,
                                                     )
    
    test_set = test_datagen.flow_from_directory('/Users/Dinesh/Documents/jupyter_projects/ineuron/webscrappper_text - master/HerokuFlaskDemo - master/firstFlask/FruitsImages',
                                                target_size = (64, 64),
                                                batch_size = 32
                                                )
    
    classifier.fit_generator(training_set,
                             steps_per_epoch = 8000,
                             epochs = 1,
                             validation_data = test_set,    
                             validation_steps = 2000)
    
    # Part 3 - Making new predictions

    #C:\Users\Dinesh\Documents\jupyter_projects\ineuron\webscrappper_text - master\HerokuFlaskDemo - master\firstFlask
    test_image = image.load_img('/Users/Dinesh/Documents/jupyter_projects/ineuron/webscrappper_text - master/HerokuFlaskDemo - master/firstFlask/FruitsTest/banana1.jpg', target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    print(result[0])
    print(training_set.class_indices)
    if result[0][0] == 1:
        prediction = 'Avocado'
        print(prediction)
    elif result[0][1] == 1:
        prediction = 'Banana'
        print(prediction)
    elif result[0][2] == 1:
        prediction = 'Cauliflower'
        print(prediction)
    else:
        print("Not Sure")
        
    return render_template('results.html', predictions=prediction)

    
    
    
    
if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)