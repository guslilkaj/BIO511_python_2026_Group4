Test_list = ["a", "b", "c", "d", "e", "f", "g"]


for index, name in enumerate(Test_list):
    print(index, name)
    if index >= 5:
        break
    

sequence = 'GATTACAGAACTGATAC'
a_count=0
indexnr=0
count_a=3

#while-loop version
while a_count < 3:
    if sequence[indexnr] == "A":
        a_count += 1
        indexnr += 1
    else:
        indexnr += 1
print("A count: " + str(a_count))
print("third A position: " + str(indexnr))



#for-loop version
for index2, base in enumerate(sequence):
    if a_count >= count_a:
            print("third A position: " + str(index2))
            break
    elif base == "A":
        a_count += 1
print("A: " + str(a_count))




sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']
for sequence in sequences:
  for codon in codons:
    if codon in sequence:
      print(codon + " is in " + sequence)

#step 1: grabs sequence 1 from sequences.
#step 2: grabs codon 1 from codons
#step 3: checks if codon 1 exists in sequence 1.
#then it grabs codon 2 and checks it against sequence 1 until all codons have been checked. Then it grabs sequence 2 etc. 


sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
start_codon = ['ATG']
stop_codon = ['TAA', 'TAG', 'TGA']

#for each sequence, for each start codon, for each stop codon.
for seqindex, sequence in enumerate(sequences):
    for start_var in start_codon:
        for stop_var in stop_codon:
            if start_var and stop_var in sequence:
                #find syntax: looks in sequence for (_var)'s and outputs the position they find the first instance in.
                pos_start = sequence.find(start_var)
                pos_stop = sequence.find(stop_var)
                if not pos_start == -1 and not pos_stop == -1:
                    if pos_start < pos_stop:
                        print("sequence " + str(seqindex) + ": detected start- and stop codons in correct relative positions. Start (" +start_var + ") base: " + str(pos_start) + " and stop (" + stop_var + ") base: " + str(pos_stop))


data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

unique_bacteria = []
bacteria_to_patients = {}

#loop through each entry in the index
for key_patient, bact_list in data.items():
    for bacteria_instance in bact_list:
        #if bacteria isn't in unique_bacteria list, add it to list
        if not bacteria_instance in unique_bacteria:
            unique_bacteria.append(bacteria_instance)

#adds every entry into the unique_bacteria list as a key with an empty list
for entry in unique_bacteria:
    bacteria_to_patients[entry] = []
print(bacteria_to_patients)

#finds the values of the bacteria_to_patients dict in the data dict and adds the patient keys associated with each gene (key) to its respective list
for key_patient, bact_list in data.items():
    for bact_instance in bact_list:
        if bact_instance in bacteria_to_patients:
            #important tool to go back to! Below is how you append a list inside of a dict.
            #syntax: dict[list_in_dict].append(value_to_insert)
            bacteria_to_patients[bact_instance].append(key_patient)

print(bacteria_to_patients)