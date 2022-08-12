from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DATABASE_NAME = 'flask_dev.db'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"
db = SQLAlchemy(app)
# Database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    
    def __repr__(self) -> str:
        return self.name


#We use marshal as django serializer
#here we list all the files we want to see
tasks_fields = {
    'id':fields.Integer,
    'name':fields.String,
}
#REST API
api = Api(app)

class Items(Resource):
    
    @marshal_with(tasks_fields)
    def get(self):
        tasks = Task.query.all()
        return tasks
    
    @marshal_with(tasks_fields)
    def post(self):
        data = request.json
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks

class Item(Resource):
    
    @marshal_with(tasks_fields)
    def get(self, pk):
        task = Task.query.filter_by(id=pk).first()
        return task
    
    @marshal_with(tasks_fields)
    def put(self, pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        task.name = data['name']
        db.session.commit()
        return task
    
    
    @marshal_with(tasks_fields)
    def delete(self, pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks
    
#REST-API Routing
api.add_resource(Items,'/')
api.add_resource(Item,'/<int:pk>')

#Main App
if __name__ == "__main__":
    app.run(debug=True)