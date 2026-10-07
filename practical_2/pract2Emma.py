
# TO COPY AND PASTE MY LOOPS PRACICAL INFORMATION HERE!

# Creating a simple loop

mylist = ["red", "blue", "purple", "black", "yellow", "pink", "beige"]

for i in range (len(mylist)):
    print (i + 1, mylist[i])

    if i + 1 == 5:
        break




# While loops practice

sequence = 'GATTACAGAACTGATAC'

position = 0
a_count = 0

while a_count < 3:
    if sequence[position] == "A":
        a_count = a_count + 1
    position += 1

third_position = position - 1
print (third_position)



# For Loop to solve the same problem!

sequenceee = 'GATTACAGAACTGATAC'
a_counter = 0
position = 0

for n in sequenceee:
    if n == "A":
        a_counter += 1

        if a_counter == 3:
            print (position)
            break
    position += 1



# Nested loop practice

## Sequences is a LIST type variable storing genetic sequence information. List of strings.
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']

## Codons is ALSO a LIST type variable storing relevant 3-letter codons. List of strings.
codons = ['CCA', 'TGT', 'GTA', 'TAG']


## Steps through sequences, for each string within sequences, each string in 'codons' is compared. 
## Each of the 4 codons are compared against the first sequence in 'sequences'. Then each of the codons are compared against the second sequence in sequences.
## If a 'match' is identified, and the codon does have a syntax match to sequences, it will print the match

for sequence in sequences:
  for codon in codons:
    if codon in sequence:
      print(codon + " is in " + sequence)



# My nested loop example
new_sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
stopcodons = ['TAA', 'TAG', 'TGA']

# Create a Nested loop structure to check new_seq for presence of... 
# BOTH *USING AND* start and stop codons

for step in new_sequences:
    for codon in stopcodons:
        if codon in step and "ATG" in step:
            if step.find("ATG") < step.find(codon):
                print (codon + " comes after ATG in " + step)





# Desert name directory... Category, Flavor. 
## Just practicing here to make a iterate thru a direct 

data = {
    'Muffin': ['Banana Nut', 'Lemon', 'Pumpkin'],
    'Cookie': ['Chocolate Chip', 'Oatmeal Raisin'],
    'Cake': ['Carrot', 'Red Velvet', 'Chocolate', 'Cheese']
}

# Now, looping through the dict printing each key and value as a list
for category, flavor in data.items():
    print (category)
    print (flavor)
    print ("Do you wanna get a sweet treat???")






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

## REVERSING THE DICTIONARY
unique_bacteria = []

for value_bact_list in data.values():
    for bacteria in value_bact_list:
        if bacteria not in unique_bacteria:
            unique_bacteria.append(bacteria)
print(unique_bacteria)



### Creating a reverse directory here
bacteria_to_patients = {}

for bac in unique_bacteria:
    if bac not in bacteria_to_patients:
        bacteria_to_patients[bac] = []
        
print (bacteria_to_patients)



## Finally, adding the patients to the newly reversed direct

for patient, bacteria_list in data.items():
    for bact in bacteria_list:
        bacteria_to_patients[bact].append(patient)

print (bacteria_to_patients)

## Output should be something like:
## 98 - patient 1, 3
## Ytd - patient 1,3
## Frr - patient 2
## 55Hj - patient 3
