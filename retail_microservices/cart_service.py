# Cart microservice
from flask import Flask, request, jsonify

app = Flask(__name__)
cart = []

@app.route("/cart", methods=["POST"])
def add_item():
    body = request.get_json()
    cart.append((body["item"], body["quantity"]))
    return jsonify({"message": f"Added {body['quantity']} {body['item']}."}), 201

@app.route("/cart", methods=["GET"])
def view_cart():
    return jsonify({"cart": cart})

if __name__ == '__main__':
    app.run(port=5001, debug=True)