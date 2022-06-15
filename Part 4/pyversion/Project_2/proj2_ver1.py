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
        self._value = value % modulus # store residue as the value

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

    def __eq__(self, other):
        if isinstance(other, Mod):
            if self.modulus != other.modulus:
                return NotImplemented
            else:
                return self.value == other.value
        elif isinstance(other, int):
            return other % self.modulus == self.value
        else:
            return NotImplemented

    def __hash__(self):
        # The hash() method returns the hash value of an object if it has one.
        return hash((self.value, self.modulus))

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __add__(self, other):
        # this part has the same logic in function __eq__
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value + other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value + other, self.modulus)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value + other.value) % self.modulus
            return self
        elif isinstance(other, int):
            self.value = (self.value + other) % self.modulus
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value - other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value - other, self.modulus)
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value - other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value - other) % self.modulus
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value * other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value * other, self.modulus)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value * other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value * other) % self.modulus
            return self
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value ** other.value, self.modulus)
        if isinstance(other, int):
            # use residue of other, to make computation potentially smaller
            return Mod(self.value ** (other % self.modulus), self.modulus)
        return NotImplemented

    def __ipow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value ** other.value) % self.modulus
            return self
        if isinstance(other, int):
            # use residue of other, to make computation potentially smaller
            self.value = (self.value ** (other % self.modulus)) % self.modulus
            return self
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return self.value < other.value
        if isinstance(other, int):
            return self.value < other % self.modulus
        return NotImplemented





