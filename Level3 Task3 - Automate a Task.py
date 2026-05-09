#-----------------------------------#
# AUTOMATIC CSV REPORT GENERATOR
#-----------------------------------#

import pandas as pd

# Load dataset
file_name = "sales_data.csv"

df = pd.read_csv(file_name)

print("Dataset Loaded Successfully\n")

# Calculate statistics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

average_sales = df["Sales"].mean()
average_profit = df["Profit"].mean()

max_sales = df["Sales"].max()
min_sales = df["Sales"].min()

# Create summary report
report = {
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Average Sales",
        "Average Profit",
        "Maximum Sales",
        "Minimum Sales"
    ],
    "Value": [
        total_sales,
        total_profit,
        average_sales,
        average_profit,
        max_sales,
        min_sales
    ]
}

report_df = pd.DataFrame(report)

# Save report
report_df.to_csv("sales_report.csv", index=False)

print("Report generated successfully!")
print("\nSaved as: sales_report.csv")




