import unittest
import main

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = main.calculate('1 1 +')
        self.assertEqual(2,result)