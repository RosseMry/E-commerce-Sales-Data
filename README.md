# E-Commerce Sales & Profit Analysis
 
A complete exploratory data analysis (EDA) and time series analysis of an E-Commerce Sales & Profit dataset, using `pandas`, `numpy`, `matplotlib`, `seaborn` and `plotly`.
 
## 📝 Introduction
 
This project analyzes an E-Commerce Sales & Profit dataset through a full exploratory data analysis and time series analysis. The main goal is to discover patterns in sales behavior and understand future business trends.
 
The project includes:
 
- Data cleaning and preprocessing
- Interactive visualizations using Plotly
- Sales and profit analysis
- Product and regional performance analysis
- Monthly and yearly trend analysis
- Time series decomposition
- Forecasting future sales
- Business insights and recommendations
## 🗂️ Project structure
 
```
E-commerce-Sales-Data/
├── ecommerce_sales_data.csv       # Raw dataset
├── load_csv.py                    # CSV loading with error handling
├── ecommerce_data_analysis.py     # Main analysis script
└── README.md
```
 
## 📊 Dataset
 
The dataset (`ecommerce_sales_data.csv`) contains the following columns:
 
| Column | Description |
|---|---|
| `Order Date` | Date of the order |
| `Product Name` | Product sold (e.g. Printer, Mouse, Tablet) |
| `Category` | Product category (e.g. Office, Accessories, Electronics) |
| `Region` | Sales region (North, East, South, West...) |
| `Quantity` | Units sold |
| `Sales` | Total sale amount |
| `Profit` | Profit generated |
 
## 🔎 Data loading and cleaning
 
- **Data loading**: `load_csv.py` loads the CSV into a `DataFrame`, prints its shape, and handles `FileNotFoundError`, empty files, and parsing errors.
- **Initial exploration**: preview of the first/last 5 rows and column names.
- **Data quality check**: missing values, duplicates, and numeric type coercion for `Quantity`, `Sales`, `Profit`.
- **Unique value analysis**: distinct values for `Product Name`, `Category`, `Region`.
- **Date handling**: `Order Date` converted to `datetime`, with `Year`, `Month`, and `Month Name` columns derived from it.
<!-- 📷 Screenshot placeholder: console output of data quality check -->
![Data quality check output](images/data_quality_check.png)
 
## 📈 Sales & profit analysis
 
Analysis of sales and profit performance across products and regions, including interactive Plotly charts.
 
<!-- 📷 Screenshot placeholder: sales/profit by region chart -->
![Sales and profit by region](images/sales_profit_by_region.png)
 
<!-- 📷 Screenshot placeholder: sales/profit by product chart -->
![Sales and profit by product](images/sales_profit_by_product.png)
 
## 📅 Trend analysis
 
Monthly and yearly trends, plus a full time series decomposition (trend, seasonality, residuals).
 
<!-- 📷 Screenshot placeholder: monthly/yearly trend chart -->
![Monthly and yearly trend](images/monthly_yearly_trend.png)
 
<!-- 📷 Screenshot placeholder: time series decomposition -->
![Time series decomposition](images/time_series_decomposition.png)
 
## 🔮 Forecasting
 
Forecast of future sales based on the historical trend.
 
<!-- 📷 Screenshot placeholder: sales forecast chart -->
![Sales forecast](images/sales_forecast.png)
 
## 💡 Business insights & recommendations
 
Key takeaways derived from the analysis above, and recommendations based on the observed sales and profit patterns.
 
## ⚙️ Running it
 
```bash
pip install pandas numpy matplotlib seaborn plotly
python ecommerce_data_analysis.py
```
 
## ✍️ Author
 
Project by [RosseMry](https://github.com/RosseMry).
