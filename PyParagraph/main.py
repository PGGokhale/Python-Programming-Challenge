# #Author: Pratima Gokhale
#
# About this Code:
# This code when run will ask the user to input a text file to be analyzed.
# Code calculates the metrics in two different ways.
# First approach is the standard way we learned in classes in Bootcamp.
# The second approach uses the regular expressions as suggested in the readme.
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


with open(filename, "r") as in_file:
   
   # Approach 1: Reads the file line by line and calculates the metrics using for loop
    sentence_count1 = 0
    letter_count1 = 0
    for line in in_file:
        words = line.split(' ')
        sentence_count1 += line.count('.')
        sentence_count1 += line.count('!')
        sentence_count1 += line.count('?')
        for word in words:
            letter_count1 += len(word)
    
    word_count1 = len(words)
    Avg_letter_count1 = letter_count1/word_count1
    print("---------------------")
    print("Analysis of Text from file: {}".format(filename))

    print("---------------------")
    print("Approach 1")
    print("---------------------")
    print("Approximate Word Count: {}".format(word_count1))
    print("Approximate Sentence Count: {}".format(sentence_count1))
    print("Average Letter Count: {}".format(Avg_letter_count1))
    print("---------------------")


    # Approach 2: Uses regular expression to extract the text from the file and return a list of sentences
    in_file.seek(0)
    paragraph = in_file.read()
    paragraph_split_lines = re.split("(?<=[!?.]) +", paragraph)# This gives list of sentences

    sentence_count2 = len(paragraph_split_lines)

    # This takes in the list of sentences and returns a list of list. The Sentence is converted into a list of words.
    word_breaked_para = [row.split(' ') for row in paragraph_split_lines]
    word_count2 = 0
    for row in word_breaked_para:
        word_count2 += len(row)

    Average_words_per_sentence = word_count2/len(word_breaked_para)

    # This takes in the list of sentences and returns a list of list containing 
    # the number of letters in each word of a sentence.
    letter_count_in_word_of_sentence = [[len(e) for e in row.split(' ')] for row in paragraph_split_lines]

    #This takes in the list of list generated above and returns the sum of letters in all the words.
    total_letters = sum([int(sum(row)) for row in letter_count_in_word_of_sentence])

    Avg_letter_count2 = total_letters/word_count2
    

    print("Approach 2")
    print("---------------------")
    print("Approximate Word Count: {}".format(word_count2))
    print("Approximate Sentence Count: {}".format(sentence_count2))
    print("Average Letter Count: {}".format(Avg_letter_count2))
    print("Average Sentence Length: {}".format(Average_words_per_sentence))
    print("---------------------")


  

   