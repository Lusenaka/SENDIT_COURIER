import unittest
import json
from app.api.tests.test_base import BaseTest


class TestUser(BaseTest):
	"""docstring for TestUser"""
	def test_create_user(self):
		response= self.client.post('/api/v1/users/signup',data = json.dumps(self.signup_dummy_data),
								content_type='application/json')
		self.assertEqual(response.status_code,201)


if __name__ == "__main__":
	unittest.main()
