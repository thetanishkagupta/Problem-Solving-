# an array of digit strings nums and a digit string target,
# return the number of pairs of indices (i, j)
# (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

class Solution(object):
    def numOfPairs(self, nums, target):
        n = len(nums)
        ans = 0
        for i in range(0,n):
            for j in range(0,n):
                if i == j:
                    continue
                if (nums[i] + nums[j] == target):
                    ans += 1
            j += 1
        i += 1    
        return ans
