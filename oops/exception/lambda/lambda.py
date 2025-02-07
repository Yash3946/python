#LAMBDA FUNCTION
#lambda function is a anonymous function
#it can take as many arguments nut only one expression
#It is used for fast and short calculation
#It is specially used with datetime module and with map(), filter() and reduce()
#It used lambda keyword
#syntax
# lambda arguments : expression

# x=lambda a: a+10
# print(x(50))

# y=lambda a,b : a * b
# print(y(12,13))


#wap to create a lambda function such that one integer calculates with power of second integer

# power = lambda base, num: base ** num
# print("5**2 =",power(5,2))

#WAP to check no is even or odd using lambda func

# x =lambda a: a%2==0

##_____________________________________________________________________##
#By using lambda function calculate length of string

# length= lambda str : len(str)
# print(length("patel yash"))

##_____________________________________________________________________##

#by using lambda function check that string is integer or not

# no= lambda str : str.isdigit()
# print(no("123"))
# print(no("abc"))
##_____________________________________________________________________##

#by using lambda function check that string is either alphabet or numeric
# alphanumeric = lambda s: s.isalpha() or s.isnumeric()

# print(alphanumeric("hello"))  
# print(alphanumeric("123"))    
# print(alphanumeric("hello123"))

##_____________________________________________________________________##

