# Fibonacci sequence is such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
       
