from flask_testing import TestCase
import unittest
from main import app
from flask import current_app, url_for

class Maintest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config['DEBUG'] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        self.assertIsNotNone(current_app.config["TESTING"])
    
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)


if __name__ == '__main__':
    unittest.main()