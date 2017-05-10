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

#global data sets





time=time.time()

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

    
    


def SVM(degree):
        clf = SVC(decision_function_shape='ovo',probability=True,kernel='poly',degree=i)  
        clf.fit(x_train,y_train)
        y_pred=clf.predict(x_train)
        acc=accuracy_score(y_train,y_pred)




    
    
    
def SVM_attention(time):
    
    input_data=pd.read_csv('clustered1.csv')

    print(input_data)

    x_train=input_data.iloc[:300,1:20].values
    x_test=input_data.iloc[300:,1:20].values
    y_train=input_data.iloc[:300,21:].values
    y_test=input_data.iloc[300:,:1].values
  

    
    degrees={}
    accs=[]
    for i in range(1,3):
        
        clf = SVC(decision_function_shape='ovo',probability=True,kernel='poly',degree=i)  
        clf.fit(x_train,y_train)
        y_pred=clf.predict(x_train)
        acc=accuracy_score(y_train,y_pred)
        assesment=['acc'+str(acc)+'degree'+str(i)]
        ass={acc:i}
        degrees.update(ass)
        print(assesment)
        accs.append(acc)
    
        
        
    #max accuracy 
    accs=np.array(accs)
    accs=np.array(accs)
    acc_max=np.amax(accs)
    
    
    
    #select value
    degree_eff=degrees[acc_max]
    print(degree_eff)
    
    
    
    #re_run
    clf = SVC(decision_function_shape='ovo',probability=True,kernel='poly',degree=i)  
    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_train)
    acc=accuracy_score(y_train,y_pred)
    
    
    
    #predict
    results=clf.predict(x_test)
    results=np.array(results)
    results=pd.DataFrame(results)
    results.to_csv('results'+str(time)+'.csv') 
    print(results)
  
    
    #evaluate
    dec = clf.decision_function(x_train)
    y_pred=clf.predict(x_train)
    print (clf.predict(x_train))
    acc=accuracy_score(y_train,y_pred)
    print(acc)
    
    '''
    
    #results
    results=clf.predict(test_data)
    results=pd.DataFrame(results)
    results.to_csv('results'+str(time)+'.csv')

    '''
    
SVM_attention(time)