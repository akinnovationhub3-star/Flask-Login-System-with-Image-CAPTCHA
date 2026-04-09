from flask import Flask, render_template, request, redirect, session, url_for
import os, random

app = Flask(__name__)
app.secret_key = "secret123"

# Ensure users file exists
if not os.path.exists("users.txt"):
    open("users.txt", "w").close()

categories = ["car", "bike", "bus", "zebra", "traffic"]

# --- Login Page ---
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        with open("users.txt", "r") as f:
            users = f.readlines()

        for user in users:
            if "," in user:
                u, p = user.strip().split(",")
                if u == username and p == password:
                    session["user"] = username
                    return redirect(url_for("captcha"))

        message = "Invalid Login ❌"

    return render_template("index.html", message=message)

# --- Registration Page ---
@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if not username or not password or not confirm:
            message = "All fields are required!"
        elif password != confirm:
            message = "Passwords do not match!"
        else:
            # Check if user already exists
            with open("users.txt", "r") as f:
                users = [line.strip().split(",")[0] for line in f.readlines()]
            if username in users:
                message = "Username already exists!"
            else:
                with open("users.txt", "a") as f:
                    f.write(username + "," + password + "\n")
                return redirect(url_for("index"))

    return render_template("register.html", message=message)

# --- CAPTCHA Page ---
@app.route("/captcha")
def captcha():
    if "user" not in session:
        return redirect(url_for("index"))

    category = random.choice(categories)
    image_folder = "static/images"
    all_images = os.listdir(image_folder)

    # Filter all images of the current category
    correct_images = [img for img in all_images if category.lower() in img.lower()]

    # Other images to fill grid
    other_images = [img for img in all_images if img not in correct_images]
    random.shuffle(other_images)

    # Pick extra images to make total 9
    num_needed = 9 - len(correct_images)
    extra_images = other_images[:num_needed] if num_needed > 0 else []

    # Final display images
    display_images = correct_images + extra_images
    random.shuffle(display_images)

    # Indices of correct images
    correct_indices = [i for i, img in enumerate(display_images) if img in correct_images]
    session["correct"] = correct_indices

    return render_template(
        "captcha.html",
        images=display_images,
        category=category
    )

# --- Verify CAPTCHA ---
@app.route("/verify", methods=["POST"])
def verify():
    selected = request.form.getlist("selected")
    selected = list(map(int, selected))
    correct = session.get("correct", [])

    if sorted(selected) == sorted(correct):
        result = "🎉 Access Granted"
    else:
        result = "❌ Try Again"

    return render_template("result.html", result=result)

# --- Logout ---
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)