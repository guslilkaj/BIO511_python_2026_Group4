#prac5Alfred.py
import sys
import csv
import os

filename='csvtest.csv'


if not os.path.isfile(filename) and len(sys.argv) >= 2: #checks if file exists. os.path just points out it's not a string but a file
    with open(filename, 'w', newline="") as file: #opens a new file in write mode with newline specified as ""
        writer=csv.writer(file) #creates writer as the converted file variable for the writerow operation. Saves me the effort of typing that out.
        for it_inst in range(5): #iteration instance. Had to name it something but it's not used. Just need it to run 5 times and the syntax wants a var.
            writer.writerow(["","","","",""]) #writes a bunch of empty lists
        
    with open(filename, 'a', newline="") as file: #reopens the file in write mode
        writer=csv.writer(file)                   
        writer.writerow([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]) #sys.argv[x] lets you insert arguments from the terminal when you order the program to run