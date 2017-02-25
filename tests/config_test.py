import unittest
from app import app
import os


class ConfigTest(unittest.TestCase):

    def test_it_should_correctly_set_app_config(self):
        result = os.environ['APP_SETTINGS']
        self.assertEqual('config.LocalConfig', result)
        self.assertTrue(app.config['FLASK_DEBUG'])
