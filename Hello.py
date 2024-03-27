from flask import Flask

app = Flask(__name__)

@app.route("/")
def sample_text():
    return "<p>Sample Text for the Website</p>"