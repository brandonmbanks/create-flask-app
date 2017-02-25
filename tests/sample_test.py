import unittest
from app import app
import os

class SampleTest(unittest.TestCase):

    def test_two_plus_two_equals_4(self):
        result = 2 + 2
        self.assertEqual(4, result)

    def test_it_should_correctly_set_app_config(self):
        result = os.getenv('APP_SETTINGS')
        self.assertEqual('config.LocalConfig', result)
        self.assertTrue(app.config['FLASK_DEBUG'])
