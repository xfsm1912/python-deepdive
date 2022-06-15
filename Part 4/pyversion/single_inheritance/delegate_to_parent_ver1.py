from math import pi
from numbers import Real

class Circle:
    def __init__(self, r):
        # if self._r = r, the r will not be checked for the real and positive
        # so we can use self.radius = r, calling the radius setter function
        self._r = r
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must be a positive real number')

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius

    # @radius.setter
    # def radius(self, value):
    #     self._radius = value


u = UnitCircle()
print(u.radius)
# AttributeError: can't set attribute
# since we don't want to change the unit radius in unitcircle.
u.radius = 10.0
