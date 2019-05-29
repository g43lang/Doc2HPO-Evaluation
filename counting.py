#!usr/bin/python

import os
import json
# import numpy as np

path = "/Users/gabelang/Documents/GitHub/Doc2HPO-Evaluation"
TP = float(0)
TN = float(0)
FP = float(0)
FN = float(0)
# TP = []
# TN = []
# FP = []
# FN = []
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename == 'Performance.json': 
            # list_of_files[filename] = os.sep.join([dirpath, filename])
            # print(os.sep.join([dirpath, filename]))
            file_full_name = os.sep.join([dirpath, filename])
            f = open(file_full_name,'r+') 
            # json_string = f.read()
            dictionary_accuracy = json.load(f)
            TP += dictionary_accuracy['True positive']
            TN += dictionary_accuracy['True negative']
            FP += dictionary_accuracy['False positive']
            FN += dictionary_accuracy['False negative']
            # TP.append(float(dictionary_accuracy['True positive']))
            # TN.append(float(dictionary_accuracy['True negative']))
            # FP.append(float(dictionary_accuracy['False positive']))
            # FN.append(float(dictionary_accuracy['False positive']))




print("TP: " + str(TP))
print("FP: " + str(FP))
print("TN: " + str(TN))
print("FN: " + str(FN))
precision = TP/(TP + FP)
recall = TP/(TP + FN)
F_score = 2 * (precision * recall)/(precision + recall)
print(precision)
print(recall)
print(F_score)
accuracy = (TP + TN)/(TP + TN + FP + FN)
print(accuracy)
