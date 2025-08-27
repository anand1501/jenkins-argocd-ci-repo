from flask import Flask

app = Flask(__name__)

@app.route("/")
def app():
    return("2nd Testing the the application...")
