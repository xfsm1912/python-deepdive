import numbers


class BaseValidator:
    def __init__(self, min_=None, max_=None):
        # avoid to overwrite the built-in function min and max.
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

    def validate(self, value):
        # this will need to be implemented specifically by each subclass
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.prop_name] = value

class IntegerField:
    def __init__(self, min_=None, max_=None):
        # avoid to overwrite the built-in function min and max.
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer value.')

        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')

        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}.')

        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self

        return instance.__dict__.get(self.prop_name, None)

class CharField:
    def __init__(self, min_=None, max_=None):
        min_ = min_ or 0
        min_ = max(0, min_)
        # avoid to overwrite the built-in function min and max.
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')

        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} char.')

        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} char.')

        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self

        return instance.__dict__.get(self.prop_name, None)


class IntegerField_inherit(BaseValidator):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be an integer value.')

        if self._min is not None and value < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min}.')

        if self._max is not None and value > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max}.')

class CharField_inherit(BaseValidator):
    def __init__(self, min_, max_):
        super().__init__(min_, max_)
        min_ = max(min_ or 0, 0)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be a string.')

        if self._min is not None and len(value) < self._min:
            raise ValueError(f'{self.prop_name} must be >= {self._min} char.')

        if self._max is not None and len(value) > self._max:
            raise ValueError(f'{self.prop_name} must be <= {self._max} char.')

class Person:
    age = IntegerField(0, 100)
    name = CharField(1, 10)
    # name = CharField(1)


p = Person()
p.age = 5
print(p.age)

p.name = 'John'
print(p.name)

try:
    p.age = 200
except ValueError as ex:
    print(ex)

try:
    p.name = 'Python Rocks!'
except ValueError as ex:
    print(ex)

