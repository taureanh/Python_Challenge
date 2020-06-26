import os

import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Variables to track
months = []
total_revenue = 0.0
revenue_changelist = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    firstrow = next(csvreader)
    previousrow = int(firstrow[1])
    for i in csvreader:
        months.append(i[0])
        total_revenue = total_revenue + int(i[1])
        revenue_change = int(i[1]) - previousrow
        revenue_changelist.append(revenue_change)

revenue_average = sum(revenue_changelist)/len(revenue_changelist)


print("The total months is" + str(len(months)))
print("Total:" + str(total_revenue))
print(revenue_average)

