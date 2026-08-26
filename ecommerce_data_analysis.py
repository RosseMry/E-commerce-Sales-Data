import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from load_csv import load

print('''
📝 Introduction

This project analyzes an E-Commerce Sales & Profit dataset using a complete exploratory data analysis (EDA) and time series analysis .

The project includes:

- Data cleaning and preprocessing
- Interactive visualizations using Plotly
- Sales and profit analysis
- Product and regional performance analysis
- Monthly and yearly trend analysis
- Time series decomposition
- Forecasting future sales
- Business insights and recommendations

The main goal is to discover patterns in sales behavior and understand future business trends.
''')

#Upload of data with error manage
print(" ================ 📂 DATA LOADING AND INITIAL EXPLORATION ==================\n")
df = load('ecommerce_sales_data.csv')
print('\n')
print(" ================ THE FIST FIVE ROWS ==================\n")
print(df.head(),'\n') # first five rows 
print(" ================ THE LAST FIVE ROWS ==================\n")
print(df.tail()) #last five rows of the dataset
print(" ================ THE LAST FIVE ROWS ==================\n")
print(df.columns)


print(" ================ 🔎 DATA QUALITY CHECK ==================\n")
print('Checking missing values : ',df.isnull().sum(),'\n')
print('Duplicate values :',df.duplicated().sum(),'\n')
print('Ensure numeric types')
for col in ['Quantity', 'Sales', 'Profit']:
    df[col] = pd.to_numeric(df[col], errors = 'coerce')

print(" ================ 📌 UNIQUE VALUE ANALYSIS ==================\n")
cols = ['Product Name', 'Category', 'Region']
print("*"*50)
for col in cols:
    print(f'{col} : {df[col].unique()}')
    print("*"*50)

print(" \n================ 📅 CONVERT DATE COLUMN ==================\n")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%B')
print(df.head())