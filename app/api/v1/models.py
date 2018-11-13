from flask import make_response, jsonify, request
from flask_restful import reqparse


users = [
    {
        "user_id" : 43,
        "username" : "Alvin",
        "email": "Alvin@gmail.com",
        "default_location":"Kiambu",
        "password":"1234"
    },
    {
        "user_id" : 23,
        "username" : "Charity",
        "email": "Charity@gmail.com",
        "default_location":"Kericho",
        "password":"54321"
    }]

# User roles
customer = "Normal user"
admin = "User administrator"

class Users(object):
    """Creating model for users"""
    def __init__(self):
        self.udb = users
        self.user_id = len(self.udb)
        self.role = customer

    def create_user(self, username, email, default_location, password):
        user = {
            "user_id" :self.user_id + 1,
            "username": username,
            "email": email,
            "default_location": default_location,
            "password": password,
            "role" : self.role 
        } 

        save_user = self.udb.append(user)
        return save_user

    def filter_user_detail(self,email):
        user = [user for user in users if user['email']==email]
        return user

    def filter_password_detail(self,password):
        passw = [passw for passw in users if passw['password']==password]
        return passw

    def user_login(self, email, password):
        registered_user = Users.filter_user_detail(self, email)
        registered_user2 = Users.filter_password_detail(self, password)
        if not registered_user:
            return make_response(jsonify({
                "message" : "{} is not a registered user".format(email)
            }), 201)
        if registered_user:
            return make_response(jsonify({
                "message" : "login successful"
            }), 201)
        if not registered_user2:
            return make_response(jsonify({
                "message" : "{} is not a registered user".format(email)
            }), 400)
        elif registered_user2:
            return make_response(jsonify({
                "welcome" : "Login successful"
            }))
        for user in users:
            if user["role"] == customer:
                return {'Role' : 'You are a user'}
            elif user['role'] == admin:
                return{'Role' : 'You are an admin'}
        


parcels = [
    {
        "order_id" : 54,
        "current_location": "Nairobi",
	    "receiver_name": "Anne",
	    "receivers_location": "Mombasa",
	    "pickup_location": "Tuskeys",
	    "weight": 23,
	    "price": 3456,
	    "status": "pending"
    },
    {
        "order_id" : 65,
        "current_location": "Nairobi",
	    "receiver_name": "Moreen",
	    "receivers_location": "Kisumu",
	    "pickup_location": "Mama Ngina",
	    "weight": 23,
	    "price": 5443,
	    "status": "delivered"
    }]

# Order status after pickup
pending= "Your order is waiting to be sent"
on_transit= "in Transit"
delivered= "Delivered"
cancelled= "Cancelled"


class ParcelOrder(object):
    """Creating model for parcels"""
    def __init__(self):
        self.db = parcels
        self.order_id = len(self.db)
        self.status = pending

    def new_parcel(self, current_location,receiver_name ,receivers_location, pickup_location, weight, price):
        new_order_data = {
            "order_id": self.order_id + 1,
            "current_location": current_location,
            "receiver_name":receiver_name,
            "receivers_location":receivers_location,
            "pickup_location": pickup_location,
            "weight": weight,
            "price": price,
            "status": self.status
        }

        order = self.db.append(new_order_data)
        return order

    def parcels_list(self):
        return self.db

    def single_parcel(self, order_id):
        for parcel in parcels:
            if parcel["order_id"]== order_id:
                return parcel
            else:
                return {'parcel': 'Is nowhere to be found'}, 404

    def cancel_order(self, order_id):
        for parcel in parcels:
            if parcel["status"] == delivered:
                return {'parcel': "This parcel was already delivered and therefore cannot be canceled"}
            elif parcel['order_id'] == order_id:
                parcel.update({"status": cancelled})
                return {'parcel': 'Order Cancelled'}

    def clear(self):
    	self.db = []

    def get_orders_by_specific_user(self,user_id):
        """"Return orders by specific user"""
        user_orders = []
        for parcel in parcels:#Iterate over a sequence
            if (parcel['user_id'] == str(user_id)):
                user_orders.append(parcel)
            return user_orders
        return "Orders not found", 404
