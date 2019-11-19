# Author: Pratima Gokhale
# Python Challenge -  Home Work for Data Analysis and Visualization Bootcamp at UT Austin

# * The dataset is composed of two columns: `Date` and `Profit/Losses`.
# * Task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period

import os
import csv

filename_in = os.path.join("Resources", "budget_data.csv")
with open(filename_in, "r") as in_file:
    with open("Financial_Analysis.txt", "+w") as out_file:
    
    # Extract the clean data
        csv_reader = csv.DictReader(in_file)
        data = list(csv_reader)
        clean_data = [{key: row[key] for key in row} for row in data]

    #Find the number of unique enteries of months    
        no_of_months = set([d["Date"] for d in clean_data])
    
    #Find the sum of all the elements under the column "Profit/Losses"
        net_profit_losses = sum(int(d["Profit/Losses"])  for d in clean_data)


    # The below block of code identifies and sums up the difference between two adjacent enteries
    # of profit/losses by looping over entire data. 
    # This sum can then be used to find the average of changes in profit/losses over entire period
        change_profit = 0
        total_change = 0
        greatest_profit = 0
        greatest_profit_date =""
        greatest_loss = 0
        greatest_loss_date = ""
        for i in range(0, len(clean_data)-1):
            change_profit = int(clean_data[i+1]['Profit/Losses']) - int(clean_data[i]['Profit/Losses'])
            total_change  += change_profit
        # the below code compares  change in profit in each iteration with the greatest profit and greatest loss till now
        # if the change in profit is greater than greatest profit or it is less than the greatest loss then the new greatest 
        # profit or greatest loss is recorded.
            if(change_profit >= greatest_profit):
                greatest_profit = change_profit
                greatest_profit_date = clean_data[i+1]['Date']
            if(change_profit <= greatest_loss):
                greatest_loss = change_profit
                greatest_loss_date = clean_data[i+1]['Date']

        average_change_in_profit = round(total_change/(len(clean_data)-1), 2)
        
     
    # Formating of the result and printing
        line = ""
        line = line.__add__("Financial Analysis \n---------------------------- \n")
        line = line.__add__("Total Months: {} \n".format(len(no_of_months)))
        line = line.__add__("Total: ${}\n".format(net_profit_losses))
        line = line.__add__("Average  Change: {} \n".format(average_change_in_profit))
        line = line.__add__("Greatest Increase in Profits: {} (${}) \n".format(greatest_profit_date, greatest_profit ))
        line = line.__add__("Greatest Decrease in Profits: {} (${}) \n".format(greatest_loss_date, greatest_loss ))
        line = line.__add__("---------------------------- \n")
        
        print(line)
        out_file.write(line)
    out_file.close()
in_file.close()