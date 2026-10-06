sequence1 = "ATGCGTACTTAGCAAT"
sequence2 = "TTAGGCATGCCGATATCGGCTTA"

sequence = sequence2  # or sequence2, depending on which sequence you want to analyze

#1
if sequence[0]  == "G" or sequence[0] == "C":
    print("The sequence starts with a G or C")
else:
    print("The sequence does not start with a G or C")

#2
gc_count = 0
for base in sequence: # base is an iteration variable
    if base == "G" or base == "C":
        gc_count += 1
print("Number of GC content: ", gc_count)

#3
percentage_gc = (gc_count/len(sequence)) * 100
print("Percentage of GC content: ", percentage_gc, "%")