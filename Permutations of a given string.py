class Solution:
    def find_permutation(self, string):
        # Code here
        if len(string) == 1:
            return [string]
        
        permutation = []
        for i in range(len(string)):
            currchar = string[i]
            newstr = string[0:i] + string[i+1:]
            perm = self.find_permutation(newstr)
            for p in perm:
                permutation.append(currchar + p)
        unique_result = list(set(permutation))  # remove duplicates and get a unique list of permutations
        return(unique_result)

  
########################

def Perm(string):
    if len(string) == 1 :
        return [string]
        
    permutation = []
    for i in range(len(string)):
        currchar = string[i]
        newstr = string[0:i] + string[i+1:]
        for p in Perm(newstr):
            permutation.append(currchar + p)
    unique_result = list(set(permutation))
    return(unique_result)
    
string = "abb"
ans = Perm(string)
z = set(ans)

for i in z:
    print(i)
            
        
