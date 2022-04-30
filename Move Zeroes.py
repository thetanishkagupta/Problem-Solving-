# move all 0's to the end of arr while maintaining the relative order of the non-zero elements.
# if 0 then ignore if non zero then swap

class Solution(object):
    def moveZeroes(self, nums):
        ptr = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[ptr] = nums[ptr],nums[i]
                ptr += 1
        return nums       
