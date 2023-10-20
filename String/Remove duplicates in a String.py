def duplicates(string):
    freq = {}
    newstring = ""
    
    for i in string:
        if i not in freq:
            freq[i] = True
            newstring += i 
    return newstring
string = "abbccda" 
result = duplicates(string)
print(result)

# Output: abcd

