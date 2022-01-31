# Find two lines that together with the x-axis form a container, such that the container contains the most water.

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:    # calculate the water level
            min_height = min(height[left] ,height[right])
            max_area = max(max_area , min_height * (right-left))   # check if area is greater than previous area
            if (height[left] < height[right]):
                left += 1    # move left pointer ahead
            else:
                right -= 1   # move right pointer back
        return max_area        
                
                
        
