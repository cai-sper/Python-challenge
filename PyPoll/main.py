# election_data.csv contains 3 columns: Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

import os
import csv

election_path = os.path.join("Resources","election_data.csv")

with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    