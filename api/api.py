from flask import Flask, jsonify
import config

app = Flask(__name__)

@app.route("/")
def index():
    return "It's working!"

@app.route("/predict", methods=["POST"])
def predict():
    """
    Puts input data in the queue and waits for result
    """
    return jsonify({"payload": "Not implemented"})

if __name__=="__main__":
    app.run()
