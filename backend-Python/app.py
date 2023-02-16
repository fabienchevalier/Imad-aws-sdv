from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

class EmployeeAPI:
    def __init__(self, db_uri):
        self.app = Flask(__name__)
        CORS(self.app)
        self.client = MongoClient(db_uri)
        self.db = self.client["employee_db"]
        self.col = self.db["employees"]
        self.routes()

    def routes(self):
        """
        Ajoute les routes à l'application Flask
        """
        self.app.route('/api/v1/employees', methods=['GET'])(self.get_employees)
        self.app.route('/api/v1/employees', methods=['POST'])(self.add_employee)
        self.app.route("/api/v1/employees/<int:id>", methods=['GET'])(self.get_employee)
        self.app.route("/api/v1/employees/<int:id>", methods=['PUT'])(self.update_employee)
        self.app.route("/api/v1/employees/<int:id>", methods=['DELETE'])(self.delete_employee)

    def get_employees(self):
        """
        Renvoie la liste de tous les employés de la base de données.
        """
        employees = [employee for employee in self.col.find({}, {"_id": 0})]
        if not employees:
            return jsonify({"error": "No employee found"}), 404
        return jsonify(employees), 200

    def add_employee(self):
        """
        Ajoute un nouvel employé à la base de données.
        """
        data = request.get_json()
        data["id"] = len([i for i in self.col.find({}, {"_id":0})]) + 1
        result = self.col.insert_one(data)
        if not result.acknowledged:
            return jsonify({"error": "Failed to add employee"}), 500
        return jsonify(), 200

    def get_employee(self, id):
        """
        Renvoie l'employé ayant l'ID spécifié.
        """
        employee = self.col.find_one({"id": id}, {"_id": 0})
        if not employee:
            return jsonify({"error": "Employee not found"}), 404
        return jsonify(employee), 200

    def update_employee(self, id):
        """
        Met à jour les données de l'employé ayant l'ID spécifié.
        """
        result = self.col.update_one({"id": id}, {"$set": request.get_json()})
        if result.modified_count == 0:
            return jsonify({"error": "Failed to update employee"}), 500
        return jsonify({"result": "Employee updated"}), 200

    def delete_employee(self, id):
        """
        Supprime l'employé ayant l'ID spécifié.
        """
        result = self.col.delete_one({"id": id})
        if result.deleted_count == 0:
            return jsonify({"error": "Failed to delete employee"}), 500
        return jsonify