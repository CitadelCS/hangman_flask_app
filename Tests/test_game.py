import unittest
from game_logic import HangmanGame, load_word_list, new_game

class TestHangmanGame(unittest.TestCase):

    def setUp(self):
        self.word_list = ['hello', 'world', 'python']

    def test_guess_letter_correct_guess(self):
        game = HangmanGame(self.word_list)
        game.chosen_word = 'hello'
        game.display = ['_', '_', '_', '_', '_']
        game.guess_letter('o')
        self.assertEqual(game.lives, 6)
        self.assertEqual(game.game_over, False)
        self.assertEqual(game.message, '')

    def test_guess_letter_wrong_guess(self):
        game = HangmanGame(self.word_list)
        game.chosen_word = 'hello'
        game.display = ['_', '_', '_', '_', '_']
        game.guess_letter('z')
        self.assertEqual(game.display, ['_', '_', '_', '_', '_'])
        self.assertEqual(game.lives, 5)
        self.assertEqual(game.game_over, False)
        self.assertEqual(game.message, 'Wrong guess. You have 5 lives left.')

    def test_game_over(self):
        game = HangmanGame(self.word_list)
        game.chosen_word = 'hello'
        game.display = ['h', 'e', 'l', 'l', 'o']
        game.guess_letter('h')
        self.assertEqual(game.game_over, True)
        self.assertEqual(game.message, "Congratulations, you've won!")

    def test_load_word_list(self):
        word_list = load_word_list('names.txt')
        self.assertIsInstance(word_list, list)
        self.assertTrue(all(isinstance(word, str) for word in word_list))

    def test_new_game(self):
        game_state = new_game(self.word_list)
        self.assertIsInstance(game_state, dict)
        self.assertIn('chosen_word', game_state)
        self.assertIn('display', game_state)
        self.assertIn('lives', game_state)
        self.assertIn('guesses', game_state)
        self.assertIn('game_over', game_state)
        self.assertIn('message', game_state)

if __name__ == '__main__':
    unittest.main()
