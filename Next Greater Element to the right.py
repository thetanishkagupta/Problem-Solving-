class Solution:
    def nextLargerElement(self,arr,n):
        stack = []
        result = [] #array for storing result
        for i in range(n-1, -1, -1): # traversing the array from right to left
            # to fetch the top element of stack from a list or array use stack[-1](for peek and pop)
            while (len(stack) !=0 and stack[-1] <= arr[i]):
                stack.pop()
                
            if len(stack) == 0: # if stack is empty
                result.append(-1)  # put -1 in result array
            else:
                result.append(stack[-1])  # else pop the top element
            stack.append(arr[i])
            
        result.reverse()
        return result
