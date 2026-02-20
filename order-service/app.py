from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    order = {
        "id": len(orders) + 1,
        "product": data.get("product"),
        "quantity": data.get("quantity"),
    }
    orders.append(order)
    return jsonify(order), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)