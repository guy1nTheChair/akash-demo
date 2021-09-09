from flask import Flask

app = Flask(__name__)


@app.route("/home")
def home():
    return {
        "Working from": "Home :)"
    }, 200

@app.route("/office")
def office():
    return {
        "Working from": "office :("
    }, 200


if __name__ == "__main__":
    app.run(debug=True)