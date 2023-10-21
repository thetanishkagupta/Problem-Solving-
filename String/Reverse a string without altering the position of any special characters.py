string = "a!b@c#d$e%f"
s = list(string)               # string is converted into a list of characters 
left = 0                       # left end of the string
right = len(s) - 1             # right end of the string
specialchar = "!@#$%"
while left < right:
    if s[left] in specialchar:
        left += 1
    elif s[right] in specialchar:
        right -= 1 
    else:
        s[left],s[right] = s[right] , s[left] 
        left += 1 
        right -= 1 
print(''.join(s))        


# Output: f!e@d#c$b%a

