# You are given an integer N.
# Print numbers from 1 to N without the help of loops.

class Solution:
    def printTillN(self, N):
    	if (N == 0):
    	    return 0
    	self.printTillN(N-1)
    	print(N, end = " ")
