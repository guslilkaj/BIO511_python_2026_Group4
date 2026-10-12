''' Create a script that uses with open() to create a csv file with 5 rows and 5 columns
 Make sure to save the file and use comma as the separator.
 Appends a row to the file based on the user’s input, using argv. '''
import sys
import csv

with open("file.csv", "w", newline='') as file: 
    writer = csv.writer(file, delimiter=',')
     # Repeat 5 times to create 5 empty rows
    for i in range(5): # for every row
        row = [] # create an empty list
         # Repeat 5 times to create 5 columns
        for j in range(5): # for every column
            row.append(j + 1) # append the value of j + 1 (it starts from 0)
        # Write the row to the CSV file
        writer.writerow(row)

# Get the user's input (except the open.py) from the command line
user_input = ' '.join(sys.argv[1:])
# Split the input into separate values
row = user_input.split()
# Append the new row to the CSV file
with open('file.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(row)

