import os
import csv

#Creating paths to my csv files
csvpath2 = "election_data.csv"

#Creating empty lists for me to enter data into
election_data = []
voter_id = []
county = []
candidates = []
unique_candidates = []
candidate_winner = []

#Creating my variables
charles_vote = 0
diana_vote = 0
raymon_vote = 0


#Connecting and running through election data csv file
with open(csvpath2, encoding='UTF-8') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=",")
    csv_header2 = next(csvreader2)
    for row2 in csvreader2:
        election_data.append(row2)
        voter_id.append(row2[0])
        county.append(row2[1])
        candidates.append(row2[2])



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

total_votes = len(candidates)
charles_vote_percent = round((charles_vote/total_votes) * 100, 3)
diana_vote_percent = round((diana_vote/total_votes) * 100, 3)
raymon_vote_percent = round((raymon_vote/total_votes) * 100, 3)


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
output_path = "election_data_output.txt"
with open (output_path, "w") as output_csv:
    output_csv.write(f''' Election Results
----------------------------------
Total Votes: {total_votes}
Charles Casper Stockham: {charles_vote_percent}% ({charles_vote})
Diana DeGette: {diana_vote_percent}% ({diana_vote})                     
Raymon Anthony Doane: {raymon_vote_percent}% ({raymon_vote})
----------------------------------
Winner: {candidate_winner[0]}
----------------------------------
                     ''')


