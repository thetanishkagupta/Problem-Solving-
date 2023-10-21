def check_alike(string):
    if len(string)%2 != 0:           # checks if the length of the input string is odd
        return False
    
    middle = len(string) // 2        # calculate the middle point of the string
    first_half = string[:middle]     # splits the string into two halves
    second_half = string[middle:]
    
    def count_vowels(string):        # counts the number of vowels in a given string
        vowels = "AEIOUaeiou"
        count = 0
        for char in string:
            if char in vowels:
                count += 1 
        return count
    return count_vowels(first_half) == count_vowels(second_half)   # returns True if number of vowels in the first_half is equal to the number of vowels in the second_half  

stri = "book"
print(check_alike(stri))

# Output: True

