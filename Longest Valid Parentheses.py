class Solution(object):
    def longestValidParentheses(self, S):
        stack = [-1]
        result = 0
        for i in range(len(S)):
            if (S[i] == "("):
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    result = max(result , (i - stack[-1]))
        return result                     
                
