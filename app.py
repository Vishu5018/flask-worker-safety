from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")  # ✅ No absolute path

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
