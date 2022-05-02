class Solution:
    def armstrongNumber (no_of_digit, num):
        no_of_digit = len(str(num))  # count no of digits in a number eg. 1634 haas 4 digit
        sums = 0
        
        original_num = num
        while num > 0:
           last_digit = num % 10
           sums += last_digit ** no_of_digit # '**' - used to find the power (pow() function)
           num = num // 10
           
        if sums == original_num:
            return("Yes")
        else:
            return("No")
          
          
# Another Method
class Solution:
    def armstrongNumber (no_of_digit, num):
        sums = 0
        original_num = num
        
        while num > 0:
           sums = sums + (num%10)*(num%10)*(num%10)
           num = num // 10
           
        if sums == original_num:
            return("Yes")
        else:
            return("No")
        
