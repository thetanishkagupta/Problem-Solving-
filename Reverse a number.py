n = int(input("Enter the number: "))
rev = 0
while n>0:
    last_digit = n%10
    rev = rev*10 + last_digit
    n = n//10
print(rev)    


# Other Methode(Slicing)

n = int(input("Enter the number: "))
print(str(n)[::-1])
