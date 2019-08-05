# Ubiqum - Big Data - Investigating the Increase of Defaulted Customers
# by Alican Tanaçan
# version 2: Building The Models

# Imports
import numpy as np
import pandas as pd
import scipy
from math import sqrt
import matplotlib.pyplot as plt

# Estimators
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score

# Cross Validation
from sklearn.cross_validation import train_test_split

# Data
rawData = pd.read_csv('default of credit card clients.csv', header=1)
rawData.head()
rawData.info()
