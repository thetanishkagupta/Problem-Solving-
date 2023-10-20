def subsequence(string, index, newstring):
    if len(string) == index:
        print(newstring)
        return

    currchar = string[index]
    subsequence(string, index + 1, newstring + currchar)
    subsequence(string, index + 1, newstring)
    
stri = "abc"



# Output: abc
          ab
          ac
          a
          bc
          b
          c

