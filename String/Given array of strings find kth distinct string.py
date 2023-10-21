arr = ["a", "b", "c", "a"]
k = 2
output = []                   # unique characters found in the array
for char in arr:
    if arr.count(char)==1:
        output.append(char)
if k > 0 and k <= len(output):     # If k is within a valid range
    print(output[k-1])
else:
    print(None)

# Output: c

