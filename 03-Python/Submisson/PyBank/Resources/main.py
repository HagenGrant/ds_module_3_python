import os
import csv

#Creating paths to my csv files
csvpath = "budget_data.csv"


#Creating empty lists for me to enter data into
budget_data = []
date = []
profit_loss = []
sum_change = []

#Creating my variables
prev = None
max_change = 0
min_change = 0

#Connecting and running through budget data csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        budget_data.append(row)
        date.append(row[0])
        profit_loss.append(int(row[1]))

#Creating a for loop to find the sum, min, max, len, and the placement of the min/max        
for i in profit_loss: 
    if prev == None:
        prev = i
    else:
        monthly_change = i - prev
        # print(monthly_change)
        if monthly_change > max_change:
            max_change = monthly_change
            max_change_placement = len(sum_change) + 1
        if monthly_change < min_change:
            min_change = monthly_change
            min_change_placement = len(sum_change) + 1
        sum_change.append(monthly_change)
        prev = i

list_len = len(sum_change)
average_monthly_change = round(sum(sum_change)/list_len,2)
min_change_date = date[min_change_placement]
max_change_date = date[max_change_placement]

#Printing financial results to the terminal
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${average_monthly_change}")
print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")

#Writing the financial results to a new csv file
output_path = "budget_data_output.txt"
with open (output_path, "w") as output_csv:
    output_csv.write(f''' Financial Analysis
----------------------------------
Total Months: {len(date)}                   
Total: ${sum(profit_loss)}                     
Average Change: ${average_monthly_change}                     
Greatest Increase in Profits: {max_change_date} (${max_change})                     
Greatest Decrease in Profits: {min_change_date} (${min_change})
''')