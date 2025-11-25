import pandas as pd     # Library uses for data analysis
import numpy as np      # This Numerical Python library is used for Fast mathematical operations on arrays

# Loading the dataset

df = pd.read_csv('Messy_Employment_India_Dataset.csv')

# Displaying the first 5 rows of the dataset

print(df.head())

# Checking for missing values in the dataset
print('Missing values in each column:')

print(df.isnull().sum())

# print(df.columns)    -> i used this to check column names
 
# Filling missing values with appropriate strategies
df['Status'] = df['Status'].fillna(df['Status'].mode()[0])
df['Age Group'] = df['Age Group'].fillna(df['Age Group'].mode()[0])
df['Education'] = df['Education'].fillna(df['Education'].mode()[0])
df['Industry'] = df['Industry'].fillna(df['Industry'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])

df['AI Risk'] = df['AI Risk'].astype(str).str.lower().str.strip().replace('nan', pd.NA).fillna(df['AI Risk'].mode()[0])


df['Years of Experience'] = df['Years of Experience'].fillna(df['Years of Experience'].median())
df['Monthly Salary (INR)'] = df['Monthly Salary (INR)'].fillna(df['Monthly Salary (INR)'].median())


print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Removing duplicates

print("Duplicates before cleaning:", df.duplicated().sum())   # in this data set, There is no duplicate values

#Replace negative salaries with NaN and then fill them with median

df['Monthly Salary (INR)'] = np.where(df['Monthly Salary (INR)'] < 0 , df['Monthly Salary (INR)'].mean(), df['Monthly Salary (INR)'])
print("\nNegative salaries replaced. Any negative values now:", (df['Monthly Salary (INR)'] < 0).sum())   # there is no negative values in this data set

# replace invalid experience values with median
df['Years of Experience'] = np.where(df['Years of Experience'] < 0 , df['Years of Experience'].median(), df['Years of Experience'])
print("\nNegative experience values replaced. Any negative values now:", (df['Years of Experience'] < 0).sum())   # there is no negative values in this data set


