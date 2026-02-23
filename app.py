from flask import Flask, render_template
from class_generator import generate_class       # change from XX to what the class generator file is

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