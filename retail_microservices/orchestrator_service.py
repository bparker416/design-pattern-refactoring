"""
Central coordinator - talks to all three services
Acts as a simple API gateway
"""

import requests
from flask import Flask, request, jsonify

CART_URL = "http://localhost:5001/cart"
INVENTORY_URL = "http://localhost:5002/inventory"
PAYMENT_URL = "http://localhost:5003/payment"

app = Flask(__name__)

@app.route("/add_to_inventory/<item>", methods=["PUT"])
def add_to_inventory(item):
    qty = request.get_json()["quantity"]
    r = requests.put(f"{INVENTORY_URL}/{item}", json={"quantity": qty})
    return jsonify(r.json()), r.status_code

@app.route("add_to_cart", methods=["POST"])
def add_to_cart():
    body = request.get_json() # {item, quantity}
    # Reserve stock first
    res = requests.post(f"{INVENTORY_URL}/{body['item']}", json={"quantity": body["quantity"]})
    if res.status_code != 200:
        return jsonify({"error": "Revervation failed."}), 409
    # Add to cart
    cart_res = requests.post(CART_URL, json=body)
    return jsonify(cart_res.json(), cart_res.status_code)

app.route("/checkout", methods=["POST"])
def checkout():
    body = request.get_json() # {amount, method}
    pay_res = requests.post(PAYMENT_URL, json=body)
    return jsonify(pay_res.json(), pay_res.status_code)

if __name__ == "__main__":
    app.run(port=5000, debug=True)