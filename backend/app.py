from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (for testing only)
users = {}

# ✅ Valid UID Ranges
valid_ranges = [
    (111723043001, 111723043050),
    (111723044001, 111723044050),
    (111723045001, 111723045050),
    (111723046001, 111723046050),
    (111723047001, 111723047050),
]


def is_valid_uid(uid):
    try:
        uid_number = int(uid)
    except:
        return False

    for start, end in valid_ranges:
        if start <= uid_number <= end:
            return True
    return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uid = request.form.get("uid")
        password = request.form.get("password")

        # ✅ Check UID format & range
        if not is_valid_uid(uid):
            return "Invalid UID. Not in allowed student range."

        # ✅ Check if already registered
        if uid in users:
            return "UID already registered."

        # Store user
        users[uid] = password

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uid = request.form.get("uid")
        password = request.form.get("password")

        if uid in users and users[uid] == password:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid UID or Password."

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# For Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
