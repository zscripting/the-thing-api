import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Discord API is working!"

@app.route("/interactions", methods=["POST"])
def interactions():
    data = request.get_json()

    # Discord's endpoint verification
    if data.get("type") == 1:
        return jsonify({"type": 1})

    # Respond to an interaction
    return jsonify({
        "type": 4,
        "data": {
            "content": "Hello from my Discord bot!"
        }
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
