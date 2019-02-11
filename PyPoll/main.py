import csv
import os

# variables 
voterid = []
country = []
candidate = []
total_votes = 0

# Set path for file
csvpath = os.path.join("election_data.csv")

# open the file and and name it csvfile, csv.reader will read it into csvreader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # read a record
    next(csvreader)
    # loop through each row and load the data into a list
    for row in csvreader:
        voterid.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

# calculate totoal votes by voterid
total_votes = len(voterid)
total_votes 

# Calculate totoal votes for each candidate and percentage
# kahn data
kahn_votes = candidate.count("Khan")
kahn_pct = (kahn_votes / total_votes) * 100
kahn_pct_rd = round(kahn_pct,2)
# correy data
correy_votes = candidate.count("Correy")
correy_pct = (correy_votes / total_votes) * 100
corry_pct_rd = round(correy_pct,2)
# li data
li_votes = candidate.count("Li")
li_pct = (li_votes / total_votes) * 100
li_pct_rd = round(li_pct,2)
# otooley data
otooley_votes = candidate.count("O'Tooley")  
otooley_pct = (otooley_votes / total_votes) * 100
otooley_pct_rd = round(otooley_pct,2)

# Calculate the most frequent candidate and use this value as the winner 
winner = max(set(candidate), key = candidate.count) 

# print to output
print("Election Results") 
print("----------------------------")
print(f"Total Votes: {total_votes}") 
print("----------------------------")
print(f"Kahn: {kahn_pct_rd}% ({kahn_votes})")
print(f"Correy: {corry_pct_rd}% ({correy_votes})")
print(f"Li: {li_pct_rd}% ({li_votes})")
print(f"O'Tooley: {otooley_pct_rd}% ({otooley_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Specify the file to write to
output_path = os.path.join("PypollAnalysis.txt")

# Open the file using "write" mode. 
with open(output_path, 'w', newline='') as out_file:
    # write the data to output file
    out_file.write("Election Results" + "\n") 
    out_file.write("----------------------------" + "\n")
    out_file.write(f"Total Votes: {total_votes}  \n") 
    out_file.write("----------------------------" + "\n")
    out_file.write(f"Kahn: {kahn_pct_rd}% ({kahn_votes}) \n")
    out_file.write(f"Correy: {corry_pct_rd}% ({correy_votes}) \n")
    out_file.write(f"Li: {li_pct_rd}% ({li_votes}) \n")
    out_file.write(f"O'Tooley: {otooley_pct_rd}% ({otooley_votes}) \n")
    out_file.write("----------------------------" + "\n")
    out_file.write(f"Winner: {winner} \n")               
    out_file.write("----------------------------" + "\n")
                   
