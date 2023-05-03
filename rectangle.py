from abc import ABC,  abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self,r):
        self.__radius = r
    
    def get_area(self):
        return (self.__radius**2)*3.14


class Rectangle(Shape):
    def __init__(self, a, b):
        self.__height = a
        self.__width = b

    def get_area(self):
        return self.__height*self.__width


class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)
    
        
rechteck = Rectangle(10,5)
print(rechteck.get_area())

quadrat = Square(10)
print(quadrat.get_area())

kreis = Circle(5)
print(kreis.get_area())