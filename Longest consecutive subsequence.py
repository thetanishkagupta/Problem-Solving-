# Input:
# N = 7
# a[] = {2,6,1,9,4,5,3}
# Output: 6   (i.e -> 1,2,3,4,5,6)

def findLongestConseqSubseq(self,arr, N):
  arr = list(set(arr))
  arr.sort()
  count , ans = 1, 1   # count keeps track of the current consecutive sequence length, and ans stores the maximum length found so far.
  for i in range(1,len(arr)):
  if (arr[i] == arr[i-1] + 1):   # it checks if the current element arr[i] is one greater than the previous element arr[i-1]
    count += 1
    ans = max(ans,count)
  else:     # If the current element arr[i] is not one greater than the previous element, it means the consecutive sequence has been broken.
    count = 1
return ans 
                
           
                
               
