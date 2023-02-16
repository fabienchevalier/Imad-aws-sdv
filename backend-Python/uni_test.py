import unittest
import requests

class TestEmployeeAPI(unittest.TestCase):
    
    base_url = "http://localhost:8080/api/v1"
    
    def test_get_employees(self):
        response = requests.get(f"{self.base_url}/employees")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_add_employee(self):
        new_employee = {
            "firstName": "TEST",
            "lastName": "SUBJECT",
            "emailId": "TEST@TEST.FR"
        }
        response = requests.post(f"{self.base_url}/employees", json=new_employee)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)