from flask import Flask, render_template
from BO4RCGHOMESTRETCH import generate_class

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", class_data=None)

@app.route("/generate")
def generate():
    class_data = generate_class()
    return render_template("index.html", class_data=class_data)

if __name__ == "__main__":
    app.run(debug=True)