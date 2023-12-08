from flask import Flask, render_template
from pathlib import Path
import sqlite3

base_path = Path.cwd()
db_name = "database/games.db"
file_path = base_path / db_name

#app = Flask(__name__)ss
app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/games")
def game():
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    games = cursor.execute("SELECT * FROM game").fetchall()
    conn.close()

    return render_template("gamedata.html", games = games)
if __name__=="__main__":
    app.run(debug=True)
app.run(port=5000)