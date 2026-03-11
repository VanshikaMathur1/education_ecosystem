from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/student")
def student():
    return "Student Login Page"


@app.route("/teacher")
def teacher():
    return "Teacher Login Page"


@app.route("/parent")
def parent():
    return "Parent Login Page"


if __name__ == "__main__":
    app.run(debug=True)