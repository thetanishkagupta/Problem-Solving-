n=int(input("enter the size of array: "))
arr = []
print("enter the elements: ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("reverse string is: ",*arr[::-1])    


