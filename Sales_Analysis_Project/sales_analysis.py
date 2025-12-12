import pandas as pd
import matplotlib.pyplot as plt

# 1. Loading data
sales = pd.read_csv("sales_project/sales.csv")
categories = pd.read_csv("sales_project/categories.csv")

print("\n=== SALES DATA ===")
print(sales)

print("\n=== CATEGORIES ===")
print(categories)

merged = sales.merge(categories, on="product", how="left")

print("\n=== MERGED DATA ===")
print(merged)

merged["total"] = merged["quantity"] * merged["price"]

print("\n=== Total revenue per product ===")
print(merged.groupby("product")["total"].sum())

print("\n=== Total revenue per category ===")
print(merged.groupby("category")["total"].sum())

merged["date"] = pd.to_datetime(merged["date"])

print("\n=== Orders per day ===")
print(merged.groupby("date")["order_id"].count())

print("\n=== Average price by category ===")
print(merged.groupby("category")["price"].mean())

merged.to_excel("sales_project/sales_report.xlsx", index=False)

print("\n=== KPI ===")
print("Total revenue:", merged["total"].sum())
print("Average order value:", merged["total"].mean())
print("Best-selling product:", merged.groupby("product")["total"].sum().idxmax())
print("Most popular category:", merged.groupby("category")["total"].sum().idxmax())

# 1. Total revenue per product
plt.figure()
merged.groupby("product")["total"].sum().plot(kind="bar")
plt.title("Total revenue per product")
plt.xlabel("Product")
plt.ylabel("Revenue")

# 2. Total revenue per category
plt.figure()
merged.groupby("category")["total"].sum().plot(kind="bar", color="orange")
plt.title("Total revenue per category")
plt.xlabel("Category")
plt.ylabel("Revenue")

# 3. Orders per day
plt.figure()
merged.groupby("date")["order_id"].count().plot(kind="line", marker="o")
plt.title("Orders per day")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.grid(True)

plt.show()

# --- KPI ---
total_revenue = merged["total"].sum()
avg_order = merged["total"].mean()
best_product = merged.groupby("product")["total"].sum().idxmax()
best_category = merged.groupby("category")["total"].sum().idxmax()

kpi = {
    "metric": ["total_revenue", "average_order_value", "best_selling_product", "best_category"],
    "value": [total_revenue, avg_order, best_product, best_category]
}
kpi_df = pd.DataFrame(kpi)

# --- Exporting results to Excel ---
with pd.ExcelWriter("sales_project/sales_report.xlsx", engine="openpyxl") as writer:
    merged.to_excel(writer, sheet_name="merged", index=False)
    sales.to_excel(writer, sheet_name="raw_sales", index=False)
    categories.to_excel(writer, sheet_name="categories", index=False)
    kpi_df.to_excel(writer, sheet_name="KPI", index=False)
    # sample summary
    summary = merged.groupby("category").agg(total_revenue=("total","sum"),
                                             avg_price=("price","mean"),
                                             items_sold=("quantity","sum")).reset_index()
    summary.to_excel(writer, sheet_name="summary_by_category", index=False)

print("XLSX saved: sales_project/sales_report.xlsx")

# --- Saving charts to PNG files ---
plt.figure()
merged.groupby("product")["total"].sum().plot(kind="bar")
plt.title("Total revenue per product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_project/product_revenue.png")

plt.figure()
merged.groupby("category")["total"].sum().plot(kind="bar", color="orange")
plt.title("Total revenue per category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_project/category_revenue.png")

plt.figure()
merged.groupby("date")["order_id"].count().plot(kind="line", marker="o")
plt.title("Orders per day")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_project/orders_per_day.png")

print("PNGs saved: sales_project/*.png")