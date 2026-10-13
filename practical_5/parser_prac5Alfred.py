#parser.py
import argparse
import csv
import pandas as pd

parser = argparse.ArgumentParser("da csv parser",
"You'll wanna run it from the terminal with another file",
"script that reads a .csv file") #adds the name, help and description info to the parser
parser.add_argument('filename', help="input the path to whatever you wanna parse") #

args=parser.parse_args()

with open(args.filename, 'r') as f:        #if you check the prac5Alfred.py file you'll note that it does basically the same thing. This just adds args which is a shorthand for...the entire parser basically.
    reader=csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

#time to read it into a pandas format
df=pd.read_csv(args.filename, header=None)  #doing this within the "with open()" loop caused it to fail because it read f after cycling to the end, thinking it was empty
print(df)                                   #also remember to specify that there are no headers or it'll eat a row for you!
print(df.describe)              #df.describe would give us a bunch of statistical info if we had numbers in our matrix :) 