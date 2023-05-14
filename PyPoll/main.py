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
for i in range(0, int(votes)):
    for j in range(3):
        if data[i][2] == candidates["name"][j]:
            candidate_counts[j] += 1
for j in range(3):
    vote_percent = round((candidate_counts[j]/votes)*100, 3)
    print(f"{candidates['name'][j]}: {vote_percent}% ({candidate_counts[j]})")

# The winner of the election based on popular vote