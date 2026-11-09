from flask import Flask

app = Flask(__name__)

@app.route("/movie", methods=["GET"])
def show_movies():
    pass

