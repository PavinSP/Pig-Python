from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        players = int(request.form['players'])
        session['players'] = players
        session['max_score'] = 50
        session['player_scores'] = [0] * players
        session['current_player'] = 0
        return redirect('/play')
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    player_scores = session['player_scores']
    current_player = session['current_player']
    if request.method == 'POST':
        if 'roll' in request.form:
            roll_value = roll()
            if roll_value == 1:
                session['current_score'] = 0
                return render_template('play.html', roll=roll_value, bust=True, player=current_player + 1, score=player_scores[current_player])
            else:
                session['current_score'] += roll_value
                return render_template('play.html', roll=roll_value, bust=False, player=current_player + 1, score=player_scores[current_player] + session['current_score'])
        elif 'hold' in request.form:
            player_scores[current_player] += session['current_score']
            session['player_scores'] = player_scores
            session['current_score'] = 0
            if max(player_scores) >= session['max_score']:
                winner = player_scores.index(max(player_scores)) + 1
                return redirect(f'/winner/{winner}')
            session['current_player'] = (current_player + 1) % session['players']
            return redirect('/play')
    session['current_score'] = 0
    return render_template('play.html', player=current_player + 1, score=player_scores[current_player])

@app.route('/winner/<int:winner>')
def winner(winner):
    player_scores = session['player_scores']
    return render_template('winner.html', winner=winner, score=max(player_scores))

if __name__ == '__main__':
    app.run(debug=True)
