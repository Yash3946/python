#filter() => it filters or selected required connditions

# adults=[12,34,5,43,32,12,18]
# def age18(n):
    
#     if n>=18:
#         return n

# a = filter(age18,adults)
# print(list(a))

##__________________________________________________________________________________##    

    #in a list of integers, find even and odd integers using filter()

# integer=[1,2,3,4,12,23,34,11,21,31,56,78,90,88,9]
# def even(n):
    
#     if n % 2 ==0:
#         return True

# def odd(n):
    
#     if n % 2 !=0:
#         return True
  
# a=filter(even,integer)
# print(list(a))
# a=filter(odd,integer)
# print(list(a))

##__________________________________________________________________________________##    

      #in a list of integers, find even and odd integers using filter() using lambda function
# integer=[1,2,3,4,12,23,34,11,21,31,56,78,90,88,9]

# even = list(filter(lambda x: x % 2 == 0, integer))

# odd = list(filter(lambda x: x % 2 != 0, integer))

# print("Even Numbers:", even)
# print("Odd Numbers:", odd)

##__________________________________________________________________________________##    

    #in list of string filter non empty string


# li = ["","jalu","tithi","yash",""]

# string = list(filter(lambda x: x != "", li))

# print("Non-Empty Strings:", string)

##__________________________________________________________________________________##    

    #in a list of string, filter those words in which characters are more than 5

# name = ["yash", "vrutik", "tithi", "jalp", "mili", "jalpudi"]

# filter = list(filter(lambda x: len(x) > 5, name))

# print("Words with more than 5 characters:",filter)

##__________________________________________________________________________________##    

    #WAP to find whether a string endswith "a" or not using lambda()

# x = lambda str:True if str.endswith("i") else False

# print(x("mini"))
# print(x("mno"))

##__________________________________________________________________________________##    

#WAP to find whether a string endswith "i" in a list

# name = ["yash", "vrutik", "tithi", "jalp", "jalpudi","ishika"]

# string = [x for x in name if x.endswith('i')]

# print("Strings ending with I:", string)

##__________________________________________________________________________________##    

# Write a  Python program to find the intersection of two given 
# arrays using Lambda

# array1=[1,2,3,4,45,12,23,69,50]
# array2=[2,1,3,4,250,60,78,23]
# a=list(filter(lambda x: x in array1,array2))
# print(a)

##__________________________________________________________________________________##    

# Write a  Python program to count the even and odd numbers in a 
# given array of integers using Lambda

# num=[1,2,3,4,45,12,23,69,50]

# even= len(list(filter(lambda x: x % 2 == 0, num)))
# odd= len(list(filter(lambda x: x % 2 != 0, num)))

# print("Even Count:", even)
# print("Odd Count:", odd)

##__________________________________________________________________________________##    

# import datetime

# now=datetime.datetime.now()

# print(now)

# year=lambda x: x.year
# time=lambda x: x.time()
# day=lambda x: x.day
# month=lambda x: x.month


# print(year(now))
# print(time(now))
# print(day(now))
# print(month(now))

##__________________________________________________________________________________##    

# import re
# password=input()


##__________________________________________________________________________________##    


# Write a Python program to check the validity of passwords input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

##__________________________________________________________________________________##    

# import re
# password=input("enter a string ")

# if not re.search("[a-z]",password):
#     print("invalid pass")
# elif not re.search("[A-Z]",password):
#     print("invalid pass")
# elif not re.search("[0-9]",password):
#     print("invalid pass")
# elif not re.search("[$#@]",password):
#     print("invalid pass")
# elif len(password)<6 or len(password)>16:
#     print("inavalid pass")
# else:
#     print("valid pass")
##__________________________________________________________________________________##    
    
# import re

# # str="I am indonasia in "

# # x=re.search("in",str)
# # print(x.start())

# str1="We are on the earth"
# a=re.split("\s",str1)


# print(a)

##__________________________________________________________________________________##    

# import re

# str="I am indonasia in "
# x=re.sub("\s","@",str)
# print(x)

##__________________________________________________________________________________##    
