import unittest
from shingle_utilities import shingles


class TestShingles(unittest.TestCase):
    def test_shingles(self):
        # test with normal valid input
        t = ['one', 'two', 'three', 'four']
        k = 2
        result = shingles(t, k)
        self.assertEqual(result, {('one', 'two'): 1, ('two', 'three'): 1,
                                  ('three', 'four'): 1})

        # test with valid input with repeated words
        t = ['one', 'two', 'three', 'four', 'one', 'two', 'three', 'four']
        k = 2
        result = shingles(t, k)
        self.assertEqual(result, {('one', 'two'): 2, ('two', 'three'): 2,
                                  ('three', 'four'): 2, ('four', 'one'): 1})

        # test with valid input where k is greater than the length of t
        t = ['one', 'two', 'three', 'four']
        k = 5
        result = shingles(t, k)
        self.assertEqual(result, {})

        # test with valid input where k is equal to the length of t
        t = ['one', 'two', 'three', 'four']
        k = 4
        result = shingles(t, k)
        self.assertEqual(result, {('one', 'two', 'three', 'four'): 1})

        # test with invalid input where k is equal to 0
        t = ['one', 'two', 'three', 'four']
        k = 0
        with self.assertRaises(ValueError):
            shingles(t, k)

        # test with invalid input where k is not an integer
        t = ['one', 'two', 'three', 'four']
        k = "str"
        with self.assertRaises(TypeError):
            shingles(t, k)

        # test with invalid input where there are non-string elements in t
        t = ['one', 'two', 'three', 'four', 123]
        k = 2
        with self.assertRaises(TypeError):
            shingles(t, k)

        # test with invalid input where t is not a list
        t = 'one two three four'
        k = 2
        with self.assertRaises(TypeError):
            shingles(t, k)


if __name__ == '__main__':
    unittest.main()

