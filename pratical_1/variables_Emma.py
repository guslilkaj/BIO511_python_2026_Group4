
# Variable if/else practice

mystring = "variabletuesday"
len(mystring)

print (len(mystring))

if len(mystring) == 0:
    print ("empty string")
else:
    print ("non-empty")



# Integer multi-way if/elif/else practice
myinteger = -4873

if myinteger == 0:
    print ("Your integer is 0")
elif myinteger > 0:
    print ("Your integer is positive")
else:
    print ("Your integer is negative")



# Nested If/Elif/Else Practice

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]

if type(prime_numbers) is list or tuple or range:
    if len(prime_numbers) ==0:
        print ("empty")
    elif len(prime_numbers) == 1:
        print ("single item")
    else:
        print ("multiple items")
else:
    print ("This is not an accepted variable type")




# Looking up a sample practice

read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}

sample = "sample_A"
passed_qc= True

if read_counts[sample] == False:
    print ("unknown sample")
elif read_counts[sample] == None:
    print ("sequencing failed")
else:
    print ("known sample...")
    if read_counts[sample] >= 1000000 and passed_qc == True:
        print ("ready for analysis")
    else:
        print ("too few reads")
