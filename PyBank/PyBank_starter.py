import pandas as pd
from pathlib import Path
# Load the set with data
file_path = "budget_data.csv"
data = pd.read_csv(file_path)

# do the analysis
total_months = data.shape[0]
total_months2 = data.shape[1]
total_profit_losses = data['Profit/Losses'].sum()
# Calculate changes in Profit/Losses .
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()
# Find the greatest increase and decrease in profits
greatest_increase = data.loc[data['Change'].idxmax()]
greatest_decrease = data.loc[data['Change'].idxmin()]
# Print the results
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses:,.2f}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits:  {greatest_increase['Date']} (${greatest_increase['Change']:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']:,.2f})\n"

)
print(output)
# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as file:
    file.write(output)
print(f"Analysis saved to {output_file}")
print(data)
