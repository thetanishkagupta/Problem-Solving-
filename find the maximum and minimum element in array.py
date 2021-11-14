N = int(input("Enter number of elements: "))
Arr = list(map(int,input("Enter the elements: ").strip().split()))[:N]
print("The minimum element is", min(Arr))
print("The maximum element is", max(Arr))        
