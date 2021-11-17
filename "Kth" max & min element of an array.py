//for minimum element
n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
k = int(input("Enter the kth minimum element: "))
arr.sort()
print("Kth minimum element is: ",arr[k-1])


//for maximum element
n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter the elements: ").strip().split()))[:n]
k = int(input("Enter the kth maximum element: "))
arr.sort(reverse = True)
print("Kth maximum element is: ",arr[k-1])
