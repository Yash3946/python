#wap to make a class Polygon , make child class triangle,quadrilateral,pentagon,hexagon
#to print no of sides only, hide the class polygon and run method sides of child classes

from abc import ABC,abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def sides(self):
        pass
    
       