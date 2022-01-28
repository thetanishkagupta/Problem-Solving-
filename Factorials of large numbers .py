class Solution:
    def factorial(self, N):
        fact = 1
        i = 1
        while i <= N:
            fact = fact * i
            i += 1
        return str(fact)   
