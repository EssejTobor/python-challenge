import os
import csv

f = open(r'C:\My-Repo\python-challenge\python-challenge\PyBank\budget_data.csv')
csv = csv.reader(f)
csv_header = next(csv)
months = []
pandf = []

for row in csv:
    months.append(row[0])
    pandf.append(row[1])

profits_losses = [int(i) for i in pandf] 



'''
print("""
Financial Analysis
----------------------------------------
""")
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profits_losses)}')'''
