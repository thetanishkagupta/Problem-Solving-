class Solution:
    def leaders(self, A, N):
        result = []
        max_from_right = -float('inf')
        for i in range(N-1 , -1 , -1):  #iterating from right to left
            if A[i] >= max_from_right:
                result.append(A[i])
                max_from_right = A[i]
                
        result.reverse()
        return result
