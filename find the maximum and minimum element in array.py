n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
if n==1:
    max = arr[0]
    min = arr[0]
    
if arr[0] > arr[1]:
    max = arr[0]
    min = arr[2]
else:
    max = arr[1]
    min = arr[0]
    
for i in range(2, n):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]
 
print("maximum element: ",max)
print("minimum element: ",min)
    
    
    
