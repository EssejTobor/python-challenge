import os
import csv

csvpath = os.path.join(r'C:\My-Repo\python-challenge\PyBank\budget_data.csv')

months = 

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        print(row[])




#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period


#The average of the changes in "Profit/Losses" over the entire period


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period