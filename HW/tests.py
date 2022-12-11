import unittest
from fibonacci import func_fib

class test_fib(unittest.TestCase):
    def test_1(self):
        b = func_fib()
        fib_numbers = [next(b) for i in range(5)]
        self.assertEqual(fib_numbers, [0, 1, 1, 2, 3])

    def test_2(self):
        b = func_fib()
        fib_numbers = [next(b) for i in range(2)]
        self.assertEqual(fib_numbers, [0, 1])

    def test_3(self):
        b = func_fib()
        fib_numbers = [next(b) for i in range(10)]
        self.assertEqual(fib_numbers, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == "__main__":
    unittest.main()