# Payment microservice
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/payment", methods=['POST'])
def pay():
    body = request.get_json()
    amount = body["amount"]
    method = body["method"]
    # Dummy success
    return jsonify({"message": f"Processed {amount} via {method}."}), 200

if __name__ == "__main__":
    app.run(port=5003, debug=True)