from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, reqparse
from app.api.v1.models import Users, users, ParcelOrder, parcels


parcel = ParcelOrder()
"""details for user login"""
required = reqparse.RequestParser()
required.add_argument('email', help = "Fill the email details", required = True)
required.add_argument('password', help = "Fill the password", required = True)

class CreateParcels(Resource):
    def post(self):
        data = request.get_json()
        current_location = data['current_location']
        receiver_name = data['receiver_name']
        receivers_location = data['receivers_location']
        pickup_location = data['pickup_location']
        weight = data['weight']
        price = data['price']
        parcel.new_parcel(current_location, receiver_name, receivers_location, pickup_location,weight,price)
        parcels = parcel.db
        return make_response(jsonify({"message": "The parcel order has been successfully created"}), 200)

class AllOrders(Resource):
    """Get the parcel details"""
    def get(self):
        return parcel.db


class SpecificOrder(Resource):
    """Get the specific parcel order using order_id"""
    
    def get(self, order_id):
        single_order = parcel.single_parcel(order_id)
        return  single_order
            

class CancelOrder(Resource):
    """Cancelling the order"""
    def put(self, order_id):
        cancel_order = parcel.cancel_order(order_id)
        return cancel_order

class GetOneOrder(Resource):
    """Getting the specific order using order ID"""
    def get(self, receiver_name):
        all_user_orders = parcel.get_orders_by_specific_user(receiver_name)
        return all_user_orders

user_save = Users()

class UserSignup(Resource):
    """registering a new user"""
    def post(self):
        data = request.get_json()
        username = data["username"]
        email = data["email"]
        default_location = data["default_location"]
        password = data["password"]
        user_save.create_user(username, email, default_location, password)
        users = user_save.udb
      
        return make_response(jsonify({
            "message" : "User has been successfully created",
            
        }),201)

class UserLogin(Resource):
    def post(self):
        user = required.parse_args()
        return Users.user_login(self,user['email'], user['password'])
