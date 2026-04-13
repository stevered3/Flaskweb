from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "secretykey"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_games():
    if 'games' not in session:
        session['games'] = []
    return session['games']

fav_games = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/games")
def games():
    return render_template('games.html', games=get_games())

@app.route("/add_game", methods=["POST"])
def add_game():
    if request.method == "POST":
        name = request.form["title"]
        ingredients = request.form["genre"]
        instructions = request.form["description"]