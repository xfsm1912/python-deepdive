from math import pi
from numbers import Real

class Circle:
    def __init__(self, r):
        # but if use self.radius, when we create u = UnitCircle, the self.radius is the radius() in the instance u,
        # not the setter function in the Circle class.
        # So we use set_radius function to avoid the replicate name self.radius
        self.set_radius(r)
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    # So we use set_radius function to avoid the replicate name self.radius
    def set_radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must be a positive real number')

    @radius.setter
    def radius(self, r):
        self.set_radius(r)

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
u.radius = 10.0
