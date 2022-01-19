class Solution:
	def search(self,arr, n, k): 
    	flag = 0
    	for i in range(n):
    	    if arr[i] == k:
    	        flag = 1
    	        break
    	    else:
    	        flag = 0
    	if flag == 1:
    	    return i+1
    	else:
    	    return -1
