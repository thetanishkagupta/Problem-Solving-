# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dic = {}
        for v in nums2:
            while stack and stack[-1]<v:
                k = stack.pop()
                dic[k] = v
            stack.append(v)
        print(dic)
        return [dic.get(v , -1) for v in nums1]     # v is treated as key for dictionary
            
            
