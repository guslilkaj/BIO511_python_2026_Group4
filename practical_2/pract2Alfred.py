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


