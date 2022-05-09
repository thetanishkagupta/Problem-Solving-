# Fibonacci sequence is such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        
        
# Another method 
class Solution:
    def nthFibonacci(self, n):
        ans = [0,1]
        for i in range(n):
            ans.append(ans[i] + ans[i+1])
        return ans[n] % 1000000007
  

# Other Method
def fib(n):
    a = 0 
    b = 1 
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2,n):
            c = a + b 
            a = b 
            b = c 
            print(c)
n = int(input())
fib(n)
            
    
# Other method    
def fib(i):
    if i == 0:
        return 0 
    elif i == 1 :
        return 1 
    else:
        return fib(i-2)+fib(i-1)

n = int(input())
for x in range(n):
    print(fib(x))
