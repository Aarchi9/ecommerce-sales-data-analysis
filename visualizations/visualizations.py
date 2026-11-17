import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Locate project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Load cleaned dataset
df = pd.read_csv(BASE_DIR / "cleaned_orders.csv")

# 3. Prepare columns
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

df["payment_method"] = df["payment_method"].replace("nan", pd.NA)

# 4. Create charts folder
CHART_DIR = Path(__file__).resolve().parent / "charts"
CHART_DIR.mkdir(exist_ok=True)

# 5. Calculate summaries

product_sales = df.groupby("product").agg(
    total_revenue=("revenue", "sum")
).sort_values("total_revenue")

city_sales = df.groupby("city").agg(
    total_revenue=("revenue", "sum")
).sort_values("total_revenue")

monthly_sales = (
    df.dropna(subset=["order_date"]) #remove rows with missing dates
    .groupby(df.dropna(subset=["order_date"])["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)

status_analysis = df["order_status"].value_counts()
payment_analysis = df["payment_method"].value_counts()

# 6. Revenue by product
product_sales["total_revenue"].plot(
    kind="barh", figsize=(10, 6),
    title="Gross Revenue by Product"
)
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(CHART_DIR / "revenue_by_product.png", dpi=300)
plt.show()
plt.close()

# 7. Revenue by city
city_sales["total_revenue"].plot(
    kind="bar", figsize=(10, 5),
    title="Gross Revenue by City"
)
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "revenue_by_city.png", dpi=300)
plt.show()
plt.close()

# 8. Monthly revenue trend
monthly_sales.index = monthly_sales.index.astype(str)

monthly_sales.plot(
    kind="line", marker="o", figsize=(12, 5),
    title="Monthly Gross Revenue Trend"
)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_revenue.png", dpi=300)
plt.show()
plt.close()

# 9. Order status distribution
status_analysis.plot(
    kind="bar", figsize=(8, 5),
    title="Order Status Distribution"
)
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHART_DIR / "order_status.png", dpi=300)
plt.show()
plt.close()

# 10. Payment method distribution
payment_analysis.plot(
    kind="bar", figsize=(8, 5),
    title="Payment Method Distribution"
)
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHART_DIR / "payment_methods.png", dpi=300)
plt.show()
plt.close()

print("All five charts have been saved successfully!")
print("Chart location:", CHART_DIR)
