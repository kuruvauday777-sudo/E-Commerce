from flask import Flask, render_template_string
import requests

app = Flask(__name__)

PRODUCT_URL = "http://product-service:5001/products"

@app.route("/")
def home():
    response = requests.get(PRODUCT_URL)
    products = response.json()

    html = """
    <h1>Product Catalog</h1>
    <ul>
    {% for p in products %}
      <li>{{p.name}} - ${{p.price}}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)