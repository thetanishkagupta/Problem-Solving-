n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
i = -1
pivot = 0 
for j in range(n):
    if arr[j] < pivot :
        i += 1 
        temp = arr[i]
        arr[i] = arr[j]
        arr[j]= temp
        
print(arr)        


    
    
