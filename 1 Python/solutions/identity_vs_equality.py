
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y


p1 = Point(5, 2)
p2 = Point(5, 2)

print(id(p1))
print(id(p2))
print(p1 is p2)
print(p1 == p2)