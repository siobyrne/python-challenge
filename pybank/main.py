import os
import csv

# bank_csv = os.path.join("..", "resources", "budget_data.csv")
bank_csv = "/Users/siobhan/data-analysis-projects/python-challenge/pybank/resources/budget_data.csv"

# create lists to hold data
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
    total_profit_and_loss = 0

    # loop through profit and loss data and add amounts
    for i in range(len(profit_and_loss)):
        amount = int(profit_and_loss[i])
        print(amount)
        total_profit_and_loss += amount
        
                        

# display final analysis

print(f'''
Financial Analysis\n
--------------------------\n
Total Months: {total_months}\n
Total Amount: ${total_profit_and_loss}


''')