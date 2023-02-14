from flask import Flask, request, jsonify

app = Flask(__name__)

employes = [
    {
        'id': 1,
        'firstName': 'Pierre',
        'lastName': 'Da costa',
        'emailId': 'pierre@gmail.com'
    },

    {
    'id': 2,
    'firstName': 'Marie',
    'lastName': 'Leblanc',
    'emailId': 'marie@gmail.com'
    },

    {
    'id': 3,
    'firstName': 'Alexandre',
    'lastName': 'Dubois',
    'emailId': 'alexandre@gmail.com'
    },

    {
    'id': 4,
    'firstName': 'Sophie',
    'lastName': 'Lamoureux',
    'emailId': 'sophie@gmail.com'
    },

    {
    'id': 5,
    'firstName': 'Jean',
    'lastName': 'Gagnon',
    'emailId': 'jean@gmail.com'
    }
]

@app.route('/api/v1/employees', methods=['GET'])
def manage_products():
    if request.method == 'GET':
        return jsonify({'products': products})

    if request.method == 'POST':
        product = {
            'id': products[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json['description'],
            'price': request.json['price'],
            'image': request.json['image']
        }
        products.append(product)
        return jsonify({'product': product}), 201

@app.route('/product/<int:product_id>', methods=['GET', 'DELETE'])
def manage_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'error': 'Product not found here'})

    if request.method == 'GET':
        return jsonify({'product': product[0]})

    if request.method == 'DELETE':
        products.remove(product[0])
        return jsonify({'result': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)