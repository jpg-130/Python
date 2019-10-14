"""Uses Pythagoras theorem to calculate the distance between two points in space."""

import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

def distance(a, b):
    """
    >>> distance(Point(2, -1, 7),Point(1, -3, 5))
    3.0
    >>> distance(Point(0, 0, 1),Point(0, 0, 2))
    1.0
    """
    return math.sqrt(abs(((b.x - a.x)**2 + (b.y - a.y)**2 + (b.z - a.z)**2)))

if __name__ == "__main__":
    point1 = Point(2, -1, 7)
    point2 = Point(1, -3, 5)

    import doctest
    doctest.testmod()
