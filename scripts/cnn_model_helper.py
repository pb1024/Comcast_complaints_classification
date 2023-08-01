from keras.models import Sequential
from keras import layers
from keras.layers import Flatten
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers import Dense


import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder,LabelEncoder


"""
Function to plot the losses and accuracy
for CNN model
"""
def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

def oneHot(dummy_labels):
    le = preprocessing.LabelEncoder()
    enc = OneHotEncoder()
    
    le.fit (dummy_labels)
    y_dummy = le.fit_transform(dummy_labels)
    y_dummy = y_dummy.reshape(-1, 1)
    enc.fit(y_dummy)
    y_dummy = enc.transform(y_dummy).toarray()
    y_dummy = y_dummy.astype('float32')
    print ("\n * OneHot example")
    print (y_dummy)
    return (y_dummy)