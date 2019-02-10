class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y    

class Rectangle():
    def __init__(self,height,width,corner=Point(0,0)):
        self.height = height
        self.width = width
        self.corner = corner

  
