class Solution(object):
    def majorityElement(self, nums):
        p = math.floor(len(nums)/2)
        freq = {}
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        for i in freq:
            if freq[i] > p:
                return i
                break
        return -1     
