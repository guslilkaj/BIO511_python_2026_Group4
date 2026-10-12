import argparse
import csv
import pandas as pd

# Create an argument parser to handle command-line arguments
parser = argparse.ArgumentParser()
# Define a required argument for the name of the CSV file
parser.add_argument("file", help="Name of the CSV file to read")
# Parse the arguments provided by the user
args = parser.parse_args()

# Read the CSV file using the csv module
with open(args.file, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    data = list(reader)

# Convert the data into a pandas dataframe
df = pd.DataFrame(data)
# Convert values to numbers
df = df.apply(pd.to_numeric)
# Print a statistical summary of the data
print(df.describe())
