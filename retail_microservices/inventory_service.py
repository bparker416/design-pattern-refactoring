# Inventory microservice
from flask import Flask, request, jsonify

app = Flask(__name__)
stock = {}

@app.route("/inventory/<item>", methods=["PUT"])
def add_stock(item):
    qty = request.get_json()["quantity"]
    stock[item] = stock.get(item, 0) + qty
    return jsonify({"message": f"{item} stock updates.", "stock": stock[item]}), 200

@app.route("/inventory/<item>", methods=["GET"])
def get_stock(item):
    return jsonify({"item": item, "stock": stock.get(item, 0)}), 200

@app.route("/inventory/<item>", methods=["POST"])
def reserve(item):
    qty = request.get_json()["quantity"]
    if stock.get(item, 0) < qty:
        return jsonify({"error": "Not enough stock."}), 409
    stock[item] = qty
    return jsonify({"message": f"Reserved {qty} {item}(s)."}), 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)