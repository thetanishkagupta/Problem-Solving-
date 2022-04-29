# add the index of a element and put it in to the desired indexed list according to their sum.
# put all the odd indexed list element as it is in the result 
# whenever we have even indexed list we will reverse the list element and then add to the result

class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:   # empty matrix
            return []
          
        row, cols = len(matrix), len(matrix[0])
        diagonals = [[] for _ in range(row + cols -1)]
        for i in range(row):
            for j in range(cols):
                diagonals[i+j].append(matrix[i][j])
                
        result = diagonals[0]
        
        for x in range(1, len(diagonals)):
            if x % 2 == 1:
                result.extend(diagonals[x])         # odd index case
            else:                                   #The extend() method adds the specified list elements (or any iterable) to the end of the current list.
                result.extend(diagonals[x][::-1])   # even index case
        return result        
                
        
