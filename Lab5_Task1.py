class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def dist(p,q):
         distance = ((p.x-q.x)**2 + (p.y-q.y)**2)**(1/2)
         #print(f"Distance between the point is: {distance}")
         return (distance)         

x = int(input("Enter x for A point "))
y = int(input("Enter y for A point "))
a = Point(x,y)

x = int(input("Enter x for B point "))
y = int(input("Enter y for B point "))
b = Point(x,y)


#print(f"Distance is {dist(a,b)}")
