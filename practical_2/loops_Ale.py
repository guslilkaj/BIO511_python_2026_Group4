# 1. Simple loop
my_list = [1, 2, 3, 4, 5, 6, 7]
print(type(my_list))

for i in my_list:
    print(f"{i} iteration")
    if i == 5:
        break

# while loop
count_a = 3 #number of A's to find

print()
print("While output:")
sequence = 'GATTACAGAACTGATAC'
pos = 0
a_count = 0

while pos < len(sequence) and a_count < count_a: #count the A's until the end of the sequence or until I find enough A's
    if sequence[pos] == 'A':
        a_count += 1
    pos += 1 #check next position
    if a_count == count_a: # if i've found as much A's as I wanted, print the position and break the loop
        print (f"The {a_count}th A is at position {pos - 1} of the sequence")
        break
#at the end of the while loop
if a_count < count_a: #if I reach the end of the sequence and I haven't found enough A's, print a message
    print("There aren't enough A's in the sequence")

a_count = 0
pos = 0

# for loop
print("For output:")
for base in sequence:
    if base == 'A':
        a_count += 1
    pos += 1 #always increment position
    if a_count == count_a:
        print (f"The {a_count}th A is at position {pos - 1} of the sequence")
        break
if a_count < count_a:
    print("There aren't enough A's in the sequence")

#nested loops
print()
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
start_codons = ['ATG']
stop_codons = ['TAA', 'TAG', 'TGA']

for seq in sequences: # iterate for each sequence
  for codon in start_codons: # iterate for each start_codon
    if codon in seq:
      print(f"the start codon {codon} is in {seq} at position {seq.find(codon)}") # find() return the firs occurence, starting from 0
  for codon in stop_codons: # iterate for each stop_codon
    if codon in seq:
      print(f"the stop codon {codon} is in {seq} at position {seq.find(codon)}")

# position filter
print()
print("These are the right codons after the position control:")
for seq in sequences: # iterate for each sequence
  for start in start_codons: # iterate for each start_codon
    if start in seq: # if i find a start codon
        for stop in stop_codons: # i have to search for a stop codon
            if stop in seq: # if i find a stop codon
                if seq.find(stop) > seq.find(start): # and if the stop codon is after the start
                    print(f"the start codon {start} is in {seq} at position {seq.find(start)}") # I've found them with the correct order
                    print(f"the stop codon {stop} is in {seq} at position {seq.find(stop)}")

# patien exercise
print()
data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# Loop through the dict printing each key and each value as a list.
for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

for key_patient, value_bact_list in data.items():  
  print(key_patient)
  print(value_bact_list)
  print('bac889Ytd' in value_bact_list)

# exercise

print()
print("1 Collect the unique bacteria")

#list solution
print("List solution:")
unique_bacteria = [] # empty list
for bacteria_list in data.values(): # for every bacteria's list
    for bacteria in bacteria_list: # for every value of bacteria
        if bacteria not in unique_bacteria: #if that bacteria is not yet in the list
            unique_bacteria.append(bacteria)
print(unique_bacteria)

# set solution
print("Set solution")
bacteria_set = set() # definition of an empty set
for bacteria_list in data.values(): # for every bacteria's list
    for bacteria in bacteria_list: # for every value of bacteria
        bacteria_set.add(bacteria) # add() is the append() method for sets
        #print(f"Added {bacteria}") # check that bacteria are added at each iteration
print(bacteria_set) # but at the end only unique values are stored in the set

print()
print("2 Create the reverse dictionary")
# First step: create a dictionary with the unique bacterias as keys and empty lists as values
# (Identical steps of the first exercise - list version)
bacteria_to_patients = {} #definition of an empty dictionary
for bacteria_list in data.values(): # for every bacteria's list
    for bacteria in bacteria_list: # for every value of bacteria
        if bacteria not in bacteria_to_patients: #if that bacteria is not yet in the dictionary
            bacteria_to_patients[bacteria] = []

# Second step:  append the patient ID to the list belonging to that bacterium
for patient in data.keys(): # for all the patients in data
    for bacteria in data[patient]: # for all the bacterias in the lists
        bacteria_to_patients[bacteria].append(patient) # add that patient as a value of that bacteria key
print(bacteria_to_patients)





