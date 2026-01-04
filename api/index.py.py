from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/api", methods=["GET"])
def predict():
    x = request.args.get("x")

    if x is None:
        return jsonify({"error": "Please provide x"}), 400

    prediction = model.predict([[float(x)]])[0]

    return jsonify({"prediction": float(prediction)})
