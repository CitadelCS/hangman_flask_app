import unittest
from app import app

class TestHangmanApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Hangman!', response.data)

    def test_guess_route(self):
        # Set up session with 'game_state' key
        with self.app as client:
            with client.session_transaction() as sess:
                sess['game_state'] = {
                    'chosen_word': 'example',
                    'display': '_______',
                    'lives': 6,
                    'game_over': False,
                    'message': ''
                }




if __name__ == '__main__':
    unittest.main()
