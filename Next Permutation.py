class Solution(object):
    def nextPermutation(self, nums):
        pivot = 0
        n = len(nums)
        
        #find pivot
        for i in range(n-1,0,-1):
            if nums[i-1] < nums[i]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return
        
        #then find the swap which first number > pivot
        swap = n-1
        while nums[pivot-1] >= nums[swap]:
            swap -= 1
            
        #swap    
        nums[swap] , nums[pivot-1] = nums[pivot-1] , nums[swap]
        
        #reverse from pivot
        nums[pivot:] = sorted(nums[pivot:])
        
        
