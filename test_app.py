import unittest
from app import app
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    # Existing tests...
    def test_dummy1(self):
        response = self.app.get('/dummy1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Dummy 1'})
    # New tests for dummy endpoints
    def test_dummy4(self):
        response = self.app.get('/dummy4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Dummy 4'})
    def test_dummy5(self):
        response = self.app.get('/dummy5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Dummy 5'})
    def test_dummy6(self):
        response = self.app.get('/dummy6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Dummy 6'})

if __name__ == '__main__':
    unittest.main()
