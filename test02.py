import unittest
from tasks.ex02 import (prime_factors, product_numbers)

class Test(unittest.TestCase):

    def test_prime_factors(self):
        self.assertEqual(prime_factors(7), [7,1])

    def test_prime_factor_hard(self):
        self.assertEqual(prime_factors(99), [3,11,3])

    def test_product_num(self):
        self.assertEqual(product_numbers(3), [1,2,6])

if __name__ == '__main__':
    unittest.main()
