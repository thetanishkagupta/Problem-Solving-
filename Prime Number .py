# A prime number is a number which is only divisible by 1 and itself.


from math import sqrt
class Solution:
    def isPrime (self, N):
        if ( N==1):
            return 0
        else:
            for i in range(2, int(sqrt(N) + 1 )):
                if ( N % i == 0):
                    return 0
        return 1        
