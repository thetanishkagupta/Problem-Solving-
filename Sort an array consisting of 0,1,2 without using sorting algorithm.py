n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
c0 = 0
c1 = 0
c2 = 0
for i in range(n):
    if arr[i] == 0:
        c0 += 1
    if arr[i] == 1:
        c1 += 1
    if arr[i] == 2:
        c2 += 1
        
k = 0
for i in range(c0):
    arr[k] = 0
    k += 1
for i in range(c1):
    arr[k] = 1
    k += 1
for i in range(c2):
    arr[k] = 2
    k += 1
        
print(arr)


# Dutch National Flag Algorithm
