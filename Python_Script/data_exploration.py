import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset with error handling
file_path = "../data-set/assessment_dataset.xlsx"
try:
    df = pd.read_excel(file_path, sheet_name="in")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please make sure it exists in the same directory as the script.")
    exit()
except ValueError:
    print(f"Error: Sheet 'in' not found in '{file_path}'. Please check the Excel file.")
    exit()
except Exception as e: # Catch any other potential errors during file loading
    print(f"An error occurred while loading the Excel file: {e}")
    exit()


# Create output directory for plots
output_dir = "plots"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- Data Analysis and Output to Excel ---
output_file = "analysis_results.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # 1. Dataset Overview (Corrected)
    info_df = pd.DataFrame(df.dtypes, columns=['Data Type'])
    info_df['Non-Null Count'] = df.count()
    info_df['Memory Usage'] = df.memory_usage(deep=True)
    info_df.to_excel(writer, sheet_name="Dataset Overview")

    # 2. Sample Data
    df.head().to_excel(writer, sheet_name="Sample Data")

    # 3. Missing Values
    missing_values = df.isnull().sum()
    missing_values.to_frame(name="Missing Count").to_excel(writer, sheet_name="Missing Values")

    # 4. Aggregate Analysis (Sales)
    total_sales = df["TransactionAmount"].sum()
    total_transactions = df["TransactionID"].nunique()
    aov = total_sales / total_transactions
    sales_summary = pd.DataFrame({
        "Total Sales Revenue": [total_sales],
        "Average Order Value (AOV)": [aov]
    })
    sales_summary.to_excel(writer, sheet_name="Sales Summary")

    # 5. Sales by Region
    sales_by_region = df.groupby("Region")["TransactionAmount"].sum().sort_values(ascending=False)
    sales_by_region.to_excel(writer, sheet_name="Sales by Region")

    # 6. Top 5 Best-Selling Products
    top_products = df.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(5)
    top_products.to_excel(writer, sheet_name="Top Products")

    # 7. Sales Trends Over Time
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
    df["Month"] = df["TransactionDate"].dt.to_period("M")
    monthly_sales = df.groupby("Month")["TransactionAmount"].sum()
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales Trend")

    # --- Data Visualization and Saving Plots ---

    # 8. Visualizing Sales by Region
    plt.figure(figsize=(8, 5))
    sns.barplot(x=sales_by_region.index, y=sales_by_region.values, palette="Blues_r")
    plt.xlabel("Region")
    plt.ylabel("Total Sales (₹)")
    plt.title("Total Sales by Region")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, "plot1.png"), dpi=300)
    plt.close()

    # 9. Plot Monthly Sales Trend
    plt.figure(figsize=(10, 5))
    monthly_sales.plot(marker='o', color='b')
    plt.xlabel("Month")
    plt.ylabel("Total Sales (₹)")
    plt.title("Sales Trend Over Time")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig(os.path.join(output_dir, "plot2.jpg"), dpi=300)
    plt.close()

    # 10. Visualizing Top Products
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_products.index, y=top_products.values, palette="coolwarm")
    plt.xlabel("Product")
    plt.ylabel("Total Quantity Sold")
    plt.title("Top 5 Best-Selling Products")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, "plot3.jpg"), dpi=300)
    plt.close()

print(f"Analysis results saved to {output_file} and plots saved to '{output_dir}'")