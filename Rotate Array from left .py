class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        temp = []
        i = 0
        while (i < D):
            temp.append(A[i])
            i = i + 1
        i = 0
        while (D < N):
            A[i] = A[D]
            i += 1
            D += 1
        A[:] = A[: i] + temp
        return A
