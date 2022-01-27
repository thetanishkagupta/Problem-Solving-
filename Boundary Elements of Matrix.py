class Solution:
	def BoundaryElements(self, matrix):
		ans = []
        n = len(matrix)
        for i in range(n):
            for j in range(len(matrix[i])):
                if (i == 0):        # First Row
                    ans.append(matrix[i][j])
                elif (i == n-1):    # Last Row
                     ans.append(matrix[i][j])
                elif (j == 0):      # First Column 
                     ans.append(matrix[i][j])
                elif (j == len(matrix[i])-1):    # Last Column
                     ans.append(matrix[i][j])
        return ans
