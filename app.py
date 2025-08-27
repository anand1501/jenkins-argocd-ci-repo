from flask import Flask

app = Flask(__name__)

@app.route("/")
def lw():
    return("Testing the the application for v6...")
