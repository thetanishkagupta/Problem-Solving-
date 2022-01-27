#To rotate the matrix by 90 degrees (anti-clockwise or left).
#First of all, reverse the matrix and then transpose it.

class Solution:
    def transpose(self,matrix,n):
        for i in range(n):
            for j in range(i,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        return matrix
        
    def reverse(self,matrix):
        for row in matrix:
            row.reverse()
        return matrix 
        
    def rotateMatrix(self,matrix, n):
        self.reverse(matrix)
        self.transpose(matrix,n)
        return matrix
