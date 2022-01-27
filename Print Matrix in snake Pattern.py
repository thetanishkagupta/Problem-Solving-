class Solution:
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
        l = []
        n = len(matrix)
        for i in range(n):    # Traverse through all rows
            if i % 2 == 0:
                for j in range(len(matrix[i])):     # Traverse the elements of row
                    l.append(matrix[i][j])
            else:        
                for j in range(len(matrix[i])-1 , -1 , -1):
                    l.append(matrix[i][j])
        return l
