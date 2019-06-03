# Ubiqum - Big Data - Investigating the Increase of Defaulted Customers
# by Alican Tanaçan
# version 1: Initial Data Analysis

# Change Directory
import os
os.chdir("D:\Anaconda_Python_WD")

# Import Dataset
import pandas as pd
credit = pd.read_csv("default of credit card clients.csv", header = 1)

# Inspect the Dataset
credit.head()
credit.describe()
credit.info()
A = credit.dtypes.index
print(A)

# Visualizations
import matplot.pyplot as plt
import seaborn as sns
plt.hist(credit["LIMIT_BAL"], bins = 4)
plt.show
plt.plot(credit["LIMIT_BAL"])
plt.show
X = credit["PAY_0"]
Y = credit["PAY_1"]
plt.scatter(X,Y)
plt.show

# Outlier Detection
B = credit["BILL_AMT1"]
plt.boxplot(A,0,'gd')
plot.show

# Correlation Matrix
corrMat = credit.corr()
print(corrMat)

# Covariance Matrix
covMat = credit.cov()
print(CovMat)