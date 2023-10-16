from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Store login credentials in memory (for demonstration purposes)
credentials = {
    "user1": "password1",
    "user2": "password2",
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        # Check if the user is authenticated
        if user not in credentials or credentials[user] != password:
            return jsonify({"error": "Authentication failed"})
        else:
            return render_template("index.html")

    return render_template("login.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data["user"]
    user_message = data["user_message"]

    # Check if the user is authenticated
    if user not in credentials or credentials[user] != data["password"]:
        return jsonify({"error": "Authentication failed"})

    # Simulate a response from the bot (You can replace this with an AI-generated response)
    bot_message = f"Bot: You said: {user_message}"

    return jsonify({"bot_message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
