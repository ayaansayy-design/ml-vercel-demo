import json
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
def handler(request):
    x = request.get("query", {}).get("x")

    if x is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Please provide x"})
        }

    prediction = model.predict([[float(x)]])[0]

    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": float(prediction)})
    }
