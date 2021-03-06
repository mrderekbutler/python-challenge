import csv 
import os

# variables 
bank_date = []
bank_profit_loss = []
total_months = 0
total_profit_loss = 0
average = 0

# Set path for file
csvpath = os.path.join("budget_data.csv")

# open the file and and name it csvfile, csv.reader will read it into csvreader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # read a record
    next(csvreader)
    
    # loop through each row and load the data into a list
    for row in csvreader:
        bank_date.append(row[0])
        bank_profit_loss.append(row[1])   

# convert list to integer 
bank_profit_loss = [int(i) for i in bank_profit_loss] 
# Calculations
total_profit_loss = sum(bank_profit_loss) 
total_months =  len(bank_date)  
average = (total_profit_loss / total_months)
# get max data
max_index = bank_profit_loss.index(max(bank_profit_loss))  
max_amount = bank_profit_loss[max_index]
max_date = bank_date[max_index]
# get min data
min_index = bank_profit_loss.index(min(bank_profit_loss))  
min_amount = bank_profit_loss[min_index]
min_date = bank_date[min_index]
# print to output
print("Financial Analysis") 
print("----------------------------")
print(f"Total Months: {total_months}") 
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits:  {max_date} ({max_amount})")
print(f"Greatest Decrease in Profits:  {min_date} ({min_amount})")

# Specify the file to write to
output_path = os.path.join("PybankAnalysis.txt")

# Open the file using "write" mode. 
with open(output_path, 'w', newline='') as out_file:
    # write the data to output file
    out_file.write("Financial Analysis" + "\n") 
    out_file.write("----------------------------" + "\n")
    out_file.write(f"Total Months: {total_months} \n") 
    out_file.write(f"Total: ${total_profit_loss} \n")
    out_file.write(f"Average Change: ${average} \n")
    out_file.write(f"Greatest Increase in Profits:  {max_date} ({max_amount}) \n")
    out_file.write(f"Greatest Decrease in Profits:  {min_date} ({min_amount}) \n")    