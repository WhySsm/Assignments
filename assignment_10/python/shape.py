from mimetypes import init


class Shape():
    def __init__(self) :
        self.area=0
        self.perimeter=0


class Rectangle (Shape):
    def __init__(self,l,w):
        super().__init__()
        self.length=l
        self.width=w
        
    def Area(self):
        self.area=self.length*self.width
        
        
    def Perimeter(self):
        self.perimeter=(self.length+self.width)*2  
         
    def Show(self):
        print("Rectangle\n","Area : ",self.area,"\nPerimeter : ",self.perimeter)

class Circle(Shape):
    def __init__(self,r):
        super().__init__()
        self.radius=r
    
    def Area(self):
        self.area=6.28*(self.radius)
        
    def Perimeter(self):
        self.perimeter=3.14*self.radius*self.radius 
    
    def Show(self):
        print("\nCircle\n","Area : ",self.area,"\nPerimeter : ",self.perimeter)
obj1=Rectangle(3,4)
obj1.Area()
obj1.Perimeter()
obj1.Show()

obj2=Circle(2)
obj2.Area()
obj2.Perimeter()
obj2.Show()