from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
mongo_client = MongoClient()

employees = [
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

@app.route('/api/v1/employees', methods=['GET', 'POST'])
def list_employee():
    if request.method == 'GET':
        return jsonify(employees)
    
    if request.method == 'POST':
        new_employee = {
            'id': employees[-1]['id'] + 1,
            'firstName': request.json['firstName'],
            'lastName': request.json['lastName'],
            'emailId': request.json['emailId']
        }
        employees.append(new_employee)
        return jsonify({'employees': new_employee}), 201

@app.route('/api/v1/employees/<int:employee_id>', methods=['GET','DELETE', 'PUT'])
def manage_employee(employee_id):
    employee = [employee for employee in employees if employee['id'] == employee_id]
    if request.method == 'DELETE':
        employees.remove(employee[0])
        return jsonify({'result': f'{employee[0]} deleted'})
    
    if request.method == 'GET':
        return jsonify(employee[0])
    
    if request.method == 'PUT':
        put_employees = {
            'id': employees[-1]['id'] + 1,
            'firstName': request.json['firstName'],
            'lastName': request.json['lastName'],
            'emailId': request.json['emailId']
        }
        employees[employee_id]=(put_employees)
        return jsonify({'result': f'{employee[0]} updated'})

    
if __name__ == '__main__':
    app.run(debug=True, port=8080)