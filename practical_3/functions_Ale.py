# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

# Count numbers above a limit
print("Count numbers above a limit")
def count_above(seq, lim):
    count = 0
    for i in seq:
        if i > lim:
            count += 1
    return count

print(f"The value of the global variable 'count' is {count}")
x = count_above(nums, limit) #x = count(the value returned at the end of the function)
# # The local variable 'count' only exists when the function is called
print(f"The value of the local variable 'count' contained in the function is {x}")
print(f"The value of the global variable 'count' is still {count}")

# Summarise a text
print()
print("Summarise a text")
def summarize_text(s: str):
    summary = {"digits": 0, "letters": 0, "others" : 0} #remember to use {} for a dictionary and [] for a list
    o = ""
    for character in s:
        if character.isdigit():
            summary["digits"] += 1
        elif character.isalpha():
            summary["letters"] += 1
        else:
            summary["others"] += 1
            o += character
    x = summary["digits"] + summary["letters"] + summary["others"]
    return summary, x, o


print(f"The global summary is: {summary}")
dictionary, tot, others= summarize_text(text) #save the returns(summary, x, o) in variables (dictionary, tot, others)
print(f"This is the summary created using the function: {dictionary}")
print(f"The 'others' characters are: '{others}'")
print(f"The total of the characters is {tot} and the length is exactly {len(text)}")
print(f"This is still the global summary: {summary}")

# Aggregate with a mode
print()
print("Aggregate with a mode")

def aggregate(seq, mode, threshold):
# input -> a number sequence, the mode, a limit
# if mode is sum, sum all the numbers >= limit and return the total
# if mode is count, count how many numbers are >= than the limit
# if mode is max, return the biggest number
    if mode == "sum" or mode == "count":
        result = 0
    elif mode == "max":
        result = None #just to start
    else:
        print("mode not valid")
    
    for n in seq:
        if n < 0: #if the number is negative, ignore it
            continue #skips the rest of the current iteration and moves on to the next number
        elif n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result: # if max, result = n for the first number and after, if n+1(n) > n(result) update result
                    result = n
    return result

print(f"This is the global result: {result}")
somma = aggregate(nums, "sum", limit)
print(somma)
conta = aggregate(nums, "count", limit)
print(conta)
massimo = aggregate(nums, "max", limit)
print(massimo)
print(f"This is still the global result: {result}")

# Errors and try/except
print()
print("Errors and try/except")

values = ['10', '5', 'hello', '8', 'three', '2', 23.4, 'DNA', [1, 3, 4],
{0b00: '00', 0b01: '01', 0b10: '10', 0b11: '11'}, '9']
# I added a float, a list, and a dictionary containing binary keys
# (0b...) and their corresponding binary values as strings.

for value in values:
    try:
        v = int(value)
        print(f"Converted int: {v}")
    except ValueError:
        # invalid literal for int()
        print(f"Skipping invalid value: {value}")
    except TypeError:
        # int() argument must be a string, a bytes-like object or a real number
        print(f"Skipping invalid argument for int(): {value}")
