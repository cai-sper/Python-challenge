# election_data.csv contains 3 columns: Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv

# Set path for file
election_path = os.path.join("Resources","election_data.csv")

# Open CSV file and find the number of votes cast
with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data = list(csvreader)
    votes = len(data)
    print(f"Number of Votes Cast: {votes}")

# A complete list of candidates who received votes
candidates = {
     "name": [
            "Charles Casper Stockham",
            "Diana DeGette",
            "Raymon Anthony Doane"]}

candidate_counts = [0, 0, 0]
for i in range(int(votes)):
    for j in range(3):
        if data[i][2] == candidates["name"][j]:
            candidate_counts[j] += 1
for j in range(3):
    vote_percent = round((candidate_counts[j]/votes)*100, 3)
    print(f"{candidates['name'][j]}: {vote_percent}% ({candidate_counts[j]})")

# The winner of the election based on popular vote
winner = (max(candidate_counts))
winner_index = candidate_counts.index(winner)
print(f"Winner: {candidates['name'][winner_index]}")

# Print the analysis to the terminal (DONE STEP BY STEP) and export a text file with the results
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as analysis_file:
    analysis_file.write("Election Results\n")                                                     
    analysis_file.write("--------------------------\n")
    analysis_file.write(f"Total Votes: {votes}\n")
    analysis_file.write("--------------------------\n")
    analysis_file.write(f"{candidates['name'][0]}: {round((candidate_counts[0]/votes)*100, 3)}% ({candidate_counts[0]})\n")                                      
    analysis_file.write(f"{candidates['name'][1]}: {round((candidate_counts[1]/votes)*100, 3)}% ({candidate_counts[1]})\n") 
    analysis_file.write(f"{candidates['name'][2]}: {round((candidate_counts[2]/votes)*100, 3)}% ({candidate_counts[2]})\n")                         
    analysis_file.write("--------------------------\n")    
    analysis_file.write(f"Winner: {candidates['name'][winner_index]}\n")