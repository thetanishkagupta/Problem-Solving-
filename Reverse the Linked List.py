#Iterative Method

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        current = head
        prev = None
        while(current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        return prev      
      
      
      
#Recursive Method 

class Solution:
    def reverseList(self, head):
        if(head == None or head.next == None):
            return head
            
        new_head = self.reverseList(head.next)
        head_next = head.next 
        head_next.next = head 
        head.next = None 
        return new_head      
