# import csv module
import csv

#set variable for csv data
bank_csv = "pybank/resources/budget_data.csv"

# set file to write results to
output_file = "pybank/analysis/output.txt"

# create lists to hold data
date = []
profit_and_loss = [] 


# open and read csv file
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    header = next(csvreader)

    # iterate through rows and put data into assigned variables 
    for row in csvreader:

        date.append(row[0])
        profit_and_loss.append(row[1])

total_months = len(date)
total_profit_and_loss = 0
monthly_change = []

# loop through profit and loss data and add amounts
for i in range(len(profit_and_loss)):
    amount = int(profit_and_loss[i])
    total_profit_and_loss += amount

# calculate monthly change 
for i in range(len(profit_and_loss)):
    month1 = int(profit_and_loss[i])
    month2 = int(profit_and_loss[i-1]) 
    monthly_change.append(month1 - month2)

# calculate greatest increase and decrease   
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)

# display final analysis

print(f'''
Financial Analysis
--------------------------
Total Months: {total_months}\n
Total Amount: ${total_profit_and_loss}\n
Greatest Increase in Profits: ${greatest_increase}\n
Greatest Decrease in Profits: ${greatest_decrease}\n 


''')

# export results to text file
with open(output_file, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("-----------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total Amount: " + "$" + str(total_profit_and_loss) + "\n")
    f.write("Greatest Increase in Profits: " + "$" + str(greatest_increase) + "\n")
    f.write("Greatest Decrease in Profits: " + "$" + str(greatest_decrease) + "\n")
    
