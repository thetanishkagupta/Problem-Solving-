# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 
# k = 3
# 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 


class Solution:
    def reverse(self,head, k):
        prevptr = None
        currptr = head
        nextptr = None
        
        count = 0
        while(currptr != None and count < k):
            nextptr = currptr.next
            currptr.next = prevptr
            prevptr = currptr
            currptr = nextptr
            count += 1
            
        if nextptr != None:
            head.next = self.reverse(nextptr, k)    
        
        return prevptr
