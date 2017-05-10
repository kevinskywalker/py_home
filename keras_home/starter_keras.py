# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:39:17 2017

@author: liujiacheng1
"""




import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

def ml():
    
    input_data=pd.read_csv('input.csv')
    print(input_data)

    x_train=input_data.iloc[:150,:19].values
    x_test=input_data.iloc[150:,:19].values
    y_train=input_data.iloc[:150,19:].values
    y_test=input_data.iloc[150:,19:].values
    print(y_train)
    
    
    
    model = Sequential()
    model.add(Dense(64000, activation='relu', input_dim=19))
   
    model.add(Dense(10000, activation='relu'))
    model.add(Dense(600, activation='relu'))
    model.add(Activation('relu'))
    model.add(Dense(2000))
    model.compile(loss='sparse_categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])


    model.fit(x_train, y_train, epochs=10, batch_size=10)
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=10)

ml()
'''
    model = Sequential()

    model.add(Dense(units=64, input_dim=100))
    model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

Once your model looks good, configure its learning process with .compile():

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

If you need to, you can further configure your optimizer. A core principle of Keras is to make things reasonably simple, while allowing the user to be fully in control when they need to (the ultimate control being the easy extensibility of the source code).

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

You can now iterate on your training data in batches:

# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
model.fit(x_train, y_train, epochs=5, batch_size=32)

Alternatively, you can feed batches to your model manually:

model.train_on_batch(x_batch, y_batch)

Evaluate your performance in one line:

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

Or generate predictions on new data:

classes = model.predict(x_test, batch_size=128)














from keras.models import Sequential

model = Sequential()

Stacking layers is as easy as .add():

from keras.layers import Dense, Activation

model.add(Dense(units=64, input_dim=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

Once your model looks good, configure its learning process with .compile():

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

If you need to, you can further configure your optimizer. A core principle of Keras is to make things reasonably simple, while allowing the user to be fully in control when they need to (the ultimate control being the easy extensibility of the source code).

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

You can now iterate on your training data in batches:

# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
model.fit(x_train, y_train, epochs=5, batch_size=32)

Alternatively, you can feed batches to your model manually:

model.train_on_batch(x_batch, y_batch)

Evaluate your performance in one line:

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

Or generate predictions on new data:

classes = model.predict(x_test, batch_size=128)
'''