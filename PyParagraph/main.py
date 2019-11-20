# #Author: Pratima Gokhale
#
# Description:
# * A Python script to automate the analysis of any passage using following metrics. 
# * This script will do the following:
# * Import a text file filled with a paragraph of your choosing.
# * Assess the passage for each of the following:
# * Approximate word count
# * Approximate sentence count
# * Approximate letter count (per word)
# * Average sentence length (in words)

import re

filename = input('Enter the filename which you would like to analyze: ')

sentence_count = 0
letter_count = 0
with open(filename, "r") as in_file:
    for line in in_file:
        words = line.split(' ')
        sentence_count += line.count('.')
        sentence_count += line.count('!')
        sentence_count += line.count('?')
        for word in words:
            letter_count += len(word)
    
    word_count = len(words)
    Avg_letter_count = letter_count/word_count
    print(word_count)
    print(sentence_count)
    print(Avg_letter_count)