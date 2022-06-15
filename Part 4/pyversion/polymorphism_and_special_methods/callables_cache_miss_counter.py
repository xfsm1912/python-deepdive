from collections import defaultdict

class DefaultValue:
    def __init__(self, default_value):
        self.default_value = default_value
        self.counter = 0

    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')

    def __call__(self):
        self.counter += 1
        return self.default_value

cache_def_1 = DefaultValue(None)
cache_def_2 = DefaultValue(0)

cache_1 = defaultdict(cache_def_1)
cache_2 = defaultdict(cache_def_2)

print(cache_1['a'], cache_1['b'], cache_1['a'])
print(cache_def_1.counter)
print(cache_2['a'], cache_2['b'], cache_2['c'])
print(cache_def_2.counter)
