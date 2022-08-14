# Input: s = "leetcode"
# Output: 0

# Input: s = "loveleetcode"
# Output: 2

class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in s:
            if freq[i] == 1:
                return s.index(i)
        return -1
