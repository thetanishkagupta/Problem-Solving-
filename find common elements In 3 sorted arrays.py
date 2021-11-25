class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i = 0
        j = 0
        k = 0 
        res = []
        while (i<n1 and j<n2 and k<n3):
            if(A[i]==B[j]==C[k]):    
                res.append(A[i])
                i += 1 
                j += 1
                k += 1
            elif(A[i]<B[j]):       
                i += 1 
            elif(B[j]<C[k]):
                j += 1 
            else:
                k += 1
                
            xx = A[i-1]                
            while((i>0 and i<n1) and (A[i-1]==A[i])):
                i += 1 
            yy = B[j-1]
            while((j>0 and j<n2) and (B[j-1]==B[j])):
                j += 1
            zz = C[k-1]
            while((k>0 and k<n3) and (C[k-1]==C[k])):
                k += 1
                
        return res
        
