# -*- coding: utf-8 -*-
"""
CSC373 Data Mining
Assignment 2: Classification
Author: Tianqi Hong, Han Bao, Michael Si
Date: 09/24/2020

Description:
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# this is to ask the user to enter their address for the file
err = 0
direc = input("Please enter the directory of your file: ")
while (True):
    try:
        data = pd.read_csv(direc)
        break
    except FileNotFoundError:
        print("No such file! Please re-run the program :D")
        err = 1
        break

# C:/Users/89709/Desktop/Data Mining/Assignment 1/train_activities.csv
# Dataset is now stored in a Pandas Dataframe

if (err == 0):
    # this part is for us to understand the data before we graph them
    # this function is my favorite function to see if we have any null in our dataset (see if we need to clean our dataset)
    data.isnull().sum()

    data.info

    data.shape

    # this is to print the first five rows of our dataset
    data.head()

    # this is to print the last five rows of our dataset
    data.tail()

    data.columns

    data.describe()

    # this is to see the uniqueness of our dataset. (To see if we have a lot of repeated data like what Prof. Khuri mentioned during class
    data.nunique()

    # dropping filename and timestamp because they don't seems like our independent variables
    data = data.drop(['filename', 'timestamp'], axis=1)

    data.head()