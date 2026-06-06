import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@2026",
    database="sales_project"
)

query = "SELECT * FROM `sample - superstore`"

df = pd.read_sql(query, conn)

print(df.head())
print("\nTotal Records:") 
print(len(df))
top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Customers")
print(top_customers)
import matplotlib.pyplot as plt
sales_category = df.groupby("Category")["Sales"].sum()

print(sales_category)

import matplotlib.pyplot as plt

ax = sales_category.plot(
    kind="bar",
    figsize=(8,5)
)

for p in ax.patches:
    ax.annotate(
        f'{p.get_height():,.0f}',
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha='center',
        va='bottom'
    )

plt.title("Sales by Category", fontsize=14, fontweight="bold")
plt.xlabel("Category")
plt.ylabel("Sales Amount")

plt.tight_layout()

plt.show()
segment_profit = df.groupby("Segment")["Profit"].sum()

segment_profit.plot(kind="pie", autopct="%1.1f%%")

plt.title("Profit by Segment")

plt.show()
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

top_customers.plot(kind="bar")

plt.title("Top 10 Customers")
plt.xlabel("Customer")
plt.ylabel("Sales")

plt.show()
# Profit by Segment
segment_profit = df.groupby("Segment")["Profit"].sum()
print("\nProfit by Segment")
print(segment_profit)

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region")
print(region_sales)