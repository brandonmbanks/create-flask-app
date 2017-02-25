import unittest
from app import app
import os

class SampleTest(unittest.TestCase):

    def test_two_plus_two_equals_4(self):
        result = 2 + 2
        self.assertEqual(4, result)

    def test_it_should_get_env_variables(self):
        result = os.getenv('APP_ENV')
        self.assertEqual('local', result)
