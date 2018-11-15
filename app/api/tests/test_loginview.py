import unittest
import json
from app.api.tests.test_base import BaseTest


class TestUser(BaseTest):
	"""docstring for TestUser"""
	def test_user_login(self):
		response = self.client.post('/api/v1/users/login',data = json.dumps(self.login_dummy_data),content_type='application/json')
		self.assertEqual(response.status_code,201)


if __name__ == "__main__":
	unittest.main()
	