from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://root:example@mongo:27017/')
db = client.employee_db
col = db.employees

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    employees = list(col.find({}, {'_id': 0}))
    return jsonify(employees), 200

@app.route('/api/v1/employees', methods=['POST'])
def post_employee():
    data = request.get_json()
    employees = list(col.find({}, {'_id': 0}))
    data['id'] = len(employees) + 1
    col.insert_one(data)
    return jsonify(), 200

@app.route("/api/v1/employees/<int:id>", methods=['GET'])
def get_employee(id):
    employee = col.find_one({'id': id}, {'_id': 0})
    if employee is not None:
        return jsonify(employee), 200
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route("/api/v1/employees/<int:id>", methods=['PUT'])
def put_employee(id):
    result = col.update_one({'id': id}, {'$set': request.get_json()})
    if result.modified_count == 1:
        return jsonify({'result': 'Employee updated'}), 200
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route("/api/v1/employees/<int:id>", methods=['DELETE'])
def delete_employee(id):
    result = col.delete_one({'id': id})
    if result.deleted_count == 1:
        return jsonify({'result': 'Employee deleted'}), 200
    else:
        return jsonify({'error': 'Employee not found'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
