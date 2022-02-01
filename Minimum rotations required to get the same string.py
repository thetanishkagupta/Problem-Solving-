string = input("Enter the string: ")
check = " "
n = len(string)
for i in range(1, n + 1):
    check = string[i : ] + string[ : i]     # checking the input after each rotation
    if check == string:         # checks if input is equals to check
        print(i)
        break
