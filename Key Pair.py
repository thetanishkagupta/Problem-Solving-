# Determine whether or not there exist two elements in Arr whose sum is exactly X.

class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		# code here
		summ=sum(arr)
    nums=arr
    target=x
    d={}
    for i in range(len(nums)):
      diff=target - nums[i]
      if diff in d:
        return True
      d[nums[i]]=i
    return False   
