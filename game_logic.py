import random
import json

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.chosen_word = random.choice(self.word_list)
        self.lives = 6
        self.display = ["_" for _ in self.chosen_word]
        self.game_over = False
        self.message = ""
        self.stages = ['''
                      +---+
                      |   |
                      O   |
                     /|\  |
                     / \  |
                          |
                    =========
                    Sorry, GAME OVER...
                    ''', '''
                      +---+
                      |   |
                      O   |
                     /|\  |
                     /    |
                          |
                    =========
                    Uh oh, there the right leg, you're down to one more try!
                    ''', '''
                      +---+
                      |   |
                      O   |
                     /|\  |
                          |
                          |
                    =========
                    Here comes the left arm!
                    ''', '''
                      +---+
                      |   |
                      O   |
                     /|   |
                          |
                          |
                    =========
                    I see a right arm!
                    ''', '''
                      +---+
                      |   |
                      O   |
                      |   |
                          |
                          |
                    =========
                    Here comes the Mid-Section!
                    ''', '''
                      +---+
                      |   |
                      O   |
                          |
                          |
                          |
                    =========
                    Oh man! There goes the Head!
                    ''', '''
                      +---+
                      |   |
                          |
                          |
                          |
                          |
                    =========
                    Uh Oh, there goes the platform!
                    ''']

    def guess_letter(self, guess):
        if guess in self.chosen_word:
            for index, letter in enumerate(self.chosen_word):
                if letter == guess:
                    self.display[index] = guess
            if "_" not in self.display:
                self.game_over = True
                self.message = "Congratulations, you've won!"
        else:
            self.lives -= 1
            if self.lives == 0:
                self.game_over = True
                self.message = "Game over. The word was '{}'.".format(self.chosen_word)
            else:
                self.message = "Wrong guess. You have {} lives left.".format(self.lives)

        return ''.join(self.display), self.lives, self.message, self.game_over




    def to_json(self):
        # Serialize game state into a JSON-serializable dictionary
        return {
            'chosen_word': self.chosen_word,
            'lives': self.lives,
            'display': self.display,
            'game_over': self.game_over,
            'message': self.message,
            'stages': self.stages
        }

    @classmethod
    def from_json(cls, data):
        # Deserialize JSON data into a HangmanGame object
        game = cls([])
        game.chosen_word = data['chosen_word']
        game.lives = data['lives']
        game.display = data['display']
        game.game_over = data['game_over']
        game.message = data['message']
        game.stages = data['stages']  # Deserialize the stages attribute
        return game


def load_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = [line.strip() for line in file]
    return word_list

def new_game(word_list):
    chosen_word = random.choice(word_list)
    display = ['_' for _ in chosen_word]

    game_state = {
        'chosen_word': chosen_word,
        'display': display,
        'lives': 6,
        'guesses': [],
        'game_over': False,
        'message': 'Guess a letter!'
    }
    return game_state

# Example usage in your Flask app
# word_list = load_word_list('path/to/your/wordlist.txt')
# game = HangmanGame(word_list)
