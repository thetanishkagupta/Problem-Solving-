class Solution:
	def count(self,arr, n, x):
		freq = {}
		for i in arr:
		    if i in freq:
		        freq[i] += 1
		    else:
		        freq[i] = 1
		for i in freq:
		    if i == x:
		        return freq[i]
		return 0        
