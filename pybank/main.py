import os
import csv

# bank_csv = os.path.join("..", "resources", "budget_data.csv")
bank_csv = "/Users/siobhan/data-analysis-projects/python-challenge/pybank/resources/budget_data.csv"


date = []
profit_and_loss = [] 

# open csv file
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:

        # add date
        date.append(row[0])

        # add profit/loss
        profit_and_loss.append(row[1])

    total_months = len(date)

    print(total_months)

