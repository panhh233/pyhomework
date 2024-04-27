class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Line(object):
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
    
        if self.point1.x == self.point2.x:
            self.slope = None 
        else:
            self.slope = (self.point1.y - self.point2.y) / (self.point1.x - self.point2.x)
    
    def relationship(self, other):
        if self.slope == other.slope:
            print('平行') 
        else:
            print('相交')

x1, y1 = eval(input())
x2, y2 = eval(input())
x3, y3 = eval(input())
x4, y4 = eval(input())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)
p4 = Point(x4, y4)

distance = p1.distance(p2)
print('两点的欧式距离是{:.2f}'.format(distance))

line1 = Line(p1, p2)
line2 = Line(p3, p4)

line1.relationship(line2)