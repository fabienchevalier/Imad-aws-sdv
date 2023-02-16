import unittest
import requests
import json

class TestEmployeeAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:8080/api/v1/employees'
        self.headers = {'Content-Type': 'application/json'}
        self.employee = {
            'firstName': 'John',
            'lastName': 'Doe',
            'emailId': 'john',
            }

    def test_get_all_employees(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_post_employee(self):
        response = requests.post(self.base_url, headers=self.headers, data=json.dumps(self.employee))
        self.assertEqual(response.status_code, 200)

    def test_get_employee_by_id(self):
        response = requests.get(f'{self.base_url}/1')
        self.assertEqual(response.status_code, 200)

    def test_put_employee_by_id(self):
        response = requests.put(f'{self.base_url}/1', headers=self.headers, data=json.dumps(self.employee))
        self.assertEqual(response.status_code, 200)

    def test_delete_employee_by_id(self):
        response = requests.delete(f'{self.base_url}/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
