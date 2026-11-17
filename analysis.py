import pandas as pd
df = pd.read_csv("ecommerce_orders_practice.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe()) #statistical summary
print(df.duplicated().sum())
print(df.isnull().sum()) #missing values

print(df["product"].value_counts())
print(df["order_status"].value_counts())
print(df["city"].value_counts())
print(df["payment_method"].value_counts())

#general inspection
for col in df.columns:
    print(f"\n--- {col} ---")
    print("Data type:", df[col].dtype)
    print("Missing:", df[col].isnull().sum())
    print("Unique:", df[col].nunique())
    print("Sample values:", df[col].unique()[:10])

#data type specific inspection
print(df["order_date"].min())# to investigate dates
print(df["order_date"].max())
print(df["unit_price"].describe()) # to investigate numerical outliers

#business and rs checks
print(pd.crosstab(df["product"], df["category"])) # to investigate relationships

print("Missing IDs:", df["order_id"].isnull().sum())
print("Unique IDs:", df["order_id"].nunique())
print("Are IDs unique?", df["order_id"].is_unique)
print("Repeated IDs:", df["order_id"].duplicated().sum())
print(df["order_id"].head(10))

print("Missing customer IDs:", df["customer_id"].isnull().sum())
print("Unique customers:", df["customer_id"].nunique())
print("Most frequent customers:")
print(df["customer_id"].value_counts().head(10))
print("Customer ID samples:")
print(df["customer_id"].unique()[:20])

#Check whether repeated order IDs belong only to exact duplicate rows
repeated_orders = df[df["order_id"].duplicated(keep=False)]
print("Rows with repeated order IDs:", len(repeated_orders))
print("Exact duplicate rows among them:",
      repeated_orders.duplicated().sum())
print("Repeated order ID details:")
print(repeated_orders.sort_values("order_id").head(10))

customer_orders = df["customer_id"].value_counts()
customer_orders = df["customer_id"].nunique()
print("Customers with most orders:")
print(customer_orders.head(10))
print("Customers with only one order:",  (customer_orders == 1).sum())
print("Customers with multiple orders:",(customer_orders > 1).sum())
print("Maximum orders by one customer:",customer_orders.max())
print("Average orders per customer:",customer_orders.mean())
print(customer_orders.value_counts().sort_index())


#analysis_df for our standardized analysis
analysis_df = df.copy()
text_columns = ["product", "category", "city", "payment_method", "order_status"]
for col in text_columns:
    analysis_df[col] = analysis_df[col].str.strip().str.lower()
for col in text_columns:
    print(f"\n{col}")
    print("Original unique values:", df[col].nunique())
    print("Standardized unique values:", analysis_df[col].nunique())


#Missing values
print("Missing products:", df["product"].isna().sum())
print("Missing categories:", df["category"].isna().sum())
# Unique values
print("\nUnique products:")
print(sorted(df["product"].dropna().unique()))
print("\nUnique categories:")
print(sorted(df["category"].dropna().unique()))
# Frequency distributions
print("\nProduct frequencies:")
print(df["product"].value_counts())
print("\nCategory frequencies:")
print(df["category"].value_counts())
# Relationship between product and category
print("\nProduct-category relationship:")
print(pd.crosstab(df["product"], df["category"]))
print("Original product values:")
print(df["product"].unique())
print("\nStandardized product values:")
print(analysis_df["product"].unique())
product_category_check = (
    analysis_df.groupby("product")["category"]
    .nunique())
print(product_category_check[product_category_check > 1]) # this means we found no product associated with multiple categories
print(pd.crosstab(
    analysis_df["product"],
    analysis_df["category"]))

print("missing quantity:", df["quantity"].isna().sum())
print("missing unit_price", df["unit_price"].isna().sum())
print(" zero quantity ",(analysis_df["quantity"] == 0).sum())
print("negative quantity ",(analysis_df["quantity"] < 0).sum())
print("zero unit_price",(analysis_df["unit_price"] == 0).sum())
print("negative unit_price", (analysis_df["unit_price"] < 0).sum())
print(df[["quantity","unit_price"]].describe())

print(df[(df["quantity"] <= 0 )| (df["unit_price"] <= 0)])
filtered_df = df[(df["quantity"] <= 0) & (df["unit_price"] < 0)][["order_id", "quantity", "unit_price", "order_status"]]
print(filtered_df)
neg_q=(df["quantity"] < 0 ).sum()
print(neg_q)
neg_u = (analysis_df["unit_price"] < 0 ).sum()
print(neg_u)

print(analysis_df["discount_pct"].describe())
disc = (analysis_df["discount_pct"] < 0).sum() 
print(disc)
disc1 = (analysis_df["discount_pct"] > 100).sum() 
print(disc1)
print(analysis_df["discount_pct"].isna().sum())

print(analysis_df["order_date"].dtype)
print(pd.to_datetime(analysis_df["order_date"],errors="coerce").isna().sum())# to find invalid dates
filtered1 = analysis_df[pd.to_datetime(analysis_df["order_date"],errors="coerce").isna()]
print(filtered1)
print(pd.to_datetime(analysis_df["order_date"],errors="coerce").min())
print(pd.to_datetime(analysis_df["order_date"],errors="coerce").max())

explore_df = analysis_df.copy()

explore_df["order_date"]=pd.to_datetime(explore_df["order_date"],errors="coerce")
print(explore_df["order_date"].dtype)
explore_df["order_day"] = explore_df["order_date"].dt.day_name()
print(explore_df[["order_date","order_day"]].head())
print(explore_df["order_day"].value_counts())

explore_df["order_month"] = explore_df["order_date"].dt.month
print(explore_df["order_month"].dtype)
print(explore_df["order_month"].isna().sum())
print(explore_df["order_month"].unique())
print(explore_df["order_month"].value_counts().sort_index())

explore_df["order_year_month"] = explore_df["order_date"].dt.to_period("M")
print(explore_df["order_year_month"].value_counts().sort_index())

#investigation the missing values in customer id now fianlyyyyyy
print(analysis_df[analysis_df["customer_id"].isna()][["order_id","customer_id","order_date","order_status"]])
print(analysis_df[analysis_df["customer_id"].isna()])
print(analysis_df[analysis_df["customer_id"].isna()]["order_status"].value_counts())

print(analysis_df[analysis_df["discount_pct"].isna()][["order_id","product","unit_price","discount_pct","order_status"]])

print(analysis_df[analysis_df["city"].isna()][["order_id","customer_id","city","product","order_status"]])
print(analysis_df[analysis_df["city"].isna()]["order_status"].value_counts())

print(analysis_df[analysis_df["city"].isna()]["product"].value_counts())
missing_city_customers = analysis_df.loc[analysis_df["city"].isna(),"customer_id"]
print(missing_city_customers)
filter2=analysis_df[analysis_df["customer_id"].isin(missing_city_customers)][["customer_id","order_id","city"]]
print(filter2)
print(filter2.groupby("customer_id")["city"].nunique().value_counts())

print(analysis_df[analysis_df["payment_method"].isna()][["order_id","customer_id","product","payment_method","order_status"]])
print(analysis_df[analysis_df["payment_method"].isna()]["order_status"].value_counts())
print(analysis_df[analysis_df["payment_method"].isna()]["product"].value_counts())
#missing value investigation completed 

clean_df = analysis_df.copy()
clean_df = clean_df.drop_duplicates()
print(clean_df)
print(clean_df.shape)
print(analysis_df.shape)
print(clean_df.shape)
print(clean_df.duplicated().sum())

filter3 = clean_df[(clean_df["quantity"] <= 0)|(clean_df["unit_price"] <= 0)][["order_id","quantity","unit_price","order_status"]]
print(filter3)

valid_df = clean_df[(clean_df["quantity"] > 0)&(clean_df["unit_price"] > 0)]
print(valid_df)

invalid_dates = pd.to_datetime(valid_df["order_date"],errors="coerce").isna().sum()
print(invalid_dates)
valid_df["order_date"] = pd.to_datetime(valid_df["order_date"], errors="coerce")
print(valid_df["order_date"].dtype)
print(valid_df["order_date"].isna().sum())

print(valid_df.shape) #final overview of validdf
print(valid_df.isna().sum())
print(valid_df.duplicated().sum())

print(valid_df[["quantity","unit_price"]].min())
print(valid_df["order_date"].min())
print(valid_df["order_date"].max())
pdtcat=valid_df.groupby("product")["category"].nunique()
print(pdtcat[pdtcat>1])

#calculating revenue
valid_df["revenue"] = valid_df["quantity"] * valid_df["unit_price"]
print(valid_df[["product","quantity","unit_price","revenue"]])

print(valid_df["discount_pct"].describe())
print(valid_df["discount_pct"].isna().sum())

#Calculate net revenue after discount
valid_df["net_revenue"] = (valid_df["revenue"] *(1 - valid_df["discount_pct"] / 100))
# Inspect revenue calculations
print(valid_df[["product", "quantity", "unit_price", "discount_pct", "revenue", "net_revenue"]].head(10))
#Check missing net revenue values
print("Missing net revenue:",valid_df["net_revenue"].isna().sum())
# Revenue summary
print(valid_df[["revenue", "net_revenue"]].describe())

##BUSINESS ANALYSIS

##1. product performance
product_sales = valid_df.groupby("product").agg(
    total_quantity = ("quantity","sum"),
    total_revenue = ("revenue","sum"),
    average_revenue = ("revenue","mean"),
    total_orders = ("order_id","nunique")
).sort_values("total_revenue",ascending=False)
print("\nPRODUCT PERFORMANCE")
print(product_sales)

##2. CITY PERFORMANCE
city_sales = valid_df.groupby("city").agg(
    total_orders = ("order_id","nunique"),
    total_revenue = ("revenue","sum") 
).sort_values("total_revenue",ascending=False)
print("\nCITY PERFORMANCE")
print(city_sales)

## 3. MONTHLY SALES TREND
monthly_sales = (
    valid_df.dropna(subset=["order_date"])
    .groupby(valid_df.dropna(subset=["order_date"])["order_date"].dt.to_period("M"))["revenue"].sum().sort_index())
print("\nMONTHLY SALES")
print(monthly_sales) 

## 4. PAYMENT METHOD ANALYSIS
payment_analysis  = valid_df["payment_method"].value_counts()
print("\nPAYMENT METHODS")
print(payment_analysis)

## 5. ORDER STATUS ANALYSIS
status_analysis = valid_df["order_status"].value_counts()
print("\nORDER STATUS")
print(status_analysis)

## 6. OVERALL BUSINESS SUMMARY
print("\nOVERALL SUMMARY")
print("Total orders:", valid_df["order_id"].nunique())
print("Total quantity sold:", valid_df["quantity"].sum())
print("Gross revenue:", valid_df["revenue"].sum())
print("Average order revenue:", valid_df.groupby("order_id")["revenue"].sum().mean())
print("Average discount:", valid_df["discount_pct"].mean())

# #Correct literal "nan" in payment_method
valid_df["payment_method"] = valid_df["payment_method"].replace(
    "nan", pd.NA)
print("\nMissing payment methods:",
      valid_df["payment_method"].isna().sum())
print(valid_df["payment_method"].value_counts())


valid_df.to_csv("cleaned_orders.csv", index=False)

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
valid_df.to_csv(BASE_DIR / "cleaned_orders.csv", index=False)


