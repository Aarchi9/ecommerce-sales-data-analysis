# E-Commerce Sales Data Analysis

## Project Overview

This project focuses on cleaning, exploring, and analyzing an e-commerce orders dataset using Python. The goal is to identify sales patterns, understand product and city performance, and explore customer order behavior through data analysis and visualizations.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- CSV

## Project Structure

```text
pandas_advanced/
│
├── analysis.py
├── visualizations/
│   ├── visualizations.py
│   └── charts/
├── ecommerce_orders_practice.csv
├── cleaned_orders.csv
├── requirements.txt
└── README.md
```

## Data Cleaning & Preparation

The original dataset contained 10,035 rows and 11 columns.

The following steps were performed:

- Standardized text values by removing extra spaces and converting text to lowercase.
- Identified and removed 35 duplicate rows.
- Investigated missing values in customer ID, city, payment method, and discount percentage.
- Identified invalid quantity and unit price values.
- Converted order dates into datetime format and handled invalid dates.
- Validated product and category relationships.
- Created revenue and net revenue columns.

Missing values that could not be reliably inferred were retained rather than filled with assumptions.

## Exploratory Data Analysis

The analysis explored:

- Overall sales and revenue.
- Product performance.
- City-wise revenue.
- Monthly revenue trends.
- Order status distribution.
- Payment method distribution.

## Key Findings

- The dataset contained 10,035 original records.
- 35 duplicate records were identified and removed.
- Laptop generated the highest gross revenue among the products.
- Kolkata generated the highest gross revenue among the cities.
- Saturday had the highest order count by weekday.
- Debit card was the most frequently recorded payment method.

## Visualizations

Five visualizations were created using Matplotlib:

1. Gross Revenue by Product
2. Gross Revenue by City
3. Monthly Gross Revenue Trend
4. Order Status Distribution
5. Payment Method Distribution

All generated charts are stored in `visualizations/charts/`.

## How to Run the Project

1. Clone or download this repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the data analysis script:

```bash
python analysis.py
```

4. Generate the visualizations:

```bash
python visualizations/visualizations.py
```

## Note

This is a learning and portfolio project developed to practice data cleaning, exploratory data analysis, Pandas operations, and data visualization using Python.
