        # (1) calculator :
# def calculator (a,b):
#     print(a+b)
#     print(a-b)

# calculator(12,2)


        # (2)make a function circle  and calculator  its  perimeter  and area
# def circle(radius):
#     area=3.14*radius**2
#     perameter=2*3*radius
#     print("area is :",area)
#     print("perameter is :",perameter)
    
# circle(12)

    #(3) make a functions rectengle  and calculator  its area  and perameter 
# def rectangle(l,b):
#     area=l*b
#     perameter=2*(l+b)
    
#     print("area is :",area)
#     print("\n perameter :",perameter)

# rectangle(10,2)       

    #(4)
    
# def calc_sum(a,b):
#     return a+b

# print(calc_sum(5,10)

# def square(no):
#     return no**2

# def cube(no):
#     return no*square(no)

# print(cube(5))    


    #(5) make a function to calculate  product  of list
    
# def cal_pro_list(list):
#     prod=1
#     for i in list:
#         prod*=i 
#     return prod
# a=cal_pro_list([1,2,3,4,5])
# print(a)       

    #(6) make a function to calculate  sum  of list
 
# def calc_sum_list(list):
     
#      sum=0
#      for i in list:
#           sum+=i
#      return sum

# a=calc_sum_list([1,2,3,4])
# print(a)       


    #(7) print 10-100 in range

# def check_range(no):
#     if no in range(10,100) :
#         print("present in range")
#     else:
#         print("not in range")       
    
# check_range(10)
# check_range(100)
    
    #(8) MAKE A FUNCTION TO print a table
        
# def table(n):
#     for i in range(1,11):    
#         print(n*i)
# table(5)        

    #(9) make a function to reverse a string
# def reverse(str):
#     return str[: :-1]
# print(reverse("royal"))
        
    #(10)make a function to find maximum of two numbers            

# def max_two(a,b):
#      return max(a,b)

# def max_three(a,b,c):
#      return max(max_two(a,b),c)

# def max_four(a,b,c,d):
#      return max(max_three(a,b,c),d)


# print(max_four(10,20,30,40))


    #(11) make a function to print unique elements from list
    
# def elements(list):
#     unique=set(list)
#     for a in unique:
#         print(a)
    
# list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# elements(list)                  
##______________________________________________________##
                     #practice (functions)
##______________________________________________________##
                     
        # (1)- reverse a string with functions
        
# def reverse(str):
#     return str[: :-1]
# print(reverse("yash"))
# ##______________________________________________________##
  
            #(2)-in string  replace e with $

# def replace(string):
#      return string.replace("e","$")
# print(replace("hello"))
##______________________________________________________##

        #(3)- check string is in uppercase or lowercase
        
# def check_str(str):
#     if str.isupper()==True:
#         print("upper case")
#     elif str.islower()==True:
#         print("LOWER CASE")
#     else:
#         print("mixed")    
        
# check_str("mini")    
# check_str("MINI")    
# check_str("MiNi")                
##______________________________________________________##
       
        #(4)- check that string ends with "tion" or not
        
# def case(str):
       
#          if str.endswith("tion"):
#             print("yes")
#          else:
#             print("no")
# case("notion")
##______________________________________________________##
        
        #(5)- make a function which give output by removing whitespace of string
        
# def str_1(str):
#     print(str.strip(" "))
# str_1("    yash")        
##______________________________________________________##

        #(6)- Count vowel in the string
# def count_vowel(str):
#     count=0
#     vowel="aeiouAEIOU"
#     for i in str:
#         if i in vowel:
#             count+=1
#     print(count)
    
# a="miniarbcenu"
# count_vowel(a)
##______________________________________________________##
                 #(7)- find sum of all elements
# def sum_tuple(tuple):
#     sum=0
#     for i in tuple:
#         sum+=i
        
#     return sum

# tup1=(1,3,7,8,5)
# tup2=(4,3,4,7,8,)
# print(sum_tuple(tup1))
# print(sum_tuple(tup2))
        
##______________________________________________________##

        #(8)- write  a function  to find  largest element in list
# def large(list):
#     return max(list)
       
# li=[1,2,45,48,56,78]        
# print(large(li))  
##______________________________________________________##
        
        #(9)- write a python function that takes two list and return true if they have at least one common element
# def list_true(list1,list2):
#     redult=False
#     for i in list1:
#         for j in list2:
#             if i==j:
#                result=True
#             return result     
# list1=[1,2,3,4]
# list2=[5,6,1]
# print(list_true(list1,list2))                    
##______________________________________________________##
        
        #(10)- write a python function to remove even numbers from list

# def remove_even(list):
#     for i in list:
#         if i%2!=0:
#             print(i)
# remove_even([1,2,3,4,5])                    
##______________________________________________________##

        #(11)- make a function that takes 2 list and returns difference of two list
        
        
##______________________________________________________##
        
            #make a function to find square of any number and using this function make another
# def square(num):
#     return num**2
# print(square(4))

# def cube(num):
#     return num*square(num)
# print(cube(5))   

##______________________________________________________##

        #
# def triangle_angle(ang1,ang2):
#     ang3=180-(ang1+ang2)
#     return ang3                         
   
# print(triangle_angle(60,70))       
##______________________________________________________##

            #make a function which predict the nature of triangle ie- equilateral,isoscales or scalen
# def triangle_type(a, b, c):
#     if a == b and a==c:
#         print("Equilateral traingle")
#     elif a == b or b == c or c == a:
#         print("Isosceles")
#     else:
#        print("Scalene")
       
# triangle_type(10,10,10)
# triangle_type(10,20,10)
# triangle_type(10,20,30)            
##______________________________________________________##
            #maximum functions
# def maximum(*nummbers):  #unlimited perameters (*)
#     print(max(nummbers))
    
# maximum(12,34,56)             
   
##______________________________________________________##
            #make a function to find sum of numbers using keyword argument
# def sum_num(*a):
#     print(sum(a))

# sum_num(14,22,33)          
##______________________________________________________##
      
            #make a function to find product of numbers using keyword argument
# def prod_num(*num):
     
#     prod=1
#     for i in num:
#         prod*=i
#     return prod

# a=prod_num(3,5,6,4)
# print(a)            
##______________________________________________________##

        #make a function to return largest number from four numbers using function of largest in three numbers
        
# def max_two(a,b):
#      return max(a,b)

# def max_three(a,b,c):
#      return max(max_two(a,b),c)

# def max_four(a,b,c,d):
#      return max(max_three(a,b,c),d)


# print(max_four(10,20,30,40))        

##______________________________________________________##

        #make a function that explain that string is palindrome or not
        
# def palindrom(s):
#     return s == s[: :-1] 

# s="madam"
# ans=palindrom(s)

# if ans:
#     print("yes") 
# else:
#     print("no")
              
              
##______________________________________________________##
              #Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# def sort_words(words):
#     return '-'.join(sorted(words.split('-')))

# words = input("Enter words:- ")

# print(sort_words(words))

##______________________________________________________##

        #Generate and print a list where the values are square of numbers between two numbers from 1-20

# def value():
    
#     li=list()
    
#     for i in range(1,21):
#         li.append(i**2)
#     print(li)
    
# value()        





##______________________________________________________##
        #(1) make a function to find factorial of a number using recursion
        
# def fact(no):
#     if no==1:
#         return 1
#     else:
#         return no*fact(no-1)       
# print(fact(5))            
##______________________________________________________##
             #(2) make a two function even and odd and call the function even when user input even and call odd function when user
# def odd(no):
        
        
##______________________________________________________##
        #(4)make a function to calculate area and perimeter of two circles
# def circle(r):
#      area = 3.14*r**2
#      p = 2*3.14*r
#      print("Area = ",area)
#      print("Perameter = ",p)
# circle(6)        
##______________________________________________________##
        #(4)
        
        
        
        
        
        #(5) make a function to reverse a string
# def rev_str(string):
#     return string[: :-1]
# print(rev_str("yash"))        
##______________________________________________________##

        #(7) make a function which convert hour and min into mins
# def  convert(hr,min):
#     m=hr*60
#     totalmin=m+min
    
#     return totalmin
# print(convert(2,20))     
##______________________________________________________##
        #(8)#make a function to calculate sum of list using recursion
# li=[1,2,5,4,7]
# li1=[1]
# def list_sum(list):
#     if len(list)==1:
#         return  list[0]
#     else:
#         return list[0] + list_sum(list[1:])

# print(list_sum(li))
# print(list_sum(li1))        
##______________________________________________________##
   
   
  #write a python function that takes a sequence of numbers and determine whether all numbers are 
  #different from each other

# def different(list):
        
#         if len(list)==len(set(list)):
#                 print("all elements are different")
#         else:
#                 print("all elements are same")
                
# different([1,2,4,4,5])
# different([1,2,3,4,5])                
##______________________________________________________#
        #write a python program to print today's date

# def today_date():
#     import datetime
    
#     # today==datetime.datetime.now()
#     today=datetime.datetime.today()
    
#     print(today.strftime("%d--%m--%y @ %H--%M--%S"))
# today_date()
##______________________________________________________#
        #write a function that accepts file name and returns extension of file name
# def filext():
#     filename = input("Enter file name: ")
#     ext = filename.split('.')[-1]
#     print("The file ext:",ext)

# filext()
##______________________________________________________#


#write a function that create a list with values ranging from 0 to n.

# def list(n):
#     return [i for i in range(n + 1)]

# n = 20
# print(list(n))
##______________________________________________________#

        #write a function that return elements of list multiplied by 2
# def mul(lst):
#     return [x * 2 for x in lst]

# mylist = [1, 2, 3, 4, 5]
# out = mul(mylist)
# print(out)        
##______________________________________________________#
        #wap to make a class Bestfriends by defining bff names , make a child class which inherit bff names
        # to display ;by using super function
# class bff:
#       def __init__(self,bff1,bff2):
#               self.bff1=bff1
#               self.bff2=bff2
# class name(bff):
#         def __init__(self, bff1, bff2):
#                super().__init__(bff1, bff2)              
        
# obj1=name('yash','vrutik')
# print(obj1.bff1,obj1.bff2)               
##______________________________________________________#
                #wap to make a class Triangle with method area ,
                # make a child class righttriangle to inherit area method
# class triangle:
#         def __init__(self,base,hight):
#                 self.base=base
#                 self.hight=hight
        
# class tri(triangle):
#         def __init__(self, base, hight):
#                 super().__init__(base, hight)   
                
#         def cal(self):
#                 return (self.base*self.hight)/2    
                                 
# obj1=tri(12,20)
# print("base : ",obj1.base)                
# print("height : ",obj1.hight)                
# print("triangle formula : ",obj1.cal())
##______________________________________________________#

#wap to make a class Shape , add method area in such a way that on passing one value calculate area 
#of square , on 2 values calculate area of rectangle , om passing 3 values calculate volume of cuboid
# and on no values gives perimeter of square and rectangle

# class rec:

#     def no(self,x=None,y=None,z=None):

#         if x==None and y==None and z==None:
#             print("rectangle formula= l*b")
#             print("squre formula= num**2")

#         elif x!=None and y==None and z==None:
#             print("squre  is : ",x**2)

#         elif x!=None and y!=None and z==None:
#             print("rectangle is : ",x*y)

#         else:
#             print("volume is : ",x*y*z) 

# n1=rec()
# n1.no()
# n1.no(10)
# n1.no(10,20)
# n1.no(5,3,2)

        #SECOND STYLE

# from multipledispatch import dispatch
# class Shape:
#     @dispatch(int,int,int)
#     def num(a,b,c):
#         print("rectangle formula=l*b")
#         print("square formula is=num**2")
#     @dispatch(int)
#     def num(a):
#         print("square is",a**2)

#         @dispatch(int,int)
#         def num(a,b):
#             print("rectangle is",a*b)
             
# n1=Shape()
# n1.num(10,20,30)
# n1.num(5)
# n1.num(2,8)
##______________________________________________________#
