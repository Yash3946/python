#wap to make a class Linkedlist to insert ,delete and to show values of nodes

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
#             # self.head.next=newnode
#             lastnode=self.head
#             while True:
#                 if lastnode.next is None:
#                     break
#                 lastnode=lastnode.next
#             lastnode.next=newnode
            
#     def printlist(self): 
#         currentnode=self.head
#         while True:
#             if currentnode is None:
#                 break    
#             print(currentnode.data)
#             currentnode=currentnode.next  
            
# firstnode=Node("vrutik")
# l1=Linkedlist()
# l1.insert(firstnode)
# secondnode=Node("patel")
# l1.insert(secondnode)
# l1.printlist()
##______________________________________________________________________________________##

# Write a  Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square.

# class Shape:
    
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def _init_(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# class Triangle(Shape):
#     def _init_(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def area(self):
#         return (self.a + self.b + self.c) / 2

##______________________________________________________________________________________##

#  Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price,and 
#  methods like add_item, update_item, and check_item_details.
# Use a dictionary to store the item details, 
# where the key is the item_id and the value is a dictionary containing the item_name, 
# stock_count, and price           


# class Inventory:
    
#     def __init__(self):
#         self.Inventory={}
    
#     def add_items(self,item_id,item_name,stock_count,price):
#         self.Inventory[item_id]={"item name" : item_name,
#                                  "counting of stock":stock_count,
#                                  "price":price            
#                                 }
#     def update(self,item_id,stock_count,price):
#             if item_id in self.Inventory:
#                 self.Inventory[item_id]["counting of stock"]=stock_count
#                 self.Inventory[item_id]["price"]=price
#             else:
#                 price("item is not found")
                
#     def delete(self,item_id,item_name):
#         if item_id in self.Inventory:
#             self.Inventory[item_id]["delete of stock"]=stock_count
            
        
        
#     def check_item_details(self):  
#         print(self.Inventory)
        
# i1=Inventory()
# i1.add_items("a11","laptop",10,50000)       
# i1.add_items("a12","mobile",15,70000)
# i1.add_items("a13","charger",14,5000)

# i1.check_item_details()

# i1.update("a11",5,67000) 
# i1.update("a12",8,65000)

# i1.check_item_details() 
##______________________________________________________________________________________##
      
       
# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods 
# like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked,
# which is the number of hours worked by the employee. If the number of hours worked is more than 50, 
# the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked – 50
# Overtime amount = (overtime * (salary / 50))       


class Employee:
    def __init__(self,emp_name,emp_id,emp_salary,emp_department):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_salary=emp_salary
        self.emp_dep=emp_department

    def calculate_emp_salary(self,hours_worked):
        if hours_worked > 50:
            overtime=hours_worked - 50
            overtime_amount=(overtime * (self.emp_salary/50))
            print("Overtime Salary; ",overtime_amount)
            print("total salary is ",self.emp_salary+overtime_amount)

        else:
            print("employee salary is: ",self.emp_salary)

    def assign_department(self,department):
        self.emp_dep=department

    def print_employee_details(self):
        print("Employee Id", self.emp_id, "\nEmployee NAme", self.emp_name, "\nEmployee Salary", self.emp_salary, "\nemployee Department", self.emp_dep)

e1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
e1.calculate_emp_salary(55)
e1.assign_department("Sales")

e1.print_employee_details()
        