import os
import csv

f = open(r'C:\My-Repo\python-challenge\PyBank\budget_data.csv')
csv = csv.reader(f)
csv_header = next(csv)
months = []
profits_losses = []
for row in csv:
    months.append(row[0])
    profits_losses.append(row[1])
   
f.close()

print(len(months))