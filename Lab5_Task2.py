class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y    

class Rectangle():
    def __init__(self,height,width,corner=Point(0,0)):
        self.height = height
        self.width = width
        self.corner = corner

def centre(self):
    self.x = self.corner.x + (self.height / 2)
    self.y = self.corner.y + (self.width / 2)
    return (self.x, self.y)


p = int(input("enter x coordinates of corner: "))
q = int(input("enter y coordinates of corner: "))
height = int(input("enter the Height: "))
width = int(input("enter the width: "))
box = Rectangle(height, width, corner=Point(p, q))
print(box.centre())  
