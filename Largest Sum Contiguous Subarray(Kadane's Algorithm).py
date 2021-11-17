n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
max = -float('inf') 
max_till_here = 0
for i in range(n):
    max_till_here = max_till_here + arr[i]
    if max_till_here > max:
        max = max_till_here
    if max_till_here < 0:
        max_till_here = 0
print("largest contiguous sum is: ",max)        


