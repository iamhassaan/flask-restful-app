from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}


# when we initialize the JWT object, it is gonna create 2 endpoints, when we call / auth we send
# it a username and a password

#and the JWT extension gets the username and password and sends it over to the authenticate function. That takes
#in a username and a passworcd ..d, we are then going to find the correct user object using the username and then we are going to compare the
#user password to the one we received to do the auth endpoint. If they match we are going to return the user. And that becomes sort of
#the identity.






# imported from flask restful, allow us to very easliy add resources.
# so we can say for this resource we can get and post, or for some you can put, delete and get .. e.t.c
# Api works with resources and every resource has to be a class.
# class STudent inherits form class Resiurce, student class becomes a copy of resource class.
#201 = created
#404 = notfound
#200 = success
#202= accepted, when we are delaying the creation
