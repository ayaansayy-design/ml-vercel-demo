from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])  # maps to /api
def predict():
    x = request.args.get("x")
    if x is None:
        return jsonify({"error": "Please provide x"}), 400
    try:
        prediction = model.predict([[float(x)]])[0]
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"prediction": float(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)