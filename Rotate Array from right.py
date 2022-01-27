class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums) # needed for cases when k is equal or longer than the length of the array
        
        if k ==0: # no change needed
            return nums
        
		#1 reverse the whole array
        l,r = 0, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            
            l +=1
            r -=1
            
        #2 reverse the first k items
        l,r = 0, k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            
            l +=1
            r -=1
            
		#reverse the remaining items	
        l,r = k, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            
            l +=1
            r -=1
            
        return nums
        
