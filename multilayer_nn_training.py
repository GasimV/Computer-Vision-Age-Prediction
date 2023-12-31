# -*- coding: utf-8 -*-
"""Multilayer_NN_Training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L1RyMPds64sJxE1Y35kYyH-UskqoFg3K
"""

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np

def load_train(path):
    """
    Функция для загрузки обучающей выборки.
    """
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(features_train.shape[0], 28 * 28) / 255.0
    return features_train, target_train

def create_model(input_shape):
    """
    Функция для создания модели нейронной сети.
    """
    model = Sequential()
    model.add(Dense(128, input_shape=input_shape, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, train_data, test_data, batch_size=32, epochs=7, steps_per_epoch=None, validation_steps=None):
    """
    Функция для обучения модели.
    """
    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(features_train, target_train, validation_data=(features_test, target_test), batch_size=batch_size, epochs=epochs, steps_per_epoch=steps_per_epoch, validation_steps=validation_steps, verbose=2, shuffle=True)
    return model