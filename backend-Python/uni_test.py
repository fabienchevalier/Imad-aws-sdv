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
        id_post = response['id']
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
    
    def test_update_employee(self):
        updated_employee = {
            "firstName": "up_TEST",
            "lastName": "up_SUBJECT"
        }
        employee_id = 1
        response = requests.put(f"{self.base_url}/employees/{employee_id}", json=updated_employee)
        self.assertEqual(response.status_code, 204)
    
    def test_delete_employee(self):
        employee_id = 1
        response = requests.delete(f"{self.base_url}/employees/{employee_id}")
        self.assertEqual(response.status_code, 204)
