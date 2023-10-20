def duplicate(string, index,count,newstring):
    if len(string) == index:
        for i in range(count):
            newstring += 'x'
        print(newstring)
        return
    
    currchar = string[index]
    if(currchar == "x"):
        count += 1 
        duplicate(string, index + 1 ,count,newstring)
    else:
        newstring += currchar
        duplicate(string, index + 1 ,count,newstring)
stri = "axbcxxd"
duplicate(stri,0,0,"")


# Output: abcdxxx

