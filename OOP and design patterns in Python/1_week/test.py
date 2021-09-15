import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    result = []
    if x == 0:
        return (0,)
    elif x == 1:
        return (1,)
    else:
        i = 2
        while x != 1:
            while x % i == 0:
                result.append(i)
                x /= i
            i += 1
    return tuple(result)


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        """Args with type float or str, call TypeError"""
        cases = ('string', 1.5)
        for var in cases:
            with self.subTest(x=var):
                self.assertRaises(TypeError, factorize, var)

    def test_negative(self):
        """Negative numbers call ValueError"""
        cases = (-1, -10, -100)
        for num in cases:
            with self.subTest(x=num):
                self.assertRaises(ValueError, factorize, num)

    def test_zero_and_one_cases(self):
        """Int numbers 0 and 1, returns tuple (0,), (1,)"""
        cases = (0, 1)
        for num in cases:
            with self.subTest(x=num):
                self.assertTupleEqual(factorize(num), (num,))

    def test_simple_numbers(self):
        """For simple numbers, func should return tuple contain one simple number"""
        cases = (3, 13, 29)
        for num in cases:
            with self.subTest(x=num):
                self.assertTupleEqual(factorize(num), (num,))

    def test_two_simple_multipliers(self):
        """For this numbers, func returns tuple with length=2"""
        cases = (6, 26, 121)
        excpected = ((2, 3), (2, 13), (11, 11))
        for pos, num in enumerate(cases):
            with self.subTest(x=num):
                self.assertTupleEqual(factorize(num), excpected[pos])

    def test_many_multipliers(self):
        """For this numbers, func returns tuple with length>2"""
        cases = (1001, 9699690)
        excpected = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for pos, num in enumerate(cases):
            with self.subTest(x=num):
                self.assertTupleEqual(factorize(num), excpected[pos])


if __name__ == '__main__':

    unittest.main()

