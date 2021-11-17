n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
previous = 0
current = 0 
jumps = 0
for i in range(n):
    if(i > previous):
        jumps = jumps + 1
        previous = current
        
    current = max(current, i + arr[i])
print("Minimum no. of Jumps to reach end of an array is: ",jumps)
