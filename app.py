from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key = "secretykey"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

fav_games = []

@app.route("/")
def home():
    return render_template("home.html", fav_games=fav_games)

@app.route("/games")
def games_page():
    return render_template("games.html")

@app.route("/add_game", methods=["POST"])
def add_game():
    if request.method == "POST":
        name = request.form["name"]
        ingredients = request.form["year"]
        instructions = request.form["price"]