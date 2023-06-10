# Calculate the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period
# Print the analysis to the terminal and export a text file with the results

# Modules
import os
import csv

#Set path for file
budget_path = os.path.join("Resources","budget_data.csv")

#Open the CSV file and find the number of months
"""
https://stackoverflow.com/questions/27504056/row-count-in-a-csv-file    
"""
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip the header
    data = list(csvreader)
    months = len(data)
    print(f"Number of Months: {months}")

# The net total amount of "Profit/Losses" over the entire period
    net_total = 0
    for row in data:
        net_total += int(row[1])
    print(f"Net Total: ${net_total}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period   
# The greatest decrease in profits (date and amount) over the entire period
    changes_list = []
    increase = 0
    decrease = 0
    for i in range(1, int(months)):                                                             
        change = int(data[i][1]) - int(data[i-1][1])                                           
        changes_list.append(change)
        average_change = int(sum(changes_list) / len(changes_list))
        if change > increase:
            increase = change
            increase_month = data[i][0]
        if change < decrease:
            decrease = change
            decrease_month = data[i][0]
    print(f"Average Change: ${average_change}")                
    print(f"Greatest Increase in Profits: {increase_month} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")

# Print the analysis to the terminal (DONE STEP BY STEP) and export a text file with the results
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as analysis_file:
    analysis_file.write("Financial Analysis\n")                                                     
    analysis_file.write("-----------------------\n")
    analysis_file.write(f"Number of Months: {months}\n")
    analysis_file.write(f"Net Total: ${net_total}\n")
    analysis_file.write(f"Average Change: ${average_change}\n")                                      
    analysis_file.write(f"Greatest Increase in Profits: {increase_month} (${increase})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {decrease_month} (${decrease})\n")