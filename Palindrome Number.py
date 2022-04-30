class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = x
        rev = 0
        while temp:   #reverse the number
            s = temp % 10
            rev = (rev * 10) + s
            temp = temp // 10
        if rev == x:     #compare the temporary number with reversed number
            return True
        else:
            return False

        

# Another method
class Solution(object):
    def isPalindrome(self, i):
        rev = 0
        x = i
        while(i>0):
            rev = (rev * 10) + i % 10
            i = i // 10
        if x == rev:
            return True
        else:
            return False
