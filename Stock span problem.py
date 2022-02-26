class Solution:
    def calculateSpan(self,arr,n):
        stack = []
        result = []
        span = []
        for i in range(0,n):
            while(len(stack)!=0 and stack[-1][0] <= arr[i]):
                stack.pop()
                
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1][1])
            stack.append([arr[i],i])
            
        for i in range(n):
            span.append(i-result[i])
        return span    
