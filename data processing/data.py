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
# =============================================================================
# print(train_x[0])
# =============================================================================
train_x = train_x[1:]
for idx, val in enumerate(train_x):
    train_x[idx] = list(map(int, val))
train_x = np.array(train_x)  

train_y = []
vals = [40, 39, 31, 54, 32, 38, 31, 33, 31, 31, 32, 31]
count = 0
for i in vals:
    train_y = train_y + i * [count]
    count = count + 1


# =============================================================================
# import lime
# import sklearn
# import numpy as np
# 
# from sklearn.naive_bayes import MultinomialNB
# nb = MultinomialNB(alpha=.01)
# nb.fit(train_x, train_y)
# pred = nb.predict(train_x)
# print(nb.predict_proba([train_x[0]]))
# print(sklearn.metrics.f1_score(train_y, pred, average='weighted'))
# =============================================================================
# =============================================================================
# 
# class_names = ["better", "best", "blue", "broken", "clear", "giving", "good", "grand", "heavy", "light", "ragged", "sick" ]
# feature_names = ['ʒ', 'ʃ', 'ɹ', 'f', 'ʊ', 'i', 'æ', 'ɛ', 'ɡ', 'p', 'w', 'd͡ʒ', 'k', 'ŋ', 'oʊ', 'aɪ', 'j', 'ə', 't', 'ð', 'z', 'aʊ', 'm', 'ɪ', 'd', 'θ', 'h', 'b', 'ɚ', 'u', 'n', 's', 'v', 'ɑ', 'eɪ', 'ɔ', 't͡ʃ', 'ɔɪ', 'l']
# 
# explainer = lime.lime_tabular.LimeTabularExplainer(train_x, feature_names=feature_names, class_names=class_names, discretize_continuous=True)
# exp = explainer.explain_instance(train_x[0], nb.predict_proba, num_features=2, top_labels=1)
# exp.show_in_notebook(show_table=True, show_all=False)
# =============================================================================
