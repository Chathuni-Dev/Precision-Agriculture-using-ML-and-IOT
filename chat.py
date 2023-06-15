from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Dictionary of predefined responses
responses = {
    "hi": ["Hello!", "Hi!", "Hey there!"],
    "how are you": ["I'm good, thanks!", "I'm fine, how about you?", "I'm doing great!"],
    "bye": ["Goodbye!", "Farewell!", "Take care!"],
    "default": ["Sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning. Can you ask something else?"]
}

# Function to generate a response
def get_response(message):
    message = message.lower()

    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

@app.route("/")
def index():
    return render_template("template/signup.html")

@app.route("/get_response", methods=["POST"])
def get_chat_response():
    user_message = request.form["usermsg"]
    response = get_response(user_message)
    return jsonify(response)

if __name__ == "__main__":
    app.run()
