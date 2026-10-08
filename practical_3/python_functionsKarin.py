#Defining and calling a function - examples from the practical
'''
def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return

my_added_numbers = add_two_numbers(1, 1)

print(my_added_numbers) # will print 2
'''

#All three exercises use the variables below. Copy them into the top of your script, outside of any function, and do not rename them
# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

#Write a function that counts how many numbers in a list are larger than a limit.

#efine the function.

#Define a function named count_above that takes two arguments: seq and lim.
#count_above
print("Count numbers above a limit")
def count_above(seq, lim):
#Create a local counter.
#Inside the function, create a local variable named count that starts at 0.
    count=0
#Count the numbers.
#Loop through seq. For each number that is strictly greater than lim, increase count by 1.
    for i in seq:
        if i > lim:
            count += 1
#Return the result.
#Return count from the function.
    return count
#Call the function.
#Outside the function:
#Print the global count.
#Call count_above(nums, limit) and print the returned number.
#Print the global count again.
#Why is the global count still 999, even though the function set a variable called count to 0 and then increased it?