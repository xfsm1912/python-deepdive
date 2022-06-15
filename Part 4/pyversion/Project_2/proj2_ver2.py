from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupported type for modulus')
        if not isinstance(value, int):
            raise TypeError('Unsupported type for value')
        if modulus <= 0:
            raise ValueError('Modulus must be positive')

        self._modulus = modulus
        self._value = value % modulus  # store residue as the value

    @property
    def modulus(self):
        return self._modulus

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f'Mod({self._value}, {self._modulus})'

    def __int__(self):
        # calculate the value (residue)
        return self.value

    def _get_value(self, other):
        if isinstance(other, int):
            return other % self.modulus  # return the residue
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible types.')

    def __eq__(self, other):
        # calculate congruence (same equivalence class)
        other_value = self._get_value(other)
        return other_value == self.value

    def __hash__(self):
        # The hash() method returns the hash value of an object if it has one.
        return hash((self.value, self.modulus))

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __add__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value + other_value, self.modulus)

    def __iadd__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value + other_value) % self.modulus

    def __sub__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value - other_value, self.modulus)

    def __isub__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value - other_value) % self.modulus
        return self

    def __mul__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value * other_value, self.modulus)

    def __imul__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value * other_value) % self.modulus
        return self

    def __pow__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value ** other_value, self.modulus)

    def __ipow__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value ** other_value) % self.modulus
        return self

    def __lr__(self, other):
        # here, raising a TypeError instead of returning NotImplemented
        # would result in Python not trying the reflection - which we DO want
        # although since we are using @total_ordering this does not really matter
        try:
            other_value = self._get_value(other)
            return self.value < other_value
        except TypeError:
            return NotImplemented
