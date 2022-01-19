class Solution(object):
    def majorityElement(self, nums):
        p = math.floor(len(nums)/3)
        freq = {}
        lst = []
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
                
        for i in freq:
            if freq[i] > p:
                lst.append(i)
        return lst      
