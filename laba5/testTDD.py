import unittest
from unique import Testing

class UniqueTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Testing([1, 3, 1, 2, 5, 2]),
            [1, 3, 2, 5]
        )
    def test_1(self):
        self.assertEqual(
            Testing([1, 3, 1, 2, 5, 2]),
            [1, 3, 2, 5]
        )
    def test_empty(self):
        self.assertEqual(
            Testing([]),
            []
        )
    def test_single(self):
        self.assertEqual(
            Testing([1, 1, 1, 1, 1]),
            [1]
        )


