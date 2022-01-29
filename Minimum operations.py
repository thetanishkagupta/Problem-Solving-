# the minimum number of operations required to make all the elements of array equal to zero.
# make subarrays

n = int(input())
Arr = list(map(int,input().strip().split()))[:n]
count = 1
for i in range(1,n):
    if Arr[i] != Arr[i-1]:
        count += 1
print(count)           
