from flask import Flask, Blueprint
from flask_restful import Api, Resource

from app.api.v1.views import CreateParcels, AllOrders, SpecificOrder, UserLogin,UserSignup, CancelOrder, GetOneOrder
v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(v1)
#register the blueprints
api.add_resource(CreateParcels, "/parcel", strict_slashes=False)
api.add_resource(AllOrders, "/parcels", strict_slashes=False)
api.add_resource(SpecificOrder, '/parcels/<int:order_id>', strict_slashes=False)
api.add_resource(UserSignup, "/users/signup", strict_slashes=False)
api.add_resource(UserLogin, "/users/login", strict_slashes=False)
api.add_resource(CancelOrder, "/parcels/cancel", strict_slashes=False)
api.add_resource(GetOneOrder, "/parcels/userorder/<int:user_id>", strict_slashes=False)