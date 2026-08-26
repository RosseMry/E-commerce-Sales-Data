import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

df = pd.read_csv('ecommerce_sales_data.csv')


print(df.head()) # first five rows 
print(df.tail()) #last five rows of the dataset
print(df.shape) #shape of the dataset

print(df.columns)

https://www.kaggle.com/code/sohaibdevv/eda-of-e-commerce-sales-data#Data-Loading-and-Initial-Exploration