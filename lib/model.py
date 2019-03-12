# -*- coding: utf-8 -*-
"""

@file: model.py
@guid: d07fa3dc5f434beca96c2d9e99bb06c4

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-03-12 22:58:14
@modified:

@brief:
"""
__author__ = "Yue Peng"
import tensorflow as tf


class CharCNN(tf.keras.Model):
    def __init__(self):
        super(CharCNN, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(32, 3, activation="relu")

    def call(self, x):
        x = self.conv1(x)
        return x

