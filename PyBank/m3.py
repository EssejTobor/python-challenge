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

def percentChange(startPoint,currentPoint):
    return((float(currentPoint)-startPoint)/abs(startPoint))*100.00
for eachN in profits_losses:
    pc = percentChange(profits_losses[0], eachN)
    print(pc)


# $-2315.12
#print(average_diff)

'''
print("""
Financial Analysis
----------------------------------------
""")
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profits_losses)}')'''
