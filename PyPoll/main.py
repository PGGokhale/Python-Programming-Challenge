# Author: Pratima Gokhale
# 
# Description:
# Given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import csv
import os

filename_in = os.path.join("Resources", "election_data.csv")


with open(filename_in, "r") as in_file:
    with open("Poll_Result.txt", "+w") as out_file:
        csv_reader=csv.reader(in_file)
        header = next(csv_reader)
        clean_data = [[e.strip() for e in row] for row in csv_reader]

        # find the total number of votes
        total_votes = len(clean_data)

        # figureout the complete list of candidates without duplicates
        candidates = [row[2] for row in clean_data]

        # remove duplicate entries of candidate names
        unique_candidates = list(set(candidates))
        
        # find the total number of votes per candidate and the percentage of votes they received
        percentage_votes = []
        No_of_Votes = []
        for candidate in unique_candidates:
            count = 0
            for row in clean_data:
                if row[2] == candidate:
                    count += 1
            No_of_Votes.append(round(count))
            percentage_votes.append(round(100*count/total_votes, 3))
        
        #identify the winner
        winner = unique_candidates[percentage_votes.index(max(percentage_votes))]
        
        #Formatting the result
        line = "\n"
        
        line = line.__add__("Election Results \n")
        line = line.__add__("-------------------------\n")
        line = line.__add__("Total Votes: {} \n".format(total_votes))
        line = line.__add__("-------------------------\n")
        for i in range(0, len(unique_candidates)):
            line = line.__add__("{}: {}% ({}) \n".format(unique_candidates[i],percentage_votes[i],No_of_Votes[i] ))
        line = line.__add__("-------------------------\n")  
        line = line.__add__("Winner: {} \n".format(winner))
        line = line.__add__("-------------------------\n")

        #printing the result in a file
        out_file.write(line)

        #printing the result on the terminal
        print(line)

    out_file.close()
in_file.close()
  


