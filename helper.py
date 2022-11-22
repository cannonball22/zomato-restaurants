import os

import joblib
import numpy as np

import pickle

import tensorflow as tf

from tensorflow.keras import layers

from tensorflow.keras import models, utils

import pandas as pd

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img, img_to_array

from tensorflow.python.keras import utils

current_path = os.getcwd()

scaler = joblib.load(
    r"C:\Users\Cannonball\Downloads\Epsilon AI Traning\4th project\zomato app\static\scaler.h5")
model = joblib.load(
    r'C:\Users\Cannonball\Downloads\Epsilon AI Traning\4th project\zomato app\static\model.h5')



def predictor(features):
    #print(len(features[0]))
    prediction = model.predict(features)

    return prediction
