# import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# Load the dataset
df = pd.read_csv('diabetes.csv')

###### exploring the dataset to understand its structure, data types, 
##### and any potential missing values

# Display the first few rows
print(df.head())

# Get basic information about the dataset
print(df.info())

# Display basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Check the distribution of the target variable
print(df['Outcome'].value_counts())

