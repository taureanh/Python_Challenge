#import Poll Data
import os

import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Working directory

csvpath = os.path.join('.', 'Resources', 'election_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
   

    csv_header = next(csvreader)

 #Variables to track
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #Vote Count
    total_votes = (len(votes))
    print(total_votes)

    #Votes by Person
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
    
    
    #Calculatin Percentages and round to 2 decimal places
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)
    
    
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

        #Print Statements and export results

    f = open("Election Results.txt", "w")

    print(f"Election Results", file = f)
    print(f"-----------------------------------", file = f)
    print(f"Total Votes: {total_votes}", file = f)
    print(f"-----------------------------------", file = f)
    print(f"Khan: {khan_percent}% ({khan_votes})", file = f)
    print(f"Correy: {correy_percent}% ({correy_votes})", file = f)
    print(f"Li: {li_percent}% ({li_votes})", file = f)
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})", file = f)
    print(f"-----------------------------------", file = f)
    print(f"Winner: {winner}", file = f)
    print(f"-----------------------------------", file = f)

    f.close()