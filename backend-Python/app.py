from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://root:example@mongo:27017/')
db = client["employee_db"]
col = db["employees"]

@app.route('/api/v1/employees', methods=['GET', 'POST'])
def employee():
    liste=[]
    cursor = col.find({}, {'_id': 0})
    liste = [i for i in cursor]
    if request.method == 'GET':
        return jsonify(liste), 200

    if request.method == 'POST':   
        data = request.get_json()
        try:
            data['id'] = liste[-1]['id'] + 1
        except:
            data['id'] = 1
        col.insert_one(data).inserted_id
        return jsonify(data), 200

@app.route('/api/v1/employees/<int:employee_id>', methods=['GET','DELETE', 'PUT'])
def manage_employee(employee_id):
    if request.method == 'GET':
        cursor = col.find({}, {'_id': 0})
        for i in cursor:
            if i['id'] == employee_id:
                return jsonify(i)

    if request.method == 'DELETE':
        cursor = col.find({}, {'_id': 0})
        for i in cursor:
            if i['id'] == employee_id:
                col.delete_one(
                    {
                        'id' : employee_id
                    }
                )
        return jsonify()
    
    if request.method == 'PUT':
        col.update_one(
            {
            'id': employee_id
            },    
            {
                "$set": 
                    {
                        "id" : employee_id,
                        'firstName': request.json['firstName'],
                        'lastName': request.json['lastName'],
                        'emailId': request.json['emailId']
                    }
            }
        )
        return jsonify()
        
if __name__ == '__main__':
    app.run(debug=True)