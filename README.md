# Python-challenge
This repository is to work on and submit python programming homework.
This repository contains Python script for analyzing the financial records of a company. A set of financial data called budget_data.csv is given. The dataset is composed of two columns: Date and Profit/Losses. 

* The task is to create a Python script that analyzes the records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period

This repository consist of four folders, namely 
1. PyBank
    This folder consist of files "main.py" and "Financial_Analysis.txt". The main.py is the python code. When this code is executed it reads the "budget_data.csv" from the folder "Resources" which is inside PyBank folder. It generates the output "Financial_Analysis.txt" as well as prints the output on command prompt.
2. PyBoss
    This folder consist of files "main.py", "employee_data.csv", "us_state_abbrev.py" and "employee_data_new.csv". The main.py is the python code. It reads the employee_data.csv, reformats it and writes it in employee_data_new.csv. While doing this it uses a dictionary from us_state_abbrev.py
3. PyParagraph
    This folder consist of files "main.py", "para1.txt", "para2.txt". The main.py is the python code. When this code is executed it asks the user to input a text file which he/she wants to analyse. It is expected that user provides the full path of the text file along with its name. para1.txt and para2.txt are just the sample files which could be used for analysis but it is not mandatory to use these files. The python code analyzes the text file and prints the analyzed output on the command prompt. The same analysis is done using two different approaches. The output of both the approaches is printed on the command prompt.
4. PyPoll
    This folder consist of files "main.py" and "Poll_Result.txt". The main.py is the python code. When this code is executed it reads the "election_data.csv" from the folder "Resources" which is inside PyPoll folder. It generates the output "Poll_Result.txt" as well as prints the output on command prompt.

