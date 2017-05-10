# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:39:17 2017

@author: liujiacheng1
"""



#for DeepLearning
import time
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

#for SVM
from sklearn.svm import SVC  
import numpy as np  
from sklearn.metrics import accuracy_score

#global data setz
time=time.time()


    
input_data=pd.read_csv('titan_train.csv')
test_data=pd.read_csv('titan_test.csv')
print(input_data)

x_train=input_data.iloc[:600,1:].values
x_test=input_data.iloc[600:,1:].values
y_train=input_data.iloc[:600,:1].values
y_test=input_data.iloc[600:,:1].values

test_data=test_data.values




def ml2():
    
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


def ml():
    
    input_data=pd.read_csv('titan_train.csv')
    test_data=pd.read_csv('titan_test.csv')
    print(input_data)

    x_train=input_data.iloc[:600,1:].values
    x_test=input_data.iloc[600:,1:].values
    y_train=input_data.iloc[:600,:1].values
    y_test=input_data.iloc[600:,:1].values
    print(y_test)
    
    
      
    model = Sequential()
    model.add(Dense(1000, activation='relu', input_dim=5))

    model.add(Dense(1000, activation='sigmoid'))
    model.add(Dense(6000, activation='relu'))
    model.add(Dense(1000, activation='sigmoid'))
    model.add(Dense(6000, activation='relu'))
    model.add(Dense(1000, activation='sigmoid'))
    model.add(Dense(6000, activation='relu'))
    
    
    
    model.add(Dense(1000, activation='sigmoid'))
    model.add(Dense(3000, activation='relu'))
    model.add(Dense(2000, activation='sigmoid'))
    model.add(Dense(1000, activation='relu'))

    model.add(Dense(800, activation='sigmoid'))
    model.add(Dense(500, activation='relu'))
    model.add(Dense(300, activation='sigmoid'))
    model.add(Dense(100, activation='relu'))
    
    model.add(Dense(50, activation='sigmoid'))
    model.add(Dense(10, activation='relu'))
  
    model.compile(loss='sparse_categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])


    model.fit(x_train, y_train, epochs=100, batch_size=30)
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=30)
    print(loss_and_metrics)

    
    
    
    
    
def SVM():
    
    

    
    
    
    clf = SVC(decision_function_shape='ovo',probability=True)  
    clf.fit(x_train,y_train)  
    print (clf.fit(x_train,y_train))  
    
    
    results=clf.predict(x_test)
    
    results=np.array(results)
    results=pd.DataFrame(results)
    results.to_csv('results'+str(time)+'.csv')
    print(results)
    print(np.reshape(results,-1))
    print('ok')
    dec = clf.decision_function(x_train)
    print(dec)
    print('ok')
    
    
    y_pred=clf.predict(x_train)
    print (clf.predict(x_train))  
    acc=accuracy_score(y_train,y_pred)
    print(acc)
    
    
    #results
    results=clf.predict(test_data)
    results=pd.DataFrame(results)
    results.to_csv('C:/Users/liujiacheng1/Desktop/py/py_home/keras_home/data/'+'results'+str(time)+'.csv')

SVM()
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