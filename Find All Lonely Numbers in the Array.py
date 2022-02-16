# A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

class Solution(object):
    def findLonely(self, nums):
        freq = {}
        lonely = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in freq:
            if (freq[i] == 1) and (i+1 not in freq) and (i-1 not in freq):
                lonely.append(i)
        return lonely    
