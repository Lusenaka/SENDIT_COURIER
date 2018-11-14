import unittest
import sys  # fix import errors
from app import create_app
import os
from app.api.v1.models import ParcelOrder, Users

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

parcels = ParcelOrder()
user = Users()


class BaseTest(unittest.TestCase):
    """docstring for BaseTest"""

    def setUp(self):
        """Method called to prepare the test fixture"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.parcel_dummy_data = {
            "order_id": 56,
            "current_location": "Nairobi",
            "receiver_name": "Anne",
            "receivers_location": "Mombasa",
            "pickup_location": "Tuskeys",
            "weight": 23,
            "price": 3456,
            "status": "pending"
        }

        self.signup_dummy_data = {
            "user_id": 23,
            "username": "Alvin",
            "email": "Alvin@gmail.com",
            "default_location": "Kiambu",
            "password": 1234
        }
        self.login_dummy_data = {
            "email": "Alvin@gmail.com",
            "password": 1234
        },
        {
            "email" : "jane.doe@gmail.com",
            "password" : "1234"
        }

    def tearDown(self):
        """A class method called before tests in an individual class run."""
        parcels.db.clear()
    def tearDown(self):
        user.udb.clear()
