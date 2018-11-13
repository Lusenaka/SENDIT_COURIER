import unittest
import json
import sys  # fix import errors
import os
from app.api.tests.test_base import BaseTest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestParcel(BaseTest):
	"""docstring for TestParcel"""
	def test_new_parcel(self):
		respo= self.client.post('/api/v1/parcel',data = json.dumps(self.parcel_dummy_data), content_type='application/json')
		self.assertEqual(respo.status_code,200)


	def test_single_parcel(self):
		respo= self.client.get('/api/v1/parcels')
		self.assertEqual(respo.status_code, 200)

if __name__ == "__main__":
	unittest.main()