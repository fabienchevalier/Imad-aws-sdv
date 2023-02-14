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
def get_employe():
    if request.method == 'GET':
        



if __name__ == '__main__':
    app.run(debug=True)