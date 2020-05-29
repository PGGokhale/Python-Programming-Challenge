# Python-challenge
This repository is to work on and submit python programming homework.

## PyBank
This repository contains Python script for analyzing the financial records of a company. A set of financial data called budget_data.csv is given. The dataset is composed of two columns: Date and Profit/Losses. 

The task is to create a Python script that analyzes the records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period

The folder PyBank consists of files "main.py" and "Financial_Analysis.txt". The main.py is the python code. When this code is executed it reads the "budget_data.csv" from the folder "Resources" which is inside PyBank folder. It generates the output "Financial_Analysis.txt" as well as prints the output on command prompt.

## PyBoss
This task consists of creating a Python script which will be able to convert employee records from the old format to the required format. The script will need to do the following:

* Import the employee_data.csv file, which currently holds employee records like the below:

```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then convert and export the data to use the following format instead:

```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

PyBoss folder consist of files "main.py", "employee_data.csv", "us_state_abbrev.py" and "employee_data_new.csv". The main.py is the python code. It reads the employee_data.csv, reformats it and writes it in employee_data_new.csv. While doing this it uses a dictionary from us_state_abbrev.py
    
## PyParagraph
This task is to assess the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Following is a set of metrics for assessing complexity.

This folder contains Python script to automate the analysis of any such passage using these metrics. 

* Import a text file filled with a paragraph of your choosing.
* Assess the passage for each of the following:
* Approximate word count
* Approximate sentence count
* Approximate letter count (per word)
* Average sentence length (in words)

    PyParagraph folder consist of files "main.py", "para1.txt", "para2.txt". The main.py is the python code. When this code is executed it asks the user to input a text file which he/she wants to analyse. It is expected that user provides the full path of the text file along with its name. para1.txt and para2.txt are just the sample files which could be used for analysis but it is not mandatory to use these files. The python code analyzes the text file and prints the analyzed output on the command prompt. The same analysis is done using two different approaches. The output of both the approaches is printed on the command prompt.
    
## PyPoll

This task is with helping a small, rural town modernize its vote-counting process. 

Given is a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. The task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

    The PyPoll folder consist of files "main.py" and "Poll_Result.txt". The main.py is the python code. When this code is executed it reads the "election_data.csv" from the folder "Resources" which is inside PyPoll folder. It generates the output "Poll_Result.txt" as well as prints the output on command prompt.

