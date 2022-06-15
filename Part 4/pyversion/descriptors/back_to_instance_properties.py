import weakref


class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))


class Point:
    x = IntegerValue()

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x


# p = Point()
# print(hex(id(p)))

p = Point(10.1)
weak_p = weakref.ref(p)

print(hex(id(p)), weak_p)

del p

print(weak_p)
