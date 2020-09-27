# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:29:25 2020

@author: CHINMAY
"""

import keras
from PIL import Image, ImageOps
import numpy as np


def pred(img):
    # Load the model
    model = keras.models.load_model('croppi.h5')

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 256, 256, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (256, 256)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 255.0) 

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability
