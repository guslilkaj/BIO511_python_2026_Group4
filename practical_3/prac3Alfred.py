# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

def count_above(seq, lim):
    count=0
    for seq_instance in seq:
        if seq_instance > lim:
            count += 1
    return count

print(count)

answer = count_above(nums, limit)
print(answer)


def summarize_text(s):
    summary = {
    'digits':  0,
    'letters': 0,
    'other':   0,
    }
    
    for s_instance in s: #checks each letter in the string in sequence
        if s_instance.isdigit(): #if letter is a number, adds to the integer entry in the dict
            summary['digits'] += 1
        elif s_instance.isalpha(): #does the same for letters
            summary['letters'] += 1
        else: #puts everything else in the "other" entry
            summary['other'] += 1
    return summary
answer = summarize_text(text)
print(answer)

if sum(answer.values()) == len(text):
    print("every character in the string has been properly counted")
else:
    print("ERROR: character count does not match string length")



def aggregate(seq, mode, treshold):
    if mode is "sum": #sum adds all the values (above threshold) in the list together
        result = 0
    elif mode is "count": #counts the amount of values in the list that clear the threshold
        result = 0
    elif mode is "max": #max finds the biggest number
        result = None
    for n in seq:               #grabs a number from the list and checks if its negative skips the rest of the for-loop, leaving the result as 0 or none
        if n < 0:               #skips all negative numbers
            continue
        elif n >= treshold:     #if the number is above or at the threshold value (4)
            if mode is "sum":   #if we're summarizing, it will take every positive value above threshold and add it together
                result += n
            elif mode is "count": #if we're counting the values, it just adds one for each above threshold
                result += 1
            else:
                mode = "max"  #just defaults to max mode if no valid mode was input
                if result == None or n > result: #sets result to the highest value
                    result = n
    return result
print(result)

call1 = aggregate(nums, "sum", limit)
call2 = aggregate(nums, "count", limit)
call3 = aggregate(nums, "max", limit)

print(call1)
print(call2)
print(call3)
print(result)