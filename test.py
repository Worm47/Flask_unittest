import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_positive(self):
        response_positive = self.app.post('/convert', data=dict(
            from_currency='usd',
            to_currency='rub',
            amount=100
        ))
        self.assertIn(b'9163.0', response_positive.data)

    def test_zero(self):
        response_zero = self.app.post('/convert', data=dict(
            from_currency='usd',
            to_currency='jpy',
            amount=0
        ))
        self.assertIn(b'0.0', response_zero.data)

    def test_negative(self):
        response_negative = self.app.post('/convert', data=dict(
            from_currency='usd',
            to_currency='usd',
            amount=-100
        ))
        self.assertIn(b'100', response_negative.data)

if __name__ == '__main__':
    unittest.main()

