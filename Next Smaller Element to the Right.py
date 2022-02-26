class Solution:
    def nextSmallerElementToRight(self, arr, n):
        stack = []
        result = []
        for i in range(n-1, -1, -1): #iterating from right to left
        # we have to pop when stack is having greater element
            while(len(stack)!=0 and stack[-1] >= arr[i]):
                stack.pop()
                
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(arr[i])
        result.reverse()    
        return result    
