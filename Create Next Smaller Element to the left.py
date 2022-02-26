class Solution:
	def nextSmallerElementToTheLeft(self, arr):
        stack = []
        result = []
        n = len(arr)
        for i in range(0,n): #iterating from right to left
        # we have to pop when stack is having greater element
            while(len(stack)!=0 and stack[-1] >= arr[i]):
                stack.pop()

            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(arr[i])
        return result    
