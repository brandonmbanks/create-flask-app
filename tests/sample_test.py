import unittest
from app import app

class SampleTest(unittest.TestCase):

    def test_two_plus_two_equals_4(self):
        result = 2 + 2
        self.assertEqual(4, result)
