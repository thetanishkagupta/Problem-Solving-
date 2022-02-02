class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        res = 0
        i = 0
        for j in range(0 , len(s)):
            if s[j] in d:
                i =max(i , (d[s[j]] + 1))
            res = max(res, (j - i + 1))
            d[s[j]] = j 
        return res    
            
