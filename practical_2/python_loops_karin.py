# Example code

# Make a list
mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
# You can double check if it's a list
type(mylist)

# print your list
print(mylist)

# print the first item in your list
print(mylist[0])

sequence = 'GATTACAGAACTGATAC'

#Your task is to find the position of the third A in the sequence. 
#Use zero-based indexing, so the first character is at position 0

#To double check I check manually what I expect to find as a result later
#The third A in the sequence "sequence" is in position 6 because the first base is position 0

#look up PEP8 as a styleguide for python committee on how to write with good practices

position = 0
A_count = 0

while A_count < 3:
    if sequence[position] == 'A':
        A_count += 1
    position += 1

third_A_position = position - 1
#this is now an f-string -requiring the curly brachets 
print(f"A_count: {type(A_count)}")
print(f"sequence: {type(sequence)}")
print(f"mylist: {type(mylist)}")
print(f"This is the position where the third A in the 'sequence' is found: {third_A_position}")
#another option is to convert this into a string by using "str()"
#stylistically an f-string is more on par with regular coding
