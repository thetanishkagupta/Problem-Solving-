class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # no 3 goes to index 2
            correctPos = nums[i]-1  #correct position for ith no
            while 1 <= nums[i] <= n and nums[i] != nums[correctPos]:
                nums[i] , nums[correctPos] = nums[correctPos] , nums[i] # swapping elements present at ith position and the element at the correct position  
                                                                        # so that current no goes to the correct position 
                correctPos = nums[i]-1  # now nums[i] has changed
                
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1    
                
        
