#polymorphism-> poly- many , morphism -forms
# print(10+20)   #sum
# print("shraddha " + "pachauri")  #joint
# print([1,2,3] + [2,3,4])  #merge
#polymorphism -> by three types
#1-method overloading -> this helps us to use function with diff forms
#2-method overriding
#3-operator overloading (dunder functions)
##_________________________________________________________________##

               #1-method overloading -> 
##_________________________________________________________________##

# class Number:    # method overloding

#     def num(self,x=None,y=None,z=None):
#         if x==None and y==None and z==None:
#             print("this everybody")
            
#         elif x!=None and y==None and z==None:
#             print("sum is:-",x**2)
            
#         elif x!=None and y!=None and z==None:
#             print("product is",x+y)
#         else:
#             print("product is",x*y*z)
            
# obj=Number()
# obj.num()
# obj.num(10)
# obj.num(10,20)
# obj.num(10,2,3)
##_________________________________________________________________##

#wap to make python class Digit in such a way that using method overloading same function is used 
#like without parameter it welcomes user, on one parameter it gives factorial , on two parameter give sum of squares 
#of both parameter

# class Digit:

#     def number(self,a=None,b=None):      #least efective method
#         if a==None and b==None:
#             print("welcome user")
          
#         elif a!=None and b==None:
#             f=1
#             for i in range(1,a+1):
#                 f=f*i
#             print("factorial is : ",f)
#         else:
#             print("sum of squares is : ",a**2+b**2)
            
# d1=Digit()
# d1.number()
# d1.number(4)
# d1.number(2,3)
##_________________________________________________________________##

# from multipledispatch import dispatch
# class Prod:

#     @dispatch(int,int,int)
#     def pr(a,b,c):
#         print("prod is : ",a*b*c)
     
#     @dispatch(int,int)
#     def pr(a,b):    
#         print("prod is : ",a*b)
        
#     @dispatch(int)
#     def pr(a):    
#         print("prod is : ",a)    
        
# obj=Prod()
# obj.pr(2)
# obj.pr(2,3)
# obj.pr(2,3,4)
##_________________________________________________________________##


            #2 == > method overriding

##_________________________________________________________________##
       
# class A:
#     def abc(Self):
#         print("hellow")
        
# class B:
#     def abc(self):
#         print("patel")
    
# obj1=B()
# obj1.abc()
# obj2=A()
# obj2.abc()
##_________________________________________________________________##
     #wap to make a class F with child class F1 with same method fun() but show diff behaviour                    
     
# class F:
#     def beh(self):
#         print("hiii")
# class F1:
#     def beh(self):
#         print("yash")
# obj1=F1()
# obj1.beh()
# obj2=F()
# obj2.beh()          
##_________________________________________________________________##

# wap to make a class Rectangle with child class Rectangle1 , add method shape() but in class 
#Rectangle it calculate area but in class Rectangle1 it calculate perimeter
#area= l*b
#peri= 2(l+b)

# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
        
#     def shape(self):
#         print("area is : ",self.l*self.b)
        
# class Rectangle1(Rectangle):
#     def __init__(self, l, b):
#         super().__init__(l, b)
        
#     def shape(self):      
#         print("perameter is : ",2*(self.l+self.b))

# obj1=Rectangle(2,3)
# obj1.shape()

# obj2=Rectangle1(4,5)
# obj2.shape()

##_________________________________________________________________##

          # 3.DUNDER function
##_________________________________________________________________##

# class A:
#     def abc(self,x):
#         self.x=x

#     def __add__(self,o):         #__add__  ==> dunder functions
#         return self.x+o.x

# ob1=A()
# ob1.abc(10)

# ob2=A()
# ob2.abc(20)

# print(ob1+ob2) 
##_________________________________________________________________##

#wap to make a class Diff in such a way which allow to substract the value of two objects
# use dunder function __sub__()


# class A:
#     def abc(self,x):
#         self.x=x

#     def __sub__(self,o):        
#         return self.x-o.x
    
# ob1=A()
# ob1.abc(20)

# ob2=A()
# ob2.abc(10)

# print(ob1-ob2)
##_________________________________________________________________##

     #wap to make a class Complex and add method to add complex numbers
     
# class Complex:
#      def _init_(self, real, img): 
#           self.real=real 
#           self.img=img

#      def show(self): 
#           print(self.real, "i +", self.img,"j")

#      def __add__(self, other):
#           newreal=self.real + other.real 
#           newimg=self.img + other.img 
#           return Complex(newreal, newimg)

#      #def add (self,other):
#      #return self.real + other.real, self.img + other.img

# obj1=Complex(2,6) #4i +5j
# obj1.show()
# obj2=Complex(5,6)  
# obj2.show()

# # n=obj1+obj2
# # n.show()

# n=obj1+obj2
# print(n)               
##_________________________________________________________________##

     #wap to make a class Complex and add method to substract complex numbers
# class Object:
    
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def show(self):
#         print(self.real,"-" , self.img,"j")
        
#     def __sub__(self,other):
#         newreal=self.real - other.real
#         newimg=self.img - other.img
#         return Object(newreal,newimg)
    
# obj1=Object(20,10)
# obj1.show()

# obj2=Object(10,2)
# obj2.show()

# v=obj1 - obj2
# v.show()

##_________________________________________________________________##

   #wap to make a class Complex and add method to mulyiply complex numbers
# class Object:
    
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def show(self):
#         print(self.real,"*" , self.img,"j")
        
#     def __mul__(self,other):
#         newreal=self.real * other.real
#         newimg=self.img * other.img
#         return Object(newreal,newimg)
    
# obj1=Object(20,10)
# obj1.show()

# obj2=Object(10,2)
# obj2.show()

# v=obj1 * obj2
# v.show()
##_________________________________________________________________##

   #wap to make a class Complex and add method to division complex numbers
# class Object:
    
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def show(self):
#         print(self.real,"/" , self.img,"j")
        
#     def __div__(self,other):
#         newreal=self.real / other.real
#         newimg=self.img / other.img
#         return Object(newreal,newimg)
    
# obj1=Object(20,10)
# obj1.show()

# obj2=Object(10,2)
# obj2.show()

# v = obj1 / obj2
# v.show()
##_________________________________________________________________##

    #wap to make a class Order which takes itemname and price in constructor
    #use dunder functions __gt__ to compare that price of which order is greator
  
# class Order :
    
#     def __init__(self,itemname,price):
#         self.itemname=itemname
#         self.price=price   
        
#     def __gt__(self,other):
#         return self.price > other.price
    
# order1=Order("pen",20)
# order2=Order("pencil",10)

# if order1 > order2:
#     print("order1 is of highest price")
# else:
#     print("order2 is of highest price")
##_________________________________________________________________##
               
# class Account:
    
#         def __init__(self,accname,accno,balance):
#             self.accname=accname
#             self.accno=accno
#             self.balance=balance
            
#         def __gt__(self,other):         
#             return self.balance > other.balance          
        
# accno1=Account("jalay",121,10000)
# accno2=Account("jalp",122,1000)

# if accno1 > accno2:
#     print("account balance of + " self.accname1,"more than + "self.accname2 )        
##_________________________________________________________________##

# class Grade:
#      def __init__(self,studentname,marks):
#           self.studentname=studentname
#           self.marks=marks
     
#      def __It__(self,other):
#           return self.marks > other.marks
          
# s1=Grade("yash",96)     
# s2=Grade("vrutik",94)

# if s1<s2:
#      print("s2 is less")     
# else:
#      print("s1 is less")     
##_________________________________________________________________##
     #wap to make a class Complex , which add,substract, multiply and divide
     #complex numbers , use __truediv__ for division
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def show(self):
#         print(self.real,"+",self.img ) 
        
#     def __add__(self,other):
#         newreal = self.real + other.real
#         newimg = self.img + other.img
#         return Complex(newreal,newimg)    
    
#     def show(self):
#         print(self.real,"-",self.img )   
    
#     def __sub__(self,other):
#         newreal = self.real - other.real
#         newimg = self.img - other.img
#         return Complex(newreal,newimg)  
    
#     def show(self):
#         print(self.real,"*",self.img ) 
        
#     def __mul__(self,other):
#         newreal = self.real * other.real
#         newimg = self.img * other.img
#         return Complex(newreal,newimg)    
    
#     def show(self):
#         print(self.real,"/",self.img )  
    
#     def __truediv__(self,other):
#         newreal = self.real / other.real
#         newimg = self.img / other.img
#         return Complex(newreal,newimg)
# obj1=Complex(5,9)
# obj1.show()
# obj2=Complex(3,4)
# obj2.show()
# n=obj1+obj2
# print(n.show())     
# n=obj1-obj2
# print(n.show()) 
# n=obj1*obj2
# print(n.show())    
# n=obj1/obj2
# print(n.show())
##_________________________________________________________________##
          
#wap to make a class Employee with attribute role,department,salary
#with method showdetails() also.
#Create an Engineer class which inherit features of Employee and hass additional attribute
#name and age
##_________________________________________________________________##

     #wap to make a class Circle; make a class c1 which inherit features of class Circle
     # add method formula() which calculate area of circle in class Circle and same method
     # calculate perimeter of circle in Class c1

# class Circle:
    
#     def __init__(self, radius):
#         self.radius = radius
#     def formula(self):
#         return 3.14 * (self.radius ** 2)
# class c1(Circle):
    
#     def __init__(self, radius):
#         super().__init__(radius)
        
#     def formula(self):
#         return 2 * 3.14 * self.radius

# circle = Circle(2)
# print("Area of Circle:", circle.formula())
# c1 = c1(4)
# print("Perimeter of Circle:", c1.formula())

##_________________________________________________________________##
    #wap to make a class books; with attributes bookname ,price.
     #add method to add books,delete books , show books.
     #compare the price of 2 books using dunder __gt__
     
# class Books:
    
#     def __init__(self,price):
#         self.items=[]
#         self.price=price
#     def addbook(self,book):
#         self.items.append(book)
        
#     def removebook(self,book):
#         self.items.remove(book)
        
#     def showbook(self):
#         print("available books are :",self.items)
        
#     def __gt__(self,other):
#         return self.price > other.price
    
# b1 = Books(100)
# b2 = Books(200)
# b1.addbook("python")    
# b1.addbook("data science")
# b1.showbook()
# b1.removebook("python")
# b1.showbook()
# if b1 > b2:
#     print("b1 is expencive")
# else:
#     print("b2 is expensive")
    
##_________________________________________________________________##
    
from multipledispatch import dispatch

class Product:
    @dispatch(int)
    def add(a):
        print("product ",a)

    @dispatch(int,int)
    def add(a,b):
        print("product of two num is",a*b)

    @dispatch(int,int,int)    
    def add(a,b,c):
        print("product of three num is",a*b*c)

obj=Product()
obj.add(2,6)
obj.add(5)
obj.add(9,5,3)    





