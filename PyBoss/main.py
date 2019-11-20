# Author: Pratima Gokhale
#
# Description:
# Convert the employee records from `employee_data.csv` file to a different format
#
# Old Format
#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#
#New Format
#Emp ID,First Name,Last Name,DOB,SSN,State
#214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#

import csv

# import the dictionary us_state_abbrev from the file us_state_abbrev.py
from us_state_abbrev import us_state_abbrev

with open('employee_data.csv', 'r') as in_file:
    with open('employee_data_new.csv', '+w') as out_file:

        csv_reader = csv.reader(in_file)
        clean_data = [[e.strip() for e in row] for row in csv_reader] 

# remove the spaces and '-' and clean the data further
        clean_data_new = []            
        clean_data_new =  [[row[0], row[1].split(' '),row[2].split('-'),row[3].split('-'),row[4]]for row in clean_data]

# format the data as required
        clean_data_new1 = []
        #clean_data_new1 = ['Emp ID','First Name','Last Name','DOB','SSN,State']
   
        for row in clean_data_new[1:]:

            clean_data_new1.append([row[0], 
            row[1][0], row[1][1], 
            '/'.join([row[2][1], 
            row[2][2], row[2][0]]), 
            '-'.join(['***', '**', row[3][2]]), 
            us_state_abbrev[row[4]]])
    
        clean_data_new1.insert(0, ['Emp ID','First Name','Last Name','DOB','SSN','State'])

# convert the formated data into string so that it could be writing into the csv file
        line = ''
        for row in clean_data_new1:
            line = line.__add__(str(row).replace('\'','', -1).replace('[','', -1).replace(']', '', -1).strip() + '\n')
        out_file.write(line)

    out_file.close()
in_file.close()