#ABSTRACTION  MEANING ==> HIDDEN
from abstract import Person

class Human(Person):
    
    def __init__(self, n):
        super().__init__(n)
        print("human has legs",n)
        
    def sleep(self):
        print("human sleeps 8 hrs")
        
    def eat(self):
        print("humans eats veg and non-veg")
        
obj1=Human(2)
obj1.eat()
obj1.sleep()            