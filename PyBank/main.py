#Dependencies
import os
import csv

# Data to read in and analyze
f = open('budget_data.csv')
csv = csv.reader(f)
csv_header = next(csv)

# Stored Variables
months = []
pandf = []

for row in csv:
    months.append(row[0])
    pandf.append(row[1])

#convert variable data type
profits_losses = [int(i) for i in pandf] 


average_change = []

for i in range(1, len(profits_losses)):
    average_change.append((int(profits_losses[i]) - int(profits_losses[i-1])))
    revenue_average = sum(average_change) / len(average_change)
    total_months = len(months)
    greatest_increase = max(average_change)
    greatest_decrease = min(average_change)
print("""
        Financial Analysis
----------------------------------------
""")
print(f'      Total Months: {len(months)}')
print(f'      Total: ${sum(profits_losses)}')
print(f'      Average change: ${str(round(revenue_average))}')
print(f'Greatest Increase in Profits: {str(months[average_change.index(max(average_change))+1])} $ {str(greatest_increase)}')
print(f'Greatest Decrease in Profits: {str(months[average_change.index(min(average_change))+1])} $ {str(greatest_decrease)}')


output_path = os.path.join('Financial-Analysis.txt')

with open(output_path,"w") as file:
    file.write("""
        Financial Analysis
----------------------------------------
""")
    file.write("\n")
    file.write(f'       Total Months: {len(months)}')
    file.write("\n")
    file.write(f'       Total: ${sum(profits_losses)}')
    file.write("\n")
    file.write(f'       Average change: ${str(round(revenue_average))}')
    file.write("\n")
    file.write(f'Greatest Increase in Profits: {str(months[average_change.index(max(average_change))+1])} $ {str(greatest_increase)}')
    file.write("\n")
    file.write(f'Greatest Decrease in Profits: {str(months[average_change.index(min(average_change))+1])} $ {str(greatest_decrease)}')


