n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
start = 0
end = n-1
while(start<end):
    arr[start] , arr[end] = arr[end] , arr[start]
    start += 1
    end -= 1
print(arr)    
