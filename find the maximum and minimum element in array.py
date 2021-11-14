n=int(input("enter the size of array: "))
arr = []
print("enter the elements: ")
for i in range(n):
    element=int(input())
    arr.append(element)
    
print("The minimum element in the list is", min(arr))
print("The maximum element in the list is", max(arr))                        
