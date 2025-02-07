    # (1)by using while loop print fibbonacci series from 0 to 50

# n=int(input("enter a number : "))
# a,b=0,1

# i=1
# while i<=n:
#     print(a,end=" ")
#     a,b=b,a+b
    
#     i+=1

##__________________________________________________________________________________##
    # (2)Using for loop count the no of alphabet,digit and special symbol present in string

# input_string = "patelyash@3946"

# alphabets = 0
# digits = 0
# special = 0

# for char in input_string:
#     if char.isalpha():         
#         alphabets += 1
#     elif char.isdigit():       
#         digits += 1
#     elif not char.isspace():   
#         special+= 1

# print("Alphabets:", alphabets)
# print("Digits:", digits)
# print("Special Symbols:",special)
##__________________________________________________________________________________##

    # (3)wap to input a string and print it's reverse if it endswith 'a'

# str = input("Enter a string: ")
# if str.endswith('a'):
#     reverse = str[::-1]
#     print("Reverse of the string:", reverse)
# else:
#     print("does not end with'a'.")
##__________________________________________________________________________________##

    # (4)using for loop print no from n to 1
# n = int(input("Enter a number: "))

# for i in range(n, 0, -1):
#     print(i)

##__________________________________________________________________________________##

    # (5)check no is prime or not
# no = int(input("Enter a number: "))

# if no> 1:
#     for i in range(2,no):
#         if no % i == 0:
#             print( "is not a prime number",no)
#             break
#     else:
#         print ("is a prime number",no)

##__________________________________________________________________________________##

    # (6)print the even integers of list using while loop
# make this pattern
#   *
#   **
#   ***
#   ****
#   ***** 

# for i in range(6):
#     print("*"*i)
##__________________________________________________________________________________##
    
    # (7)make this pattern
#   1
#   22
#   333
#   4444
#   55555

# n = 5
# for i in range(1, n + 1):
#     print(str(i)*i)