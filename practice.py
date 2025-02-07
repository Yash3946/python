# str=[1,3,5,7,9,"yash"]
# # print(str[1:6])
# print(len(str))

# a=("Learning is never done without errors and defeat” and replace ")
# print(a.replace("a","@"))
# print(a.replace("e","$"))


# str=["patel"]
# str=["patel"]
# str=["patel"]
# print(str)
##___________________________________________________________________##
    #wap to make a dictionary Student ,with details name, age, hobbies, subjects- scores(key-value)

# student ={                                    
#     "name" : "vrutik patel" , 
#     "age":21,
#     "hobbies":["cricket","football","chess"],
#     "subjects":
#     {
#         "phy":89,
#         "chem":80,
#         "math":92         
#     }
# }    
# print(student["subjects"])
# print(student["subjects"]["phy"])
# print(student["age"])
##___________________________________________________________________##

# d1={
#     "a":1,
#     "b":2
# }
# d2={
#     "c":1.0,
#     "d":2.0
# }
# d3={
#     "e":10,
#     "f":20
# }
# #merge d1 , d2 , d3


# merge = {}
# merge.update(d1)
# merge.update(d2)
# merge.update(d3)

# print(merge)
##___________________________________________________________________##
# employee={
#     "name":"abc",
#     "age":42
# }
#in dict employee add key- surname and change value of age from 42 to 35

# dict={
#     "name":"yash",
#     "age":42
# }
# dict["surname"]="patel",
# dict["age"]=35,
# print(dict)

##___________________________________________________________________##

# employee={
#     "name":"abc",
#     "age":42
# }

# def keys(key,dict):
#     if key in dict:
#         print("present")
#     else:
#         print("not present")
    
# keys("name",employee)
# keys("a",employee)
##___________________________________________________________________##
    #wap to make a function which sum all the key of dictionary        
# d={
#   1:"a",
#   2:"b"  
# }    
# d1={
#   10:"c",
#   20:"d"  
# }    

# def sum_keys(dict):
#     print(sum(dict.keys()))
# sum_keys(d)
# sum_keys(d1)



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class Linkedlist:
#     def __init__(self):
#         self.head=None
        
#     def insert(self,newnode):
        
#         if self.head is None:
#             self.head=newnode
#         else:
#             lastnode=self.head
#             while True:
#                 if lastnode.next is None:
#                     break
#                 lastnode=lastnode.next
#             lastnode.next=newnode
            
# firstnode=Node("jalay")
# l1=Linkedlist()
# secondnode=Node("panchal")
# l1.insert(secondnode)



# class Node:
#         def __init__(self,data):
#             self.data=data
#             self.next=None
                                
# class Linkedlist:
#         def __init__(self):
#             self.head=None
            
#         def insert(self,newNode):    
            
#             if self.head is None:
#                 self.head=newNode
#             else:
#                 lastNode=self.head
                
#             while True:        
#                if lastNode.next is None:
#                     break
#                 lastNode=lastNode.next 
#             lastNode.next=newNode         

# firstNode=Node("yash")
# l1=Linkedlist()
# secondNode=Node("patel")
# l1.insert(secondNode)

##________________________________________________________________________________________##
#wap to make a class Person , add att birth_year and add method calculate age,
# to calculate persons age

# class Person:
    
#     def __init__(self,birth_year):
#         self.birth_year=birth_year
        
#     def calculate_age(self):
#         current_year =2024
#         return current_year - self.birth_year

# Person=Person(2002)
# print(Person.calculate_age())
##________________________________________________________________________________________##

#wap to make a class Animal , add 2  methods and make them static

# class Animal:
    
#     @staticmethod
#     def sound():
#         return "The animal makes a sound."

#     @staticmethod
#     def eat():
#         return "The animal is eating."

# print(Animal.sound())  
# print(Animal.eat())
##________________________________________________________________________________________##

#Account, add attrubutes Accno and balance (in constructor)
#make them hide so that no one can get it outside class


# class Account:
#     def __init__(self,accno,balance):
#         self.__accno=accno
#         self.__balance=balance
        
#     def print_details(self):
#         print("account no is : ",self.__accno)
#         print("account balance is : ",self.__balance)
        
# obj1=Account("acc123",500000) 
# print(obj1.print_details())       
           
##________________________________________________________________________________________##
           
#wap to make a class Bike with one attribute , make a sub class apache with any attribute
#make b1 object in Bike() and A1 object in Apache(), check that both objects are
#instance of Bike() class or not 

# class Bike:
#     model=2024
 
# class Apache(Bike):
#     color="black"
    
# b1=Bike()
# a1=Apache()        

# print(isinstance(b1,Bike))
# print(isinstance(b1,Apache))

##________________________________________________________________________________________##
# Write a  Python class that has two methods: get_String and print_String ,
# get_String accept a string from the user and
# print_String prints the string in upper case.  
# Write a Python class to reverse a string word by word.

##________________________________________________________________________________________##


# Write a  Python program to create a class representing a  shopping cart.
# Include methods for adding(itemname,qyt) and removing items, and calculating the total quantity.



# class Shoipng_cart:
    
#     def __init__(self):
#         self.items=[]
        
#     def add_item(self,itemname,qty):
#         item=(itemname,qty)
#         self.items.append(item)
        
#     def remove_item(self,itemname):
#         for item in self.items:
#             if item[0]==itemname:
#                 self.items.remove(item)       
     
#     def calc_qty(self):
#         qty=0
#         for item in self.items:
#             qty +=item[1]
            
#         print("total quantity is : ",qty)
        
#     def show(self):
#         print("items in cart are : ",self.items)
        
# obj1=Shoipng_cart()
# obj1.add_item("apple",20)
# obj1.add_item("banana",20)
# obj1.add_item("mango",20)

# obj1.show

# obj1.remove_item("apple")
# obj1.show()
# obj1.calc_qty()
                
##________________________________________________________________________________________##
                
#  Write a Python program to create a person class. 
#  Include attributes like name, country and date of birth.
#  Implement a method to determine the person's age  using datetime module                

# from datetime import date

# class Person:
    
#     def __init__(self,name,country,dob):
#         self.name=name
#         self.dob=dob
    
#     def calc_age(self):
#        today = date.today()
#        age = today.year - self.dob
#        print("Your age is = ",age)   

# obj1=Person()
# obj1.name=()  
# obj1.country=()
# obj1.dob=()

##________________________________________________________________________________________##

# Write a  Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions    
#use dictionary{} to create account where key is acc_no and value is balance 
#add method make deposit to deposit amount 
# add method make_withdrawal to withdraw amount but after checking that balance should not 
#be less than 500
#add method show to show balance

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, acc_no, balance):
#         self.accounts[acc_no] = balance

#     def deposit(self, acc_no, amount):
#         if acc_no in self.accounts:
#             self.accounts[acc_no] += amount
#             print("Deposit successful. New balance: {self.accounts[acc_no]}")
#         else:
#             print("Account not found.")

# bank = Bank()
# bank.create_account("467826473", 400000)
# bank.deposit("467826473", 500000)





# def sum_of_even_and_odd_numbers(*args):
    
#     even_sum = 0
#     odd_sum = 0
    
#     for num in args:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num
#     print("Sum of even numbers:", even_sum)
#     print("Sum of odd numbers:", odd_sum)


# sum_of_even_and_odd_numbers(23,65,76,45,23,65,98,94)




##print palindrom numbers

# def palindrome_numbers(n):
#     for i in range(1, n+1):
#         if str(i) == str(i)[::-1]:
#             print(i)

# palindrome_numbers(100)
