n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
last = arr[n-1]  //storing last element
for i in range(n-1,0,-1): //traversing array from last
    arr[i] = arr[i-1]
arr[0] = last
print(arr)
    
