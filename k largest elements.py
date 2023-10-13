# Input: N = 5, K = 2
# Arr[] = {12, 5, 787, 1, 23}
# Output: 787 23   Explanation: 1st largest element in the array is 787 and second largest is 23.


import heapq
class Solution:

	def kLargest(self,arr, n, k):
		# code here
		max_heap = []    # store elements in a max-heap data structure.
		for i in range(n):
		    heapq.heappush(max_heap, -arr[i])   #For each element arr[i], it turns value into its negative and pushes it onto the max_heap using the heapq.heappush() function. 
		ans = []        # store the k largest elements from the max_heap.
		for j in range(k):
		    ans.append(-heapq.heappop(max_heap))  # It pops the top element of the max-heap using heapq.heappop(), negates the value back to its original form, and appends it to the ans list.
		return ans    


