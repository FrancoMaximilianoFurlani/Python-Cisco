import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = math.sqrt((self.vertices[1].x - self.vertices[0].x)
                          ** 2 + (self.vertices[1].y - self.vertices[0].y) ** 2)
        side2 = math.sqrt((self.vertices[2].x - self.vertices[1].x)
                          ** 2 + (self.vertices[2].y - self.vertices[1].y) ** 2)
        side3 = math.sqrt((self.vertices[0].x - self.vertices[2].x)
                          ** 2 + (self.vertices[0].y - self.vertices[2].y) ** 2)
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
