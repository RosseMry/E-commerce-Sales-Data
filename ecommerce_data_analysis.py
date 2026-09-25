import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from load_csv import load
from theme_colors import PRIMARY, SUCCESS, WARNING, PURPLE, TEAL, DARK_TEXT, MID_TEXT, REGION_COLORS, LIGHT_TEXT

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

print(" ================ UNIQUE VALUE ANALYSIS ==================\n")
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

print(" \n================ STATISTICAL SUMMARY WITH DATE ==================\n")
print(df.describe())

print(" \n================ REGIONAL PROFIT ANALYSIS ==================\n")
region = df.groupby('Region')['Profit'].sum()
print(region.sort_values(ascending=False), "\n") #order by profit descending


print(" \n================ CATEGORY BY REGION ==================\n")
table_catreg = pd.pivot_table(df, values='Profit', index='Region', columns='Category', aggfunc=np.sum)
print(table_catreg, "\n")

print(" \n================ QUANTITY OF PRODUCT BY REGION ==================\n")
table_qtyreg = pd.pivot_table(df, values='Quantity', index='Region', columns='Product Name', aggfunc=np.sum)
print(table_qtyreg, "\n")

print(" \n================ 📈 DISTRIBUTION OF PROFIT ==================\n")
sales_month = df.groupby('Month Name')['Profit'].sum()
print(sales_month.sort_values(ascending=False), "\n")


print('''
📝 Analisis

Data Overview :

Total Records: 3,500 transactions
Time Period: 2022-2024
No missing values or duplicate records found

Regional Performance :

West region leads in total profit with 495,358.73
Followed by East (464,888.46), South (458,103.27), and North (426,314.75)
West dominates in Electronics and Accessories profits
South shows strong performance in Office category

Regional Product Preferences :

East: Strong in Smartwatch (517 units) and Smartphone (469 units)
North: Leads in Monitor sales (504 units)
South: Highest in Camera (527 units) and Printer (500 units)
West: Dominates in Tablet (508 units) and Mouse (498 units)

Correlation Insights :

Positive correlation between Sales and Profit (as expected)
Quantity shows moderate correlation with both Sales and Profit
No significant negative correlations observed

Data Distribution:

Profit distribution is right-skewed with some high-value outliers
Quantity shows fairly uniform distribution from 1-9 units
Regional distribution is relatively balanced
Category distribution shows Electronics dominating (~50%), followed by Accessories (~40%), and Office (~10%)


''')

print(" \n================ 📊 DATA VISUALIZATION ==================\n")
num_cols = ['Profit','Quantity','Sales','Month','Year']
plt.figure(figsize=(15,8))


for i, col in enumerate(num_cols, 1):
    plt.subplot(2, 3, i) #1 columna x 3 figuras por cada i 

    if col == 'Profit':
        color = PRIMARY
    elif col == 'Quantity':
        color = SUCCESS
    elif col == 'Sales':
        color = WARNING
    elif col == 'Month':
        color = PURPLE
    else:
        color = TEAL

    sns.histplot(df[col], kde=True, color=color, alpha=0.6, edgecolor='white')
    plt.title(f'Distribution of {col}', fontsize=14, fontweight='bold', color=DARK_TEXT)
    plt.xlabel(col, color=MID_TEXT)
    plt.ylabel('Frequency', color=MID_TEXT)


plt.subplot(2, 3, 6).set_visible(False)

plt.tight_layout()
plt.savefig('distribution_plots.png', dpi=300, bbox_inches='tight')
plt.show()

#DISTRIBUTION BY REGION PIE CHARTS
cat_cols = ['Region', 'Category', 'Product Name']
plt.figure(figsize=(18, 6))

for i, col in enumerate(cat_cols, 1):
    plt.subplot(1, 3, i)

    values = df[col].value_counts().values
    labels = df[col].value_counts().index

    # Assign colors based on column
    if col == 'Region':
        colors = [PRIMARY, SUCCESS, WARNING, PURPLE]  # North, East, South, West
    elif col == 'Category':
        colors = [PRIMARY, PURPLE, TEAL]  # Electronics, Accessories, Office
    else:
        colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(labels)))

    wedges, texts, autotexts = plt.pie(values,
                                        labels=labels,
                                        autopct='%1.1f%%',
                                        colors=colors,
                                        startangle=90,
                                        wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'alpha': 0.6},
                                        textprops={'fontsize': 11})

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)

    for text in texts:
        text.set_fontsize(11)
        text.set_color(DARK_TEXT)

    plt.title(f'Distribution of {col}', fontsize=16, fontweight='bold', color=DARK_TEXT, pad=20)

plt.tight_layout()
plt.show()


# DIAGRAM OF BLOQUES >? 
plt.figure(figsize=(10, 6))


ax = sns.barplot(x=region.index,
                 y=region.values,
                 palette=REGION_COLORS,
                 edgecolor='white',
                 linewidth=1.5,
                 saturation=0.9)


for container in ax.containers:
    ax.bar_label(container,
                 fmt='₹%.0f',  # Format as currency
                 fontsize=12,
                 fontweight='bold',
                 color=DARK_TEXT,
                 padding=3)


plt.title('Profit by Region', fontsize=18, fontweight='bold', color=DARK_TEXT, pad=20)
plt.xlabel('Region', fontsize=14, color=MID_TEXT, labelpad=10)
plt.ylabel('Total Profit (₹)', fontsize=14, color=MID_TEXT, labelpad=10)
plt.xticks(rotation=30, fontsize=12, color=MID_TEXT)
plt.yticks(fontsize=12, color=MID_TEXT)
plt.grid(axis='y', alpha=0.3, linestyle='--', color=LIGHT_TEXT)
sns.despine()
plt.tight_layout()
plt.show()