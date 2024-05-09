import os
import csv

#Creating paths to my csv files
csvpath = "budget_data.csv"
csvpath2 = "election_data.csv"

#Creating empty lists for me to enter data into
budget_data = []
date = []
profit_loss = []
sum_change = []
election_data = []
voter_id = []
county = []
candidates = []
unique_candidates = []
candidate_winner = []

#Creating my variables
prev = None
max_change = 0
min_change = 0
charles_vote = 0
diana_vote = 0
raymon_vote = 0

#Connecting and running through budget data csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        budget_data.append(row)
        date.append(row[0])
        profit_loss.append(int(row[1]))

#Connecting and running through election data csv file
with open(csvpath2, encoding='UTF-8') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=",")
    csv_header2 = next(csvreader2)
    for row2 in csvreader2:
        election_data.append(row2)
        voter_id.append(row2[0])
        county.append(row2[1])
        candidates.append(row2[2])

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

#Creating a for loop to get the unique candidates and appending it to a list    
for x in candidates:
    if x not in unique_candidates:
        unique_candidates.append(x)

#Counting up the votes per each unique candidate
for person in candidates:
    if person == unique_candidates[0]:
          charles_vote = charles_vote + 1
    elif person == unique_candidates[1]:
        diana_vote = diana_vote + 1
    else:
        raymon_vote = raymon_vote + 1

#Finding the winner of the election
if (charles_vote > diana_vote) and (charles_vote > raymon_vote):
    candidate_winner.append(unique_candidates[0])
elif (raymon_vote > charles_vote) and (raymon_vote > diana_vote):
    candidate_winner.append(unique_candidates[2])
else:
    candidate_winner.append(unique_candidates[1])


#Creating variables
list_len = len(sum_change)
average_monthly_change = round(sum(sum_change)/list_len,2)
min_change_date = date[min_change_placement]
max_change_date = date[max_change_placement]
total_votes = len(candidates)
charles_vote_percent = round((charles_vote/total_votes) * 100, 3)
diana_vote_percent = round((diana_vote/total_votes) * 100, 3)
raymon_vote_percent = round((raymon_vote/total_votes) * 100, 3)

#Printing financial results to the terminal
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${average_monthly_change}")
print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")

#Printing election results to the terminal
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
print(f"Charles Casper Stockham: {charles_vote_percent}% ({charles_vote})")
print(f"Diana DeGette: {diana_vote_percent}% ({diana_vote})")
print(f"Raymon Anthony Doane: {raymon_vote_percent}% ({raymon_vote})")
print("----------------------------------")
print(f"Winner: {candidate_winner[0]}")
print("----------------------------------")

#Writing the financial and election results to a new csv file
output_path = "output.txt"
with open (output_path, "w") as output_csv:
    output_csv.write(f''' Financial Analysis
----------------------------------
Total Months: {len(date)}                   
Total: ${sum(profit_loss)}                     
Average Change: ${average_monthly_change}                     
Greatest Increase in Profits: {max_change_date} (${max_change})                     
Greatest Decrease in Profits: {min_change_date} (${min_change})


Election Results
----------------------------------
Total Votes: {total_votes}
Charles Casper Stockham: {charles_vote_percent}% ({charles_vote})
Diana DeGette: {diana_vote_percent}% ({diana_vote})                     
Raymon Anthony Doane: {raymon_vote_percent}% ({raymon_vote})
----------------------------------
Winner: {candidate_winner[0]}
----------------------------------
                     ''')


