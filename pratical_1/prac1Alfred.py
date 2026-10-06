var_int = int(-4)
var_string = "oy"
var_float = float(5.4)
var_complex = complex(1j)
var_list = list(("a", "b"))
var_range = range(5)
var_dict = dict(name="John", age=20)
var_bool =bool(4)

string_length_check = ""

print("the variable " + str(var_int) + " is of the " + str(type(var_int)))
#do the same for all others


if len(string_length_check) == 0:
    print("empty")
else:
    print("non-empty")


if var_int >= 0:
    print("positive integer")
elif var_int == 0:
    print("null")
elif var_int <=0:
    print("negative integer")



if var_list == list or tuple or range:
    if len(var_list) == 0:
        print("empty")
    elif len(var_list) == 1:
        print("single item")
    elif len(var_list) >= 1:
        print("multiple items")
else:
    print("wrong data type")



read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}


#print("sample_B" in read_counts)

#if sample doesn't exist, print unknown sample. if value = none, print sequencing failed
for sample in read_counts:
    if not sample in read_counts:
        print(sample + ": unknown sample")
    elif read_counts[sample] == None:
        print(sample + ": sequencing failed")
    elif read_counts[sample] >= 1000000 or read_counts[sample] == 1000000 and passed_qc == True:
        print(sample + ": ready for analysis")
    else:
        print(sample + ": too few reads or didn't pass QC")