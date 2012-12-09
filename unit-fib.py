# -*- coding: utf-8 -*-
import unittest

from fibonacci import cuenta_fib

class TestCalculoFibonacci(unittest.TestCase):
    def testLnds(self):
        self.assertEqual(cuenta_fib(1234567890, 9876543210), 4)
        self.assertEqual(cuenta_fib(9876543210, 1234567890), 4)

    def testVacio(self):
        self.assertEqual(cuenta_fib(14, 20), 0)

    def testBorde(self):
        self.assertEqual(cuenta_fib(5, 6),1)


if __name__ == '__main__':
    unittest.main()
