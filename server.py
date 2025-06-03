from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    characters = ["Ed", "Al", "Winry", "Riza", "Roy"]
    return render_template("index.html", names=characters)


if __name__ == '__main__':
    app.run()
