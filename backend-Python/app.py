from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://root:example@mongo:27017/')
db = client["employee_db"]
col = db["employees"]


db_dict = []

# employees = [
#     {
#         'id': 1,
#         'firstName': 'Pierre',
#         'lastName': 'Da costa',
#         'emailId': 'pierre@gmail.com'
#     }
# ]

@app.route('/api/v1/employees', methods=['GET', 'POST'])
def list_employee():
    if request.method == 'GET':
        cursor = col.find({}, {'_id': 0})
        for i in cursor:
                db_dict.append(i)
        return jsonify(db_dict)
    
    if request.method == 'POST':
        req_data = request.get_json()
        col.insert_one(req_data).inserted_id
        return('', 204)

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