class Solution(object):
    def nextSmallerElementToTheLeft(self,arr):
        nselIndex = []
        s = []
        for i in range(0 , len(arr)):
            while(len(s) != 0 and s[-1][0] >= arr[i]):
                s.pop()
            if len(s) == 0:
                nselIndex.append(-1)
            else:
                nselIndex.append(s[-1][1])
            s.append([arr[i] , i]) 
        return nselIndex
    
    def nextSmallerElementToTheRight(self,arr):
        nserIndex = []
        s = []
        for i in range(len(arr)-1, -1, -1):
            while(len(s) != 0 and s[-1][0] >= arr[i]):
                s.pop()
            if len(s) == 0:
                nserIndex.append(len(arr))
            else:
                nserIndex.append(s[-1][1])
            s.append([arr[i] , i])
        nserIndex.reverse()
        return nserIndex
                
    def largestRectangleArea(self, heights):
        left = self.nextSmallerElementToTheLeft(heights)
        right = self.nextSmallerElementToTheRight(heights)
        ans = []
        maxArea = 0
        for i in range(len(heights)):
            ans.append((right[i] - left[i] - 1) * heights[i])
            if(maxArea < ans[i]):
                maxArea = ans[i]
        return maxArea

        
