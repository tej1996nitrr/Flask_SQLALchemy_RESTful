from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from Models.item import ItemModel

class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name) #this returns object
        
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)},400

        data = Item.parser.parse_args()

        item = ItemModel( name, data['price'])

        try:
            item.save_to_DB()
        except:
            return {"message": "An error occurred inserting the item."},500

        return item.json(),201

    

    @jwt_required()
    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()

        # return {'message': 'Item deleted'}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_fromdb()
        return {'message':'Item deleted'}
         

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item =ItemModel(name,data['price'])
        else:
            item.price = data['price']
        item.save_to_DB()
        return item.json()

        # updated_item = ItemModel( name, data['price'])
        # if item is None:
        #     try:
        #         updated_item.insert()
        #     except:
        #         return {"message": "An error occurred inserting the item."}
        # else:
        #     try:
        #         updated_item.update() #this is not item.update() because in SQl query it will update  existing values
        #     except:  #if we give item.update() it wont update
        #         raise
        #         return {"message": "An error occurred updating the item."}
        # return updated_item.json()

    


class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}