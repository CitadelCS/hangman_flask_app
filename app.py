# from flask import Flask, render_template, request, session, redirect, url_for
# from game_logic import HangmanGame, load_word_list
#
# app = Flask(__name__)
# app.secret_key = 'hellospam'
#
# @app.route('/')
# def index():
#     if 'game_over' in session:
#         session.clear()
#
#     # Clear the session data only if the user is accessing the home page for a new game
#     if 'game_state' not in session:
#         session.clear()
#
#         word_list = load_word_list('names.txt')
#         game = HangmanGame(word_list)
#         # Serialize the parts of the game state that need to be stored
#         session['game_state'] = {
#             'chosen_word': game.chosen_word,
#             'display': game.display,
#             'lives': game.lives,
#             'game_over': game.game_over,
#             'message': game.message
#         }
#
#     # Pass the necessary parts of 'game_state' to your template
#     return render_template('index.html', game_state=session['game_state'])
#
#
#
# @app.route('/guess', methods=['POST'])
# def guess():
#     # Deserialize the game state from the session
#     game_info = session['game_state']
#     word_list = load_word_list('names.txt')  # Re-load word list to pass to the game
#     game = HangmanGame(word_list)
#     game.chosen_word = game_info['chosen_word']
#     game.display = game_info['display']
#     game.lives = game_info['lives']
#     game.game_over = game_info['game_over']
#     game.message = game_info['message']
#
#     guess = request.form['guess']
#     # Update the game state with the guess
#     game.guess_letter(guess)
#
#
#     # Check for game over condition
#     if game.game_over:
#         print("Game over. Message:", game.message)
#         # Clear the session data
#         session.pop('game_state', None)
#         return render_template('game_over.html', game_state=game.to_json())
#
#     # Serialize updated game state for session storage
#     session['game_state'] = game.to_json()
#
#     if game.lives > 0:
#         return redirect(url_for('index'))  # Use redirect to refresh the index page with updated state
#
# @app.route('/new_game', methods=['POST'])
# def new_game():
#     word_list = load_word_list('names.txt')
#     game = HangmanGame(word_list)
#     # Serialize the parts of the game state that need to be stored
#     session['game_state'] = {
#         'chosen_word': game.chosen_word,
#         'display': game.display,
#         'lives': game.lives,
#         'game_over': game.game_over,
#         'message': game.message
#     }
#     return redirect(url_for('index'))
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, session, redirect, url_for
from game_logic import HangmanGame, load_word_list

app = Flask(__name__)
app.secret_key = 'hellospam'

@app.route('/')
def index():
    # Only clear the session if it's a new game, not if the game is simply over
    if 'game_state' not in session:
        session.clear()
        word_list = load_word_list('names.txt')
        game = HangmanGame(word_list)
        session['game_state'] = game.to_json()  # Serialize the game state

    return render_template('index.html', game_state=session['game_state'])

@app.route('/guess', methods=['POST'])  # Corrected indentation
def guess():
    # Deserialize the game state from the session
    game_info = session['game_state']
    game = HangmanGame.from_json(game_info)

    guess = request.form['guess']
    game.guess_letter(guess)

    # Serialize updated game state for session storage
    session['game_state'] = game.to_json()

    # After the guess has been processed, check if the user has won or lost
    if game.game_over:
        if "Congratulations" in game.message:  # Slightly more flexible check
            # Render a winner template if the user won
            return render_template('game_winner.html', game_state=session['game_state'])
        else:
            # Render a game over template if the user lost
            return render_template('game_over.html', game_state=session['game_state'])

    # If the game is not over, redirect back to the index page
    return redirect(url_for('index'))

@app.route('/new_game', methods=['POST'])
def new_game():
    # Reset the session for a new game
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
