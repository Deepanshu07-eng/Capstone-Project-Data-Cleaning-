import pandas as pd     # Library uses for data analysis
import numpy as np      # This Numerical Python library is used for Fast mathematical operations on arrays

# Loading the dataset

df = pd.read_csv('Messy_Employment_India_Dataset.csv')

# Displaying the first 5 rows of the dataset

print(df.head())

# Checking for missing values in the dataset
print('Missing values in each column:')

print(df.isnull().sum())
