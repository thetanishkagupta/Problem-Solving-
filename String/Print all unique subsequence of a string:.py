def subsequence(string, index, newstring,unique):
    if len(string) == index:
        if newstring in unique:
            return
        else:
            print(newstring)
            unique.add(newstring)
            return
    
    currchar = string[index]
    subsequence(string, index + 1, newstring + currchar,unique)
    subsequence(string, index + 1, newstring,unique)
stri = "aaa"
unique = set()
subsequence(stri, 0, "", unique)


# Output: aaa
          aa
          a

