from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://root:example@mongo:27017/')
db = client["employee_db"]
col = db["employees"]

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
        db_list = []
        cursor = col.find({}, {'_id': 0})
        for i in cursor:
                db_list.append(i)
        return jsonify(db_list)
    
    if request.method == 'POST':
        req_data = request.get_json()
        col.insert_one(req_data).inserted_id
        return('', 204)

@app.route('/api/v1/employees/<int:employee_id>', methods=['GET','DELETE', 'PUT'])
def manage_employee(employee_id):
    if request.method == 'GET':
        db_list = []
        cursor = col.find({}, {'_id': 0})
        for i in cursor:
            db_list.append(i)
        return jsonify(db_list['id'][f'{employee_id}'])

    if request.method == 'DELETE':
        col.delete_one(
            {
                "id" : employee_id
            }
        )
        return jsonify()
    
    if request.method == 'PUT':
        col.update_one({
            "id" : employee_id,
            'firstName': request.json['firstName'],
            'lastName': request.json['lastName'],
            'emailId': request.json['emailId']
        })

if __name__ == '__main__':
    app.run(debug=True, port=8080)