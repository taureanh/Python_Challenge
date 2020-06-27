#import Budget Data
import os

import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Working directory

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
   

    csv_header = next(csvreader)

#Variables to track

    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    #print(f"Header: {csv_header}")               

#Calculate number of months and revenue using loop
       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    
    #print(len(month))
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    #print(total_revenue)

 #Calculate average changes using loop
i = 0
for i in range(len(revenue) - 1):
    profit_loss = int(revenue[i+1]) - int(revenue[i])

 # append profit_loss
    revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    #print(monthly_change)
    #print(Total)
    
#Greatest Increase in profits
    profit_increase = max(revenue_change)
    #print(profit_increase)
    p = revenue_change.index(profit_increase)
    month_increase = month[p+1]
    
#Greatest Decrease in profits
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    q = revenue_change.index(profit_decrease)
    month_decrease = month[q+1]


#Print out final summary

f = open("Financial Analysis", "w")

print('Financial Analysis', file = f )

print('----------------------------', file = f )


print("Total number of months: " + str(len(month)), file = f )

print("Total Revenue in period: $ " + str(total_revenue), file = f )
      
print("Average monthly change in Revenue : $" + str(monthly_change), file = f )

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})", file = f )

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})", file = f )

f.close()

