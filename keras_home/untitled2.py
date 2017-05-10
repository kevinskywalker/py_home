# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:58:41 2017

@author: liujiacheng1
"""

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.layers import Dense, Activation


def ml():
    #loaingdat\
    input_data=pd.read_csv('titan_train.csv')
    print(input_data)

    x_train=input_data.iloc[:150,:19].values
    x_test=input_data.iloc[150:,:19].values
    y_train=input_data.iloc[:150,19:].values
    y_test=input_data.iloc[150:,19:].values
    print(y_train)    
    
    
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

# Generate dummy data
   
# Train the model, iterating on the data in batches of 32 samples
    
    model.fit(x_train, y_train, epochs=1000, batch_size=32)
    
ml()