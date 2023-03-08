class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return float(self._x)

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("the value must be 'int' or 'float' type")

        self._x = value

    @property
    def y(self):
        return float(self._y)

    @y.setter
    def y(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError("the value must be 'int' or 'float' type")

        self._y = value

    def distance_to_origin(self):
        return (self._x**2+self._y**2)**(1/2)

    def __add__(self, c):
        if not isinstance(c, Coordinate):
            raise TypeError("the value must be Coordinate")
        nx = c._x+self.x
        ny = c._y+self.y
        return Coordinate(nx, ny)

    def __sub__(self, c):
        if not isinstance(c, Coordinate):
            raise TypeError("the value must be Coordinate")
        nx = self.x-c.x
        ny = self.y-c.y
        return Coordinate(nx, ny)
