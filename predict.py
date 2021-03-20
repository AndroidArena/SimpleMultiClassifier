#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class Fruits:
    def __init__(self,filename):
        self.filename =filename


    def predictionfruits(self):
        # load model
        model = load_model('model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        print("result===>>",result[0])

        if result[0][0] == 1:
            prediction = 'Avocado'
            print(prediction)
            return [{"image": prediction}]
        elif result[0][1] == 1:
            prediction = 'Banana'
            print(prediction)
            return [{"image": prediction}]
        elif result[0][2] == 1:
            prediction = 'Cauliflower'
            print(prediction)
            return [{"image": prediction}]
        else:
            print("Not Sure")
            return [{"image": "Not Sure"}]


