# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"


## Counting numbers above a limit

def count_above (seq, lim):
    count=0
    for n in seq:
        if n > lim:
            count += 1
    return count


## This output does not alter the global count value of 999 because the 
## other count value is local, and thus does not augment the global value
print (count)
count_above (nums, limit)
print (count)





## Summarizing a text

def summarize_text(s):
    summary = {
        "digits": 0,
        "letters": 0,
        "other": 0,
    }

    for char in s:
        if char.isdigit():
            summary["digits"] += 1
        elif char.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

print (summary)
print (summarize_text(text))
print (summary)





# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"


## Aggregate with a mode

def aggregate (seq, mode, threshold):
    result = None
    if mode == "sum" or mode == "count":
        result = 0
    elif mode == "max":
        result = None
    else:
        print ("result input not appropriate")
    

    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result == None or n > result:
                    result = n
    return result


print (result)
print (aggregate(nums, "sum", limit))
print (aggregate(nums, "count", limit))
print (aggregate(nums, "max", limit))
print (result)

print (aggregate(nums, "max", 100))





## Errors and try/except

values = ['10', '5', 'hello', '8', 'three', '2']

for n in values:
    try:
        n = int(n)
        print (n)
    except ValueError:
        print ("Skipping invalid value: " + n)
        continue
