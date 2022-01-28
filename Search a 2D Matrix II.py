# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom

class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        cols = len(matrix[0])
        row_index = 0
        cols_index = cols - 1
        while(row_index < row and cols_index >= 0):
            num = matrix[row_index][cols_index]
            if(num == target):
                return True
            elif(num < target):
                row_index += 1
            else:
                cols_index -= 1  
        return False   
