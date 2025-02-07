# inheritance = >feature using by child  class of parent  class is inheritance

# class gen1:     #parent class
    
#     land="100acre"
#     @staticmethod
#     def bachho():
#         print("moj karo")

# class gen2(gen1):       #child class and parent class
    
#     gold="100carot"
    
# class gen3(gen2):
    
#     bussiness="it company"
     
# obj1=gen3    
# print("baccho",obj1.bachho())
# print(obj1.land)
# print(obj1.gold)

##______________________________________________________________________________##
#types of inheritance
#1- single level inheritance
#2- multi level inheritance
#3- multiple inheritance  -> when we have more than 1 parent
##______________________________________________________________________________##


# class G1:
    
#     land="100acre"
# class G2:
    
#     gold="500carot"
    
# class G3(G1,G2):
    
#     att="null"
    
# o1=G3()
# print(o1.gold)
# print(o1.land)
# print(o1.att)
##______________________________________________________________________________##
                             # multilevel
##______________________________________________________________________________##

# class Animal:
#     flying_speed="40km/h"
# class Bird(Animal):
#     color="green"
# class Parot(Bird):
#     age="1 year"
# obj1=Parot
# print(obj1.color)        
        
##______________________________________________________________________________##
                             # multiple
##______________________________________________________________________________##
# class Animal:
#     flying_speed="40km/h"
# class Bird:
#     color="green"
# class Parot(Animal,Bird):
#     age="1 year"
# obj1=Parot
# print(obj1.color)         
# print(obj1.age)         
##______________________________________________________________________________##
            
            
#wap to make class Queue, include method for enque and deque    
    
# class Queue:
    
#     def __init__(self):
#         self.items=[]
        
#     def enque(self,item):
#         self.items.append(item)
        
#     def is_empty(self):
#         return len(self.items)==0
#         # if len(self.items)==0:
#         #     print("empty")
#         # else:
#         #     print("not empty")
            
#     def deque(self):
#         if not self.is_empty():
#             self.items.pop(0)
#         else:
#             print("cant deque from empty queue")      
##______________________________________________________________________________##

    #super()-> to inherit the attributes of parent class constructor; super() is used
