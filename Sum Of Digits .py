# Sum of 12's digits:
# 1 + 2 = 3

class Solution:
    def sumOfDigits (self, N):
        s = 0
        while(N):
            r = N % 10
            s = s + r
            N = N // 10
        return s    
