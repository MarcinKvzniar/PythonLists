import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_degree_valid_input(self):
        pol1 = Polynomial([4, 3.7, 2, 1, 1])
        self.assertEqual(pol1.degree(), 4)
        pol2 = Polynomial([0])
        self.assertEqual(pol2.degree(), 0)

    def test_degree_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['A', 4, -0, 4])
            pol1.degree()

    def test_str_valid_input(self):
        pol1 = Polynomial([3, 2, 1])
        self.assertEqual(str(pol1), "3x^2 + 2x + 1")
        pol2 = Polynomial([-1, 0, 172, -18, 0])
        self.assertEqual(str(pol2), "-x^4 + 0x^3 + 172x^2 + -18x + 0")

    def test_str_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['A', 4, -0, 4])
            str(pol1)

    def test_call_valid_input(self):
        pol1 = Polynomial([-3, 7, 4])
        self.assertEqual(pol1.__call__(2), 6)
        pol2 = Polynomial([-42, 32, -1.5, 3.7, 0, 2])
        self.assertEqual(pol2.__call__(2), -827.2)

    def test_call_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['cadsa', 4.11, -0, 4])
            pol1.__call__(2)
            pol2 = Polynomial([2, 3, 4, 5])
            pol2.__call__('a')

    def test_add_valid_input(self):
        pol1 = Polynomial([1, 2, 4])
        pol2 = Polynomial([-4, 7])
        pol3 = Polynomial([3.7, 0, 3.1])
        result = pol1 + pol2
        self.assertEqual(result.coefficients, [1, -2, 11])
        result2 = pol1 + pol3
        self.assertAlmostEqual(result2.coefficients, [4.7, 2, 7.1])

    def test_add_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['acgt', 4.11, -0, 4])
            pol2 = Polynomial([4, 3, 7, 1])
            pol1 + pol2

    def test_sub_valid_input(self):
        pol1 = Polynomial([1, 2, 1])
        pol2 = Polynomial([1, -1])
        pol3 = Polynomial([-1.4, 0, -2.1])
        result = pol1 - pol2
        self.assertEqual(result.coefficients, [1, 1, 2])
        result2 = pol1 - pol3
        self.assertEqual(result2.coefficients, [2.4, 2, 3.1])

    def test_sub_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['acgt', 4.11, -0, 4])
            pol2 = Polynomial([4, 3, 7, 1])
            pol1 - pol2

    def test_mul_valid_input(self):
        pol1 = Polynomial([1, 2, 1])
        pol2 = Polynomial([1, 1, 1])
        pol3 = Polynomial([4.1, 0, 2.4])
        result = pol1 * pol2
        result2 = pol1 * pol3
        self.assertEqual(result.coefficients, [1, 3, 4, 3, 1])
        self.assertEqual(result2.coefficients, [4.1, 8.2, 6.5, 4.8, 2.4])

    def test_mul_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['acgt', 4.11, -0, 4])
            pol2 = Polynomial([4, 3, 7, 1])
            pol1 * pol2

    def test_iadd_valid_input(self):
        pol1 = Polynomial([1, 2, 1])
        pol2 = Polynomial([1, 1])
        pol3 = Polynomial([4.1, 0, 2.4])
        pol1 += pol2
        self.assertEqual(pol1.coefficients, [1, 3, 2])
        pol2 += pol3
        self.assertEqual(pol2.coefficients, [4.1, 1, 3.4])

    def test_iadd_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['acgt', 4.11, -0, 4])
            pol2 = Polynomial([4, 3, 7, 1])
            pol1 += pol2

    def test_isub_valid_input(self):
        pol1 = Polynomial([4, 2, -5])
        pol2 = Polynomial([1, 1, 5, -1])
        pol3 = Polynomial([2.1, 0, 5.4])
        pol1 -= pol2
        self.assertEqual(pol1.coefficients, [-1, 3, -3, -4])
        pol2 -= pol3
        self.assertEqual(pol2.coefficients, [1, -1.1, 5, -6.4])

    def test_isub_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['acgt', 4.11, -0, 4])
            pol2 = Polynomial([4, 3, 7, 1])
            pol1 -= pol2

    def test_imul(self):
        pol1 = Polynomial([4, 2, 1])
        pol2 = Polynomial([3, 1, 0])
        pol3 = Polynomial([3.1, 0, 9.5])
        pol1 *= pol2
        self.assertEqual(pol1.coefficients, [12, 10, 5, 1, 0])
        pol2 *= pol3
        self.assertEqual(pol2.coefficients, [9.3, 3.1, 28.5, 9.5, 0.0])

    def test_imul_invalid_input(self):
        with self.assertRaises(ValueError):
            pol1 = Polynomial(['acgt', 4.11, -0, 4])
            pol2 = Polynomial([4, 3, 7, 1])
            pol1 *= pol2


if __name__ == '__main__':
    unittest.main()
