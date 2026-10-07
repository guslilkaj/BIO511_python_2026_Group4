sequence = "ATAGGCATGCCGATATCGGCTTA"
gc_count = 0


if sequence[0] == ("G" or "C"):
    print("first base is C/G")
else:
    print("first base is A/T")

#iterates through each letter of the string in var - sequence and adds to gc_count whenever one matches.
for x in range(len(sequence)):
    if sequence[x] in "GC":
        gc_count += 1
gc_percentage = len(sequence) / gc_count
print("GC count of " + str(gc_count) + ". " + str(gc_percentage) + "%. of sequence")
print(len(sequence))
