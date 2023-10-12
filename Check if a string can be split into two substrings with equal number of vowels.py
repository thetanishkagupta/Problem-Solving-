def check_alike(string):
    if len(string)%2 != 0:
        return False
    
    middle = len(string) // 2
    first_half = string[:middle]
    second_half = string[middle:]
    
    def count_vowels(string):
        vowels = "AEIOUaeiou"
        count = 0
        for char in string:
            if char in vowels:
                count += 1 
        return count
    return count_vowels(first_half) == count_vowels(second_half)        

stri = "book"
print(check_alike(stri))


