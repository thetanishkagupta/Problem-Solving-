# You are given a number in the form of string , extract out digits at odd index then square and merge them and discard the even index
# The first 4 digits will be the required OTP which shows as output.
# If 4 digit OTP is not generated then give Output -1.

input_string= input("enter the string: ")
otp= ""
for i in range(len(input_string)) :
    if i%2:
        num_square = int(input_string[i]) **2
        otp += str(num_square)
        if len(otp) >= 4:
           print(otp[ : 4])
           break
else:
    print("-1")
