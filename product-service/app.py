from flask import Flask, jsonify, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Phone", "price": 500},
]

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)