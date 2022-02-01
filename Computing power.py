# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

class Solution(object):
    def myPow(self, x, n):
        ans = 1.0
        temp = n                # store power in a temporary variable
        if temp < 0:            # make the power positive
            temp = -1 * temp
        while (temp > 0): 
            if temp % 2 == 1:   # if power is odd
                ans = ans * x
                temp = temp -1
            else:               # if power is even
                x = x * x
                temp = temp // 2
        if n < 0:               # if power is negative
            ans = 1.0 / ans
        return ans    
