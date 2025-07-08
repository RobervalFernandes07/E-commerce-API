from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelagem de exemplo para um produto
#Produto (id,name,description,price)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(
            name=data['name'],
            price=data['price'],
            description=data.get("description",""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201
    return jsonify({
        "error": "Invalid data. Please provide name, price, and description."
    }), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"error": "Product not found"}), 404

# Define uma rota raiz (página inicial) e a função que será executada ao requisitar.
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
