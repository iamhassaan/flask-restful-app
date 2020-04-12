from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)


# from flask import Flask, request
# from flask_restful import Resource, Api,reqparse
# from flask_jwt import JWT, jwt_required

# from security import authenticate, identity
# from user import UserRegister

# app=Flask(__name__)
# app.secret_key = 'jdoyle'
# api=Api(app)

# jwt=JWT(app, authenticate, identity)
# # when we initialize the JWT object, it is gonna create 2 endpoints, when we call / auth we send
# # it a username and a password

# #and the JWT extension gets the username and password and sends it over to the authenticate function. That takes
# #in a username and a passworcd ..d, we are then going to find the correct user object using the username and then we are going to compare the
# #user password to the one we received to do the auth endpoint. If they match we are going to return the user. And that becomes sort of
# #the identity.

# #jwt will gonna create a new endpoint, that endpoint will be /oath
# items=[]

# # imported from flask restful, allow us to very easliy add resources.
# # so we can say for this resource we can get and post, or for some you can put, delete and get .. e.t.c
# # Api works with resources and every resource has to be a class.
# # class STudent inherits form class Resiurce, student class becomes a copy of resource class.
# #201 = created
# #404 = notfound
# #200 = success
# #202= accepted, when we are delaying the creation


# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#         type=float,
#         required=True,
#         help="This field cannot be left blank!"
#     )




#     @jwt_required()
#     def get(self,name):
#         item=next(filter (lambda x:x['name'] ==name, items),None)
# # next is used in case there are no more items left after using next
#         return {'item':item}, 200 if item is not None else 400
#         # for x in items:
#         #     if x['name']==name:
#         #         return x
#         # return {'item':None}, 404

#     def post(self,name):

#         if next(filter(lambda x:x['name']==name,items),None):
#             return {"message":"An item with name {} already exists".format(name)}  ,400


#         data=request.get_json()
#         item= {'name':name, 'price':data['price']}
#         items.append(item)
#         return item, 201

#     @jwt_required()
#     def delete(self, name):
#         global items
#         items = list(filter(lambda x: x['name'] != name, items))
#         return {'message': 'Item deleted'}




#     @jwt_required()
#     def put(self, name):
#         data = Item.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item



# class ItemList(Resource):
#     def get(self):
#         return {'items': items}

# api.add_resource(Item, '/item/<string:name>')  #http://127.0.0.1:5000/student/Rolf
# api.add_resource(ItemList, '/items')
# api.add_resource(UserRegister, '/register')



# app.run(port=5000,debug=True)
