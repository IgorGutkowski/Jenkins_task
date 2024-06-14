import unittest
from calculator import multiply

class TestMultiply(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
