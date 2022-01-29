class Solution:
    def printTillN(self, N):
    	if (N == 0):
    	    return 0
    	print(N, end = " ")
    	self.printTillN(N-1)
