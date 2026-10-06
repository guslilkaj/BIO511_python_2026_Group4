# Data types: integer, floating point, string, boolean,
# NoneType, list, dictionary, tuple, set, range

i = 3
f = 2.14
s = "Hello World"
b = True
none_value = None
my_list = [3, 4, "ciao", 6] # ordered and mutable collection of elements
dictionary = {"g1": "ATGTTGACC", "g2": "GGCCTATT"}
my_tuple = (10, 40, 30, 10) # ordered and immutable collection of elements (ex: coordinates)
my_set = {"Homo sapiens", "E.coli", "S.cerevisiae", "Homo sapiens"} # unordered and mutable collection of unique elements (ex: species)
# A set automatically removes duplicate elements.
my_range = range(5)

print("the variable i has value", i, "and type", type(i))
print("the variable f has value", f, "and type", type(f))
print("the variable s has value", s, "and type", type(s), "and length", len(s))
print("the variable b has value", b, "and type", type(b))
print("the variable none_value has value", none_value, "and type", type(none_value))
print("the variable my_list has value", my_list, "and type", type(my_list))
print("the variable dictionary has value", dictionary, "and type", type(dictionary))
print("the variable my_tuple has value", my_tuple, "and type", type(my_tuple))
print("the variable my_set has value", my_set, "and type", type(my_set))
print("the variable my_range has value", my_range, "and type", type(my_range))

# length of a string
print() # Empty line as separator
if len(s) > 0:
    print("The string s is not empty")
else:
    print("The string s is empty")

# Multi-way chek of i
print()
if i > 0:
    print("The integer i is positive")
elif i == 0:
    print("The integer i is zero")
else:
    print("The integer i is negative")

# Nested if/else statement
print()
if type(my_tuple) == list or type(my_tuple) == tuple or type(my_tuple) == range:
    if len(my_tuple) == 0:
        print("The variable is empty")
    elif len(my_tuple) == 1:
        print("The variable has one element")
    else:
        print("The variable has multiple elements")
else:
    print("The variable is not a list, tuple or range")

# Sample dictionary
print()
read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}
sample = "sample_C"
if sample not in read_counts:
    print("The sample is not contained in this dictionary")
elif read_counts[sample] is None:
    print("Sequencing failed for this sample")
elif read_counts[sample] > 1000000:
    print("Enaugh reads")
else:
    print("Too few reads")