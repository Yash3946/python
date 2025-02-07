#OOPS concept- object oriented programming
#class ->it is a blueprint of instance
#class is a collection of attribute/features and methods
#object-> it is inside class and real instance

##_____________________________________________________________________________##

# class Bike:
#     model=2024
#     engine="100cc"
#     average="10km/li"
#     def brand(self):
#         print("class Bike has good brand")
# b1=Bike()
# b2=Bike()
# print(b1.average)
# print(b2.model)
# print(b1.brand())
##_____________________________________________________________________________##

# class Thar:
#     model=2024
#     engine="2200cc"
#     average="10km/li"
#     transmition="auto"
    
#     def brand(self):
#         print("class Thar has good jeep")
# b1=Thar()
# b2=Thar()
# print(b1.average)
# print(b2.model)
# print(b1.engine)
# print(b1.brand())
##_____________________________________________________________________________##

# class car:
#     name="xuv900"
#     enging="3000cc"
    
#     #constructor -> _init() ->it is automatically called when any object is called
    
#     def _init_(self,color,airbags):
#         self.col=color
#         self.airbags=airbags
        
# c1=car("red","yes")
# c2=car("black","no")

# print(c1.col,c1.airbags)
# print(c2.col)
##__________________________________________________________________##

# class student:
#     eligibility="60+"
#     fees=1000
    
#     def __init__(self,name):
#         self.name=name

# s1=student("vrutik")
# s2=student("jallu")

# print(s1.name , s2.name)
##__________________________________________________________________##
                #make a class  square  with attributes side and calcaulate its area  and perimeter 
# class square:
    
#     def __init__(self,side):
#         self.side=side
        
#     def area(self):
#         return self.side**2

#     def perimeter(self):
#         return 4*self.side

# s1=square(10)

# print("area is",s1.area())
# print("perimeter is:-",s1.perimeter())                
##__________________________________________________________________##

                #make a class Rectangle with attributes length and breadth then calculate area and perimeter
                
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
         
#     def area(self):
#         return self.length*self.breadth   
    
#     def peri(self):
#         return 2*(self.length+self.breadth)
    
# r1=Rectangle(2,4) 
# r2=Rectangle(3,2)
        
# print("area of rec = ",r1.area())
# print("peri = ",r2.peri())
##__________________________________________________________________##
               # make a class Person , add attributes like name,country and Dob ,then add functions such that to calculate 
# class person_age:
#         def __init__(self,name,country,dob):
#              self.name=name
#              self.country=country
#              self.dob=dob
             
#         def calculate_age(self):
#             current_year=2024
#             age=current_year-self.dob
#             print("age is : ",age)
           
# p1=person_age("yash","india",2002) 
# p2=person_age("vrutik","india",2002) 
# p3=person_age("jallu","india",2007) 


# print(p1.name)       
# print(p1.calculate_age())
# print(p2.name)           
# print(p2.calculate_age())
# print(p3.name)                  
# print(p3.calculate_age())
##__________________________________________________________________##
           #wap to make a class calculator, add basic methods to calculate addition,substraction,multiplication,division
# class Calculator:
#     def add(self, num1, num2):
#         return num1 + num2

#     def subtract(self, num1, num2):
#         return num1 - num2

#     def multiply(self, num1, num2):
#         return num1 * num2

#     def divide(self, num1, num2):
#         return num1 / num2
    
        
# calc = Calculator()
# print("add is : ",calc.add(2, 3))
# print("subtract is :",calc.subtract(20, 5)) 
# print("multiplt is : ",calc.multiply(4, 5)) 
# print("divide is :",calc.divide(10, 2))
##__________________________________________________________________##
        #make a class Account with attributes accno and balance ,then make credit and debit system

# class Account

#     def __init__(self,accno,balance):
#        self.accno=accno 
#        self.balance=balance
       

#     def credit(self,amount):
#         self.balance+=amount
#         print("credited amount is:-",amount)
        
#     def debit(self,amount):
#         self.balance-=amount
#         print("amount debited:-",amount)
#         print("total balance is",self.totalbal())
        
#     def totalbal(self):
#         return self.balance
    
# obj1=Account("acc12",5000)
# obj1.credit(2000)
# obj1.debit(1000)
##__________________________________________________________________##
                #write a program to make a class rectangle and calculate its area and perimeter
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
         
#     def area(self):
#         return self.length*self.breadth
    
#     def peri(self):
#         return 2*(self.length+self.breadth)
    
# r1=Rectangle(3,5) 
# r2=Rectangle(2,4)
        
# print("area of rec = ",r1.area())
# print("peri = ",r2.peri())
##__________________________________________________________________##
                
# class Animal:
#     animalname="horse"
#     name="jallu"
#     age="three months"
    
#     def dog(self):
#         print("My favourite animal")

# d1=Animal()     
# d2=Animal() 
   
# print(d1.animalname)
# print(d1.name)
# print(d2.age)
##_____________________________________________________________________________##

# class Student:
#     eligibility="80+"
#     grade="A or B"
    
#     @staticmethod
#     def hi():
#         print("welcome all students in class")
# s1=Student()
# s2=Student()
  
# print(s1.hi())        
##_____________________________________________________________________________##

# class Employee:
#     __designation="sales"             # __(double __) means private  attribute
#     uniform="formal"
       
#     def __init__(self,salary):
#         self.__salary=salary
        
#     def sal(self):
#         return self.__salary
    
           
#     def profile(self):
   
#         return self.__designation

#                                        #to access private attribute we can use setter mothod
# obj1=Employee(400000)
# obj2=Employee(500000)
  
# print(obj1.profile())
# print(obj2.sal())  
##_____________________________________________________________________________##

        #wap  to help a thief to hide  his identification by making class people

# class People:
    
#     __identification="thief"
    
#     def men(self):
#         return self.__identification
    
# obj1=People()

# print(obj1.men())
##_____________________________________________________________________________##

                #wap to make a python class Number and calculate difference between two number

# class Number:
#         def __init__(self,a,b):
#                 self.num1=a
#                 self.num2=b

#         def calc_diff(self):
#                 return self.num1-self.num2 
        
#         @staticmethod
#         def msg():
#                 print("welcome to the class") 
                
# obj1=Number(20,8)                      
# obj2=Number(100,50)
# obj2.msg()                      
# print("difference is", obj1.calc_diff())
##_____________________________________________________________________________##
              
                # write a  Python program to create two empty classes, Student and Marks.
                # Now create some instances and check whether they are instances of the said classes or not.  
                
                
# class Student:          #only classs  without attribute
#         pass
# class Marks:
#         pass

# s1=Student()
# M1=Marks()

# print(isinstance(s1,Student))
# print(isinstance(M1,Student))
# print(isinstance(s1,Marks))
# print(isinstance(M1,Marks))

##_____________________________________________________________________________##

                #Write a Python class named Student with two attributes: student_id, student_name. 
                # Create a function to display all attributes and their values in the Student class.

# class Student:
#         student_id=121
#         student_name="jallu"
        
#         def display(self):
#                 print("id is = ",self.student_id)
#                 print("name is = ",self.student_name)
# s1=Student()
# s1.display()                
##________________________________________ _____________________________________##
        
           #write a python program to make class Circle , make method c1 and c2 with their area, then calculate their difference  of area

# class Circle:
#     def __init__(self,c1,c2):
#         self.c1=c1
#         self.c2=c2
#     def areac1(self):
#         return  3.14*(self.c1*self.c1)
    
#     def areac2(self):
#         return  3.14*(self.c2*self.c2)
    
#     def diff(self):
#         return (3.14*(self.c1*self.c1) - 3.14*(self.c2*self.c2))
    
# obj1=Circle(10,5)
# print(obj1.areac1())
# print(obj1.areac2())
# print(obj1.diff())
#_____________________________________________________________________________##
                #write a python program to make a class Time which convert hrs and mins into total mins

# class time:
#         def __init__(self,hour,min):
#                 self.hour=hour
#                 self.min=min
                
#         def total_min(self):
#                 print("total minutes are : ",self.hour*60+self.min)
               
# t1=time(2,18) 
# t1.total_min()                       
##_____________________________________________________________________________##
                # Write a Python program to create a class representing a stack data structure. 
                # Include methods for pushing and popping elements.
# class Stack:
    
#     def __init__(self):
#         self.items=[]
    
#     def push(self,el):
#         self.items.append(el) 
    
#     def pop(self,el):
#         self.items.remove(el)

# s1=Stack()
# s1.push(4)
# s1.push(10)
# s1.push(4)
# print(s1.items)
##_____________________________________________________________________________##
    
# class Car:
#         def __init__(self,color,name):
#                 self.color=color
#                 self.name=name
                

#         @staticmethod
#         def yash():
#                 print("i have all cars")        
                                
# car1=Car("black","thar")
# print(car1.color,car1.name)             
# car2=Car("white","thar") 
# print(car2.color,car2.name)    
# print(car1.yash())
##_____________________________________________________________________________##

                #wap to make a class Student then find percentage of each student of three subjects

# class Student:
#     def __init__(self,math,bio,che):
#         self.math=math
#         self.che=che
#         self.bio=bio
        
#     def percentage(self):
#         return (self.math + self.che + self.bio)/3
    
# obj1=Student(90,95,97)
# print("math : ",obj1.math)
# print("che : ",obj1.che)
# print("bio : ",obj1.bio)
# print("per is = ",obj1.percentage())

##_____________________________________________________________________________##
                #wap to make a class number and calculate average of number and their square
# class Number:
#     def __init__(self,number):
#         self.number=number
        
#     def avg(self):
#         return(self.number**2 + self.number) /2  
    
# obj1=Number(2)
# print("avg is = ",obj1.avg())      
##_____________________________________________________________________________##
                #delete attribute or any object 
                
# class Student:
#         def __init__(self,name,rno):
#                 self.rno=rno
#                 self.name=name
        
# s1=Student("jalp",2)
# print(s1.name)     
#               #when we have to delete any attribute or any object 
#               #delete key word
# print(s1)
# del s1
# print(s1)      
##_____________________________________________________________________________##
        #wap to make class Account with att acc number and acc pass but
        #program in such a way that no one can access acc pass outside the class

# class Bank:
#         def __init__(self,acc_nub,acc_pass):
#                 self.acc_nub=acc_nub
#                 self.__acc_pass=acc_pass
        
#         def password(self):
#                 return self.__acc_pass        
 
# num1=Bank(132143,82622015) 
# print("acc_nub : ",num1.acc_nub)
# # print("acc_pass : ",num1.__acc_pass)                  #not give password 
# print("acc_pass : ",num1.password())                     #give password
##_____________________________________________________________________________##
        #wap to make a class Library , add methods to add books , remove books , and check
        #available books
# class Library:
#         def __init__(self):
#                 self.noofbooks=[]
                
#         def addbook(self, book):
#                 return self.noofbooks.append(book)

#         def removebook(self, book): 
#                 return self.noofbooks.remove(book)
        
#         def bookavail(self):
#                 return self.noofbooks
# b1=Library()
# b1.addbook("october junction")
# b1.addbook("designing destiny")
# b1.addbook("harry potter") 
# print(b1.bookavail())
# b1.removebook("designing destiny")
# print(b1.bookavail())
##_____________________________________________________________________________##

          #wap to make a class Basket with methods additems , del items and show items

# class Basket:
#         def __init__(self):       
#                 self.noofitems=[]
                
#         def additems(self, item):
#                 return self.noofitems.append(item)

#         def removeitems(self, item): 
#                 return self.noofitems.remove(item)
        
#         def itemavail(self):
#                 return self.noofitems

# b1=Basket()
# b1.additems("pen")
# b1.additems("pencil")
# b1.additems("toys")
# print(b1.itemavail())
# b1.removeitems("pencil")
# print(b1.itemavail())

##_____________________________________________________________________________##

   