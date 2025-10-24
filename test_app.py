import unittest
from app import app

class IndexPageTestCase(unittest.TestCase):
    def setUp(self):
        # Create test client
        self.client = app.test_client()
        self.client.testing = True

    def test_index_page_empty(self):
        """Test that the home page loads and shows no fundraisers."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Fundraiser App', response.data)
        self.assertIn(b'No fundraisers yet.', response.data)

    def test_index_page_with_fundraiser(self):
        """Test that a fundraiser appears on the home page."""
        # Add a fundraiser to the app's in-memory storage
        response = self.client.post('/add', data={
            'name': 'Test Fundraiser',
            'goal': '5000',
            'description': 'Test Description'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Fundraiser', response.data)
        self.assertIn(b'5000', response.data)
        self.assertIn(b'Test Description', response.data)

if __name__ == '__main__':
    unittest.main()
