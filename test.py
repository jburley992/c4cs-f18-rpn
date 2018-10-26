import unittest
import main

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = main.calculate('1 1 +')
        self.assertEqual(2,result)

    def test_sub(self):
        result = main.calculate('4 3 -')
        self.assertEqual(1,result)
    def test_toomany(self):
        with self.assertRaises(ValueError)
            result = main.calculate('3 4 3 +')
