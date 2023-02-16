from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://root:example@mongo:27017/')
db = client["employee_db"]
col = db["employees"]

@app.route('/api/v1/employees', methods=['GET'])
def get_employee():
    return jsonify([i for i in col.find({}, {"_id":0})]), 200

@app.route('/api/v1/employees', methods=['POST'])
def post_employee():
    data = request.get_json()
    data["id"] = len([i for i in col.find({}, {"_id":0})]) + 1
    col.insert_one(data)
    return jsonify(data), 200

@app.route("/api/v1/employees/<int:id>", methods=['GET'])
def get_employee_id(id):
    return [element for element in [i for i in col.find({}, {"_id":0})] if element["id"] == id][0]

@app.route("/api/v1/employees/<int:id>", methods=['PUT'])
def put_employee_id(id):
    result = col.update_one({"id": int(id)}, {"$set": request.get_json()})
    return jsonify({"result": "Employee updated"}) if result.modified_count == 1 else jsonify({"error": "Employee not found"}) 

@app.route("/api/v1/employees/<int:id>", methods=['DELETE'])
def del_employee_id(id):
    result = col.delete_one({'id': int(id)})
    return jsonify({'result': 'Employee deleted'}) if result.deleted_count == 1 else jsonify({'error': 'Employee not found'})
    
if __name__ == '__main__':
    app.run(debug=True)