import unittest
from tasks.ex01 import (delet_symbol, sum_num, inject,sum_odd)

class Test(unittest.TestCase):

    def test_symbol_del(self):
        self.assertEqual(delet_symbol('аб ав ро'), 'ро')

    def test_symbol(self):
        self.assertEqual(delet_symbol('Произрастает Дикая Тайга'), '')

    def test_sum(self):
        self.assertEqual(sum_num(1234), 10)

    def test_sum_float(self):
        self.assertEqual(sum_num(0.34), 7)

    def test_inject(self):
        self.assertTrue(inject(14))

    def test_except_inject(self):
        self.assertRaises(Exception,inject('dsa'))

    def test_odd(self):
        self.assertEqual(sum_odd([1,2,3,4,5,6]), 12)



if __name__ == '__main__':
    unittest.main()
