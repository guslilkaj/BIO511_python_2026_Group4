#!/usr/bin/env python3
from premade_script import codons
import argparse
import os
from premade_script import codons, exercise_function
from  collections import Counter

def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # Here you need to check the output of the function
    print(f"This are our codons: {sequence_codons}")
    
    # Here you need to call the exercise_function from premade_script.py
    print()
    sequence_aminoacids = {} # I want to save the result as a new dictionary of sequences and aminoacids
    for header, codon_list in sequence_codons.items(): # for each sequence and for each codon list
        aa = exercise_function(codon_list) # save the aminoacids in a new string
        # And check the output of that function
        sequence_aminoacids[header] = aa # save in the dictionary header as a key and the aa string as a value
    print(f"This is the translation in aa: {sequence_aminoacids}") # print the trnslated dictionary

# 1. import Counter from collections. Use it to count how many times each codon occurs in each sequence,
# and print the result for each sequence
    print()
    print("Codons occurences")
    for header, codon_list in sequence_codons.items():
        occurences = Counter(codon_list) # like a dictionary with every codon as a key and the occurences as values
        print(header, occurences)

# 2. Print only the most common codon of each sequence, together with the number of times it occurs.
    print()
    print("Most common codon in each sequence")
    for header, codon_list in sequence_codons.items():
        occurrences = Counter(codon_list) # count again all the occurences for each codon list
        max_occurrence = max(occurrences.values()) # consider only the max value
        for codon, count in occurrences.items(): # go in the Counter dictionary
            if count == max_occurrence: # when an occurence == max
                print(header, codon, count) # print the most common for that sequence
                break # stop to search in this sequence/item
    
# 3. Use Counter to count the amino acids in each translated protein as well.
# Same steps as the sequence_codons, but using the sequence_aminoacids
    print()
    print("Aminoacids occurences")
    for header, codon_list in sequence_aminoacids.items():
        occurences = Counter(codon_list)
        print(header, occurences)


# Which amino acid is the most common one in each sequence?
    print()
    print("Most common aa in each sequence")
    for header, codon_list in sequence_aminoacids.items():
        occurrences = Counter(codon_list)
        max_occurrence = max(occurrences.values())
        for codon, count in occurrences.items():
            if count == max_occurrence:
                print(header, codon, count)
                break


if __name__ == "__main__":
    main()