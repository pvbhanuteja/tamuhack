from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "ping pong"

@app.route("/predict")
def predict():
    

