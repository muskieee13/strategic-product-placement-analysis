"""
Strategic Product Placement Analysis – Data Analysis Script
============================================================
Standalone Python script that performs comprehensive exploratory data analysis
on the retail_sales_dataset and prints key insights.

Usage:
    python data_analysis.py
"""

import pandas as pd
import os

# ─── Load Data ───────────────────────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "Data", "retail_sales_dataset 2.csv")
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])

print("=" * 70)
print("  STRATEGIC PRODUCT PLACEMENT ANALYSIS – DATA REPORT")
print("=" * 70)

# ─── 1. Dataset Overview ────────────────────────────────────────────────────
print("\n1. DATASET OVERVIEW")
print("-" * 40)
print(f"   Total Records       : {len(df):,}")
print(f"   Columns             : {', '.join(df.columns)}")
print(f"   Date Range          : {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"   Product Categories  : {', '.join(df['Product Category'].unique())}")
print(f"   Unique Customers    : {df['Customer ID'].nunique():,}")
print(f"   Missing Values      : {df.isnull().sum().sum()}")

# ─── 2. Key Performance Indicators ──────────────────────────────────────────
print("\n2. KEY PERFORMANCE INDICATORS (KPIs)")
print("-" * 40)
total_revenue = df["Total Amount"].sum()
avg_order = df["Total Amount"].mean()
total_qty = df["Quantity"].sum()
print(f"   Total Revenue       : ${total_revenue:,.2f}")
print(f"   Total Transactions  : {len(df):,}")
print(f"   Average Order Value : ${avg_order:,.2f}")
print(f"   Total Quantity Sold : {total_qty:,}")
print(f"   Avg Quantity/Order  : {df['Quantity'].mean():.2f}")

# ─── 3. Sales by Product Category ───────────────────────────────────────────
print("\n3. SALES BY PRODUCT CATEGORY")
print("-" * 40)
cat_stats = (
    df.groupby("Product Category")
    .agg(
        Revenue=("Total Amount", "sum"),
        Avg_Sale=("Total Amount", "mean"),
        Transactions=("Transaction ID", "count"),
        Avg_Qty=("Quantity", "mean"),
    )
    .sort_values("Revenue", ascending=False)
)
for cat, row in cat_stats.iterrows():
    pct = row["Revenue"] / total_revenue * 100
    print(f"   {cat:<15} | Revenue: ${row['Revenue']:>10,.0f} ({pct:5.1f}%) | "
          f"Txns: {row['Transactions']:>4} | Avg Sale: ${row['Avg_Sale']:>8,.2f}")

# ─── 4. Sales by Gender ─────────────────────────────────────────────────────
print("\n4. SALES BY GENDER")
print("-" * 40)
gender_stats = df.groupby("Gender").agg(
    Revenue=("Total Amount", "sum"),
    Transactions=("Transaction ID", "count"),
    Avg_Sale=("Total Amount", "mean"),
)
for gender, row in gender_stats.iterrows():
    pct = row["Revenue"] / total_revenue * 100
    print(f"   {gender:<10} | Revenue: ${row['Revenue']:>10,.0f} ({pct:5.1f}%) | "
          f"Txns: {row['Transactions']:>4} | Avg: ${row['Avg_Sale']:>8,.2f}")

# ─── 5. Sales by Age Group ──────────────────────────────────────────────────
print("\n5. SALES BY AGE GROUP")
print("-" * 40)
bins = [0, 25, 35, 45, 55, 100]
labels = ["18-25", "26-35", "36-45", "46-55", "55+"]
df["Age Group"] = pd.cut(df["Age"], bins=bins, labels=labels)
age_stats = (
    df.groupby("Age Group", observed=True)
    .agg(Revenue=("Total Amount", "sum"), Transactions=("Transaction ID", "count"))
    .sort_values("Revenue", ascending=False)
)
for age, row in age_stats.iterrows():
    pct = row["Revenue"] / total_revenue * 100
    print(f"   {str(age):<10} | Revenue: ${row['Revenue']:>10,.0f} ({pct:5.1f}%) | Txns: {row['Transactions']:>4}")

# ─── 6. Monthly Sales Trend ─────────────────────────────────────────────────
print("\n6. MONTHLY SALES TREND (2023)")
print("-" * 40)
df["Month"] = df["Date"].dt.to_period("M")
monthly = df.groupby("Month")["Total Amount"].sum()
max_month = monthly.idxmax()
min_month = monthly.idxmin()
for month, sales in monthly.items():
    bar = "█" * int(sales / monthly.max() * 30)
    marker = " ← PEAK" if month == max_month else (" ← LOW" if month == min_month else "")
    print(f"   {month} | ${sales:>10,.0f} | {bar}{marker}")

# ─── 7. Price Point Analysis ────────────────────────────────────────────────
print("\n7. PRICE PER UNIT ANALYSIS")
print("-" * 40)
price_stats = df.groupby("Price per Unit").agg(
    Transactions=("Transaction ID", "count"),
    Total_Revenue=("Total Amount", "sum"),
)
for price, row in price_stats.sort_values("Total_Revenue", ascending=False).iterrows():
    print(f"   ${price:>6,.0f} | Txns: {row['Transactions']:>4} | Revenue: ${row['Total_Revenue']:>10,.0f}")

# ─── 8. Top 10 Customers ────────────────────────────────────────────────────
print("\n8. TOP 10 CUSTOMERS BY SPENDING")
print("-" * 40)
top_cust = (
    df.groupby("Customer ID")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
for i, (cust, amount) in enumerate(top_cust.items(), 1):
    print(f"   {i:>2}. {cust} — ${amount:,.0f}")

# ─── 9. Cross-Category Insights ─────────────────────────────────────────────
print("\n9. GENDER × CATEGORY CROSS-ANALYSIS")
print("-" * 40)
cross = pd.pivot_table(df, values="Total Amount", index="Gender",
                       columns="Product Category", aggfunc="sum")
print(cross.to_string())

# ─── 10. Statistical Summary ────────────────────────────────────────────────
print("\n10. STATISTICAL SUMMARY")
print("-" * 40)
print(df[["Age", "Quantity", "Price per Unit", "Total Amount"]].describe().to_string())

# ─── Summary ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("  KEY FINDINGS & RECOMMENDATIONS")
print("=" * 70)
print("""
  1. ELECTRONICS leads in total revenue due to high unit prices.
     → Recommend: Premium shelf placement for electronics products.

  2. CLOTHING dominates transaction volume — the most popular category.
     → Recommend: Increase variety and shelf space for clothing.

  3. Age group 26-45 drives the majority of spending.
     → Recommend: Target marketing campaigns to this demographic.

  4. Gender spending is relatively balanced.
     → Recommend: Gender-neutral placement strategies work best.

  5. Sales peak in holiday season (Nov-Dec) and mid-year (May-Jun).
     → Recommend: Align promotional campaigns with seasonal peaks.

  6. Higher price points ($300-$500) generate disproportionate revenue.
     → Recommend: Strategic placement of premium items in high-traffic areas.
""")

print("=" * 70)
print("  Analysis complete. See Tableau dashboard for interactive insights.")
print("=" * 70)
