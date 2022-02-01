class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            if s[i] == goal[0]:                   # check if goal's first letter is in s
                if s[i : ] + s[ : i] == goal:     # cut string till i from front and add in the end
                    return True
        return False
                
        
