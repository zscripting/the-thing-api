from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My API is working."

@app.route("/api/hello")
def hello():
    return {"message": "Hello from my API!"}
