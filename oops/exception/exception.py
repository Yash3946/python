## Exception handling
## ==> to handle the unwanted situation or errors is exception handling


#try: it catches the error
#except: it handles the code with error
#else-> it is optional and to execute when no error is occured
#finally-> it is also optional and it is always executed


# a=int(input("enter a number : "))
# b=int(input("enter b number : "))
# try:
#     div=a/b
#     print(div)
# except:
#     print("something is wrong")
    
# print("all rest of the code ")
##______________________________________________________________________##

# a=int(input("enter a number : "))
# b=int(input("enter a number : "))
# try:
#     div=a/b
#     print(iv)
    
# except NameError:
#     print("something typed wrong")
# except ZeroDivisionError:
#     print("division by 0 is not possible")

# print("rest code")
##______________________________________________________________________##
    
# a=10
# try:
#  b=12
# except IndentationError:
#     print("not possible")
# try:
#     print(a+c)
# except NameError:
#     print("name error")

##______________________________________________________________________##

# a=int(input("enter a number : "))
# b=int(input("enter a number : "))
# try:
#     div=a/b
#     print(di)
# except (ZeroDivisionError,NameError) as obj:
#     print(obj)
# print('rest code')

##______________________________________________________________________##

# Write a Python program that prompts the user to input an integer and 
# raises a ValueError exception 
# if the input is not a valid integer.

# def integer():
#     try:
#         num = int(input("enter integer:-"))
#         return (num)
#     except ValueError:
        
#         print("enter the only integer")
# integer()
##______________________________________________________________________##

# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero

# def inte():
    
#     a=int(input("enter a number : "))
#     b=int(input("enter a number : "))    
#     try:
        
#         div=a/b
#         print(div)
    
#     except ZeroDivisionError:
#         print("division by 0 is not possible")

# inte()

##______________________________________________________________________##

# Write a  Python program that opens a file and handles a FileNotFoundError
# exception if the file does not exist.
# exception FileNotFoundError:
# Raised when a file or directory is requested but doesn’t exist. 
# Corresponds to errno ENOENT.

# def filenotfound(filename):
#     try:
#         f=open(filename,"r")
#         file = f.read()
#         print(file)
#         f.close()
#     except FileNotFoundError:
#         print("file not exist!!")
# filenotfound("abc.txt")
# filenotfound("data.txt")

##______________________________________________________________________##

# Write a Python program that executes an operation on a list and handles an 
# IndexError exception if the index is out of range.
# exception IndexError:
# Raised when a sequence subscript is out of range.
# (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, 
#  TypeError is raised.)

# def get_element_from_list(list, index):
#     try:
#         element = list[index]
#         print(element)
#     except IndexError:
#         print("index is out of range :-")

# print(get_element_from_list([10,20,30,40,50], 2))

##______________________________________________________________________##

# In an online shopping checkout system, calculate the total price of items in the cart.
# The system should:
# Handle cases where item prices are invalid (non-numeric).
# Handle cases where the cart is empty.
# Ensure the total price is a positive value
# Messages addressed to "Meeting Group Chat" will also appear in the meeting group chat in Team Chat

# cart = input("ente item prices seperated by space").split()

# def checkout(cart):
#     try:
#             if not cart:
#                 raise ValueError("cart is empty")
            
#             total_price=0
#             for item in cart:
#                 Price=float(item)
                
#                 if Price < 0:
#                     raise ValueError("price in negative is not possible")
#                 total_price += Price
#                 print("total price is : ",total_price)
                
#     except ValueError as var:
#         print(var)
# checkout(cart)

##______________________________________________________________________##

# class AttemptExceptionError(Exception):
#     pass
#     attempt=0

# def withdraw():
#     global attempt
#     saved_pin = 1234 #hard code
#     balance = 10000 #fixed 10000 should be in balance
    
#     pin = int(input("enter your pin:-"))
#     if pin==saved_pin:
#         try:
#             amt=int(input("enter amount to withdraw"))
#             final_balance=balance-amt
            
#             if final_balance<1000:
#                 raise BalanceExceptionError("insufficient balance")
#             print("final balance is:-",final_balance)
            
#         except BalanceExceptionError as var:
#             print(var)
        
#     else:
#         ans=input("do u want to continue say y/n").lower()
        
#         if ans == 'y':
#             attempt+=1
            
#             try:
#                 if attempt==4:
#                     raise AttemptExceptionError("to many attempts!!,your account is blocked now..")
#             except AttemptExceptionError as var:
#                 print(var)  
#             else:
#                 withdraw()  
            
#         else:
#             print("happy transaction")    
   
# withdraw()




class Tendivionerror(Exception):
    pass

try:
    
    a =int(input("enter a number:"))
    b = int(input("enter a number:"))
    if b==10:
        raise Tendivionerror("division by 10 is not possible")
    print(a/b)
    
except Tendivionerror as var:
    print(var)


print("code end")
print("code finish")