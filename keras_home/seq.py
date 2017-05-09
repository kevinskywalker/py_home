# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.layers import Dense, Activation
def ml():
    
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

# Generate dummy data
    import numpy as np
    data = np.random.random((1000, 100))
    labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
    
    model.fit(data, labels, epochs=1000, batch_size=32)
    
ml()