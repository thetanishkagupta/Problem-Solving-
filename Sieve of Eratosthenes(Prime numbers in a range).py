class Solution:        
    def primeRange(self,M,N):
        prime = [True] * (N + 1)  #generating boolean array
        prime[0] = False
        prime[1] = False
        for i in range (2, int(math.sqrt(N)) + 1):
            if prime[i] == True:  #if no is prime
                for p in range(i*i , N+1 , i):#(start , end , increment)
                    prime[p] = False
        ans = []
        for i in range(M , len(prime)):
            if prime[i] == True:
                ans.append(i)
        return ans        
                
