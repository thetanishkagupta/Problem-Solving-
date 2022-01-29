# Find the Winner of the Circular Game
def pos(n,k):
    if(n==1):
        return 0
    else:
        return (pos(n-1,k)+k)%n
    
class Solution(object):
    def findTheWinner(self, n, k):
        return pos(n,k) + 1
