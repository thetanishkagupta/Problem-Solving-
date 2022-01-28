# NOTE
# - Row index of any element in matrix can be found using: -
# index of that element in the 1-D array / number_of_columns_in_matrix
# - Column index of any element in matrix can be found using: -
# index of that element in the 1-D array % number_of_columns_in_matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]  #note
            if num == target:
                return True
            elif num < target:
                 low = mid + 1
            else:
                high = mid - 1
        return False
            
