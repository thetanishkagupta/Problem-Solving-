n = int(input("Enter number of elements in first array: "))
arr1 = list(map(int,input("Enter the elements : ").strip().split()))[:n]
m = int(input("Enter number of elements in second array: "))
arr2 = list(map(int,input("Enter the elements : ").strip().split()))[:m]
union = []
intersection = []
//Union operation
i = 0 
j = 0
while( i<n and j<m):
    if arr1[i]<arr2[j]:
        union.append(arr1[i])
        i += 1 
    elif arr1[i]>arr2[j]:
        union.append(arr2[j])
        j += 1 
    else:
        union.append(arr1[i])
        i += 1 
        j += 1 
//Remaining elements    
while i<n:
    union.append(arr1[i])
    i += 1 
        
while j<m:
    union.append(arr2[j])
    j += 1 
print("Union of the given two array: ",union)    

//Intersection operation 
for i in range(n):
    for j in range(m):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
print("Intersection of the given two array: ",intersection)
        
        
        

    
    
