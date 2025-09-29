from flask import Flask

# create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is me VIDUMUKHI ! This is my simple Python app running in Flask."

@app.route("/about")
def about():
    return "This is the about page of my simple app."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

