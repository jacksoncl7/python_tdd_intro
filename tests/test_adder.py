import unittest
from adder import Adder

class TestAdderMethods(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Adder().sum(1, 2), 3)

    def test_sum_list(self):
        self.assertEqual(Adder().sum_list([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()
