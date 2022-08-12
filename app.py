from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fake_data = {
    1:{'name':'clean car'},
    2:{'name':'write blog'},
    3:{'name':'buy food'},
    4:{'name':'build portfolio'},
}

class Items(Resource):
    # get all items
    def get(self):
        return fake_data
    # Add new item
    def post(self):
        data = request.json
        item_id = len(fake_data.keys()) + 1
        fake_data[item_id] = {'name':data['name']}
        return fake_data
    
class Item(Resource):
    # get a single item
    def get(self, pk):
        return fake_data.get(pk)
    # update item
    def put(self, pk):
        data = request.json
        fake_data[pk]['name'] = data['name']
        return fake_data
    
    # delete item
    def delete(self, pk):
        del fake_data[pk]
        return fake_data

api.add_resource(Items,'/')
api.add_resource(Item,'/<int:pk>')

if __name__ == "__main__":
    app.run(debug=True)