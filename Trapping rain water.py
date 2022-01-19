class Solution(object):
    def trap(self, a):
        n = len(a)
        left = [0] * n
        right = [0] * n
        left[0] = a[0]
        for i in range(1,n):
            left[i] = max(left[i-1] , a[i])
        right[n-1] = a[n-1]   
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1] , a[i])
        
        ans = 0
        for i in range(1,n):
            ans += min(left[i] , right[i]) - a[i]
        return ans    
