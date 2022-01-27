class Solution(object):
    def transpose(self, matrix, n):
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    def reverse(self, matrix):
        for row in matrix:
            row.reverse()
        return matrix
    def rotate(self, matrix):
        n = len(matrix)
        self.transpose(matrix, n)
        self.reverse(matrix)
        return matrix

    
        
