import unittest
from solution import IntegerField, Person, CharField

class TestIntegerField(unittest.TestCase):
    class Person:
        # here, set name (prop_name) pass age.
        age = IntegerField(0, 10)

    def create_person(self, min_, max_):
        # but here we define the IntegerField without prop_name
        self.Person.age = IntegerField(min_, max_)
        # so here we need to pass age into prop_name. But this way is not clean
        self.Person.age.__set_name__(Person, 'age')

        return self.Person()

    def test_set_age_ok(self):
        p = self.Person()
        p.age = 0
        self.assertEqual(0, p.age)

    # def test_set_age_ok_with_min_max(self):
    #     # but here we define the IntegerField without prop_name
    #     self.Person.age = IntegerField(5, 10)
    #     # so here we need to pass age into prop_name. If comment this line, the test will fail.
    #     self.Person.age.__set_name__(Person, 'age')
    #
    #     p = self.Person()
    #     p.age = 5
    #     self.assertEqual(5, p.age)

    def test_set_age_ok_with_min_max(self):
        min_ = 5
        max_ = 10
        p = self.create_person(min_, max_)

        p.age = 5
        self.assertEqual(5, p.age)

    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': IntegerField(min_, max_)})

        return obj()

    def test_set_age_ok_with_min_max_create_class(self):
        min_ = 5
        max_ = 10
        p = self.create_test_class(min_, max_)

        p.age = 5
        self.assertEqual(5, p.age)

    def test_set_age_ok_with_valid_values(self):
        """Tests that valid values can be assigned/retrieved"""
        min_ = 5
        max_ = 10
        obj = self.create_test_class(min_, max_)

        valid_values = range(min_, max_ + 1)

        for i, value in enumerate(valid_values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_invalid(self):
        """Tests that invalid values raise ValueError exceptions"""
        min_ = -10
        max_ = 10
        obj = self.create_test_class(min_, max_)

        bad_values = list(range(min_ - 5, min_))
        bad_values += list(range(max_ + 1, max_ + 5))
        bad_values += [10.5, 1 + 0j, 'abv', (1, 2)]

        for i, value in enumerate(bad_values):
            with self.subTest(test_number=i):
                with self.assertRaises(ValueError):
                    obj.age = value

    def test_class_get(self):
        """Tests that class attribute retrieval returns the descriptor instance"""
        obj = self.create_test_class(0, 0)
        obj_class = type(obj)

        self.assertIsInstance(obj_class.age, IntegerField)

    def test_set_age_min_only(self):
        """Tests that we can specify a min value only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(min_, min_ + 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_max_only(self):
        """Tests that we can specify a max value only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        values = range(max_ - 100, max_, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

    def test_set_age_no_limits(self):
        """Tests that we can use IntegerField without any limits"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        values = range(-100, 100, 10)
        for i, value in enumerate(values):
            with self.subTest(test_number=i):
                obj.age = value
                self.assertEqual(value, obj.age)

class TestCharField(unittest.TestCase):
    @staticmethod
    def create_test_class(min_, max_):
        obj = type('TestClass', (), {'age': CharField(min_, max_)})

        return obj()

    def test_set_name_ok(self):
        """Tests that valid can be assigned/retrieved"""
        min_ = 1
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_length = range(min_, max_ + 1)

        for i, length in enumerate(valid_length):
            value = 'a' * length
            with self.subTest(test_number = i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_max_only(self):
        """Tests that we can specify a max length only"""
        min_ = None
        max_ = 10
        obj = self.create_test_class(min_, max_)
        valid_length = range(max_ - 100, max_, 10)

        for i, length in enumerate(valid_length):
            value = 'a' * length
            with self.subTest(test_number = i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_min_only(self):
        """Tests that we can specify a max length only"""
        min_ = 0
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_length = range(min_, min_ + 100, 10)

        for i, length in enumerate(valid_length):
            value = 'a' * length
            with self.subTest(test_number = i):
                obj.name = value
                self.assertEqual(value, obj.name)

    def test_set_name_no_limits(self):
        """Tests that we can specify a max length only"""
        min_ = None
        max_ = None
        obj = self.create_test_class(min_, max_)
        valid_length = range(0, 100, 10)

        for i, length in enumerate(valid_length):
            value = 'a' * length
            with self.subTest(test_number = i):
                obj.name = value
                self.assertEqual(value, obj.name)


if __name__ == '__main__':
    unittest.main()
