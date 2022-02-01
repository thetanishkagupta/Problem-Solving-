string1 = input("Enter the string1: ")
string2 = input("Enter the string2: ")
if len(string1) != len(string2):
    print ("Strings size are not same")

temp = string1 + string1   # concatenating string1 twice
if string2 in temp:        # searching string 2 in concatenated string
    print ("Strings are rotations of each other") 
else:
    print ("Strings are not rotations of each other")
