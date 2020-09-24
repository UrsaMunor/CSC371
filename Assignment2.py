# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:06:47 2020

@author: Emiya Kiritsugu
"""

# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import numpy as np
import math

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2, attribute):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return math.sqrt(distance)
    
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# this is to ask the user to enter their address for the file
err = 0
direc = input("Please enter the directory of your file: ")
while (True):
    try:
        data = np.genfromtxt(direc, delimiter=', ')  
        break
    except FileNotFoundError:
        print("No such file! Please re-run the program :D")
        err = 1
        break
#C:/Users/89709/Desktop/Data Mining/Assignment 2/train_activities.csv

print(predict_classification(data, [0.0214, -0.228, -1.92], 3))
