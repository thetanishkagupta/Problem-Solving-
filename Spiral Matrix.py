class Solution(object):
    def spiralOrder(self, matrix):
        ans = []
        top = 0
        left = 0
        bottom = len(matrix) - 1     # row 
        right = len(matrix[0]) - 1   # column
        direction = 0                # left to right
        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(top, right + 1):
                    ans.append(matrix[top][i])
                top += 1
            elif direction == 1:     # top to down
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direction == 2:     # right to left
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1          # decrement the value of down
            elif direction == 3:     # down to top
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1            # increasing the left pointer
            direction = (direction + 1) % 4
        return ans
        
