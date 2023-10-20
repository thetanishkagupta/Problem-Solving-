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
    
string = "abc"
ans = Perm(string)
print(ans) 


# Output: ['cba' , 'abc' , 'acb' , 'bac' , 'bca' , 'cab']

