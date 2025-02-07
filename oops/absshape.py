from abstract2 import Shape

class Cirlce(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    
    def pera(self):
        return 2*3.14*self.radius
    
class Rectagle(Shape):

    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b
    
    def pera(self):
        return 2*(self.l+self.b)
    
c=Cirlce(10)
print(c.area())
print(c.pera())

r=Rectagle(10,20)
print(r.area())
print(r.pera())