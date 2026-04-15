from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "secretykey"

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_games():
    if 'games' not in session:
        session['games'] = []
    return session['games']


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/games")
def games():
    return render_template('games.html', games=get_games())

@app.route("/add", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        title = request.form["title"]
        genre = request.form["genre"]
        description = request.form["description"]

        file = request.files['image']
        if not title or not genre or not description:
            return "Missing fields"
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            games = get_games()
            games.append({
                'title': title,
                'genre': genre,
                'description': description,
                'image': filename
            })
            session['games'] = games

            return redirect(url_for('games'))
        else:
            return "Invalid file type"

    return render_template('add_game.html')

@app.route('/delete/<int:index>')
def delete_game(index):
    games = get_games()
    if 0 <= index < len(games):
        games.pop(index)
        session['games'] = games
    return redirect(url_for('games'))

if __name__ == '__main__':
    app.run(debug=True)