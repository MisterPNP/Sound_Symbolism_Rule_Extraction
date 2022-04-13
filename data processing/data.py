#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:44:55 2022

@author: wanyongfeng
"""


import csv
import numpy as np

file = open('/Users/wanyongfeng/Desktop/training.csv')

csvreader = csv.reader(file)

train_x = []
for row in csvreader:
        train_x.append(row[1:])

train_x = np.array(train_x)    

train_y = []
vals = [1,2,3,4,5]
count = 0
for i in vals:
    train_y = train_y + i * [count]
    count = count + 1
print(train_y)