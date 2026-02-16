from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------------------------
# Temporary Vote Storage (Demo)
# ---------------------------------

votes = {}

results = {
    "Conrad Fisher": 0,
    "Jeremiah": 0,
    "Isabel Conklin": 0,
    "Steven": 0,
    "Taylor": 0
}

# ---------------------------------
# Multiple Faculty Accounts
# ---------------------------------

faculty_accounts = {
    "sage456": "sage123",
    "jett678": "jett123",
    "Phoenix890": "password123",
    "Sova": "sova123"
}

# ---------------------------------
# Student Home
# ---------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------
# Vote Submission
# ---------------------------------

@app.route("/vote", methods=["POST"])
def vote():
    uid = request.form["uid"]
    candidate = request.form["candidate"]

    if uid in votes:
        return "You have already voted!"

    votes[uid] = candidate
    results[candidate] += 1

    return "Vote Successfully Cast!"

# ---------------------------------
# Faculty Login
# ---------------------------------

@app.route("/faculty", methods=["GET", "POST"])
def faculty():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if username exists AND password matches
        if username in faculty_accounts and faculty_accounts[username] == password:
            return render_template(
                "dashboard.html",
                results=results,
                votes=votes,
                faculty=username
            )
        else:
            return "Invalid Credentials"

    return render_template("faculty_login.html")


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

