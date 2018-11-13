import unittest
import json
from app.api.tests.test_baselogin import BaseTest

login_dummy_data= {
    "email": "Alvin@gmail.com",
    "password":"1234"
}

class TestUser(BaseTest):
	"""docstring for TestUser"""
	def test_user_login(self):
		respo= self.client.post('/api/v1/users/login',data = json.dumps(login_dummy_data), content_type='application/json')
		self.assertEqual(respo.status_code,200)


if __name__ == "__main__":
	unittest.main()