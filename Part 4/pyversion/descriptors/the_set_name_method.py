class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string.')
        if len(value) < self.min_length:
            raise ValueError(f'{self.property_name} must be at least '
                             f'{self.min_length} characters'
                             )
        # if we write as: setattr(instance, self.property_name, value),
        # as we run p.first_name = 'Alex', the instance will fall into infinite loop.
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'calling __get__ for {self.property_name}')
            return instance.__dict__.get(self.property_name, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)


p = Person()
print(p.__dict__)
p.first_name = 'Alex'
print(p.__dict__)
print(p.first_name)
