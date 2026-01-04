import pickle
import json

with open("../model.pkl", "rb") as f:
    model = pickle.load(f)

def handler(request):
    try:
        x = request.get("query", {}).get("x")

        if x is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Please provide x"})
            }

        prediction = model.predict([[float(x)]])[0]

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": prediction})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
