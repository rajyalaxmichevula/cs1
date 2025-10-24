from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

WORDS = {
    "easy": [
        "apple", "car", "dog", "sun", "tree", "ball", "fish", "book", "cat", "house"
    ],
    "medium": [
        "airplane", "camera", "guitar", "mountain", "rainbow", "turtle",
        "volcano", "laptop", "pizza", "robot"
    ],
    "hard": [
        "microscope", "parachute", "time machine", "helicopter", "spaceship",
        "satellite", "binoculars", "laboratory", "submarine", "telescope"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word', methods=['POST'])
def get_word():
    difficulty = request.json.get("difficulty")
    if difficulty not in WORDS:
        return jsonify({"error": "Invalid difficulty"}), 400
    word = random.choice(WORDS[difficulty])
    return jsonify({"word": word})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
