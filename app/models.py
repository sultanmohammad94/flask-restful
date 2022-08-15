from app import app
from flask_sqlalchemy import SQLAlchemy

DATABASE_NAME = 'flask_dev.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"

DATABASE_URL = 'postgres://mzerbmkchzctmd:22a424843fcb34bd75430c1e5ca3da05c2f325d0c9d384b696e14fbcbb530961@ec2-3-223-242-224.compute-1.amazonaws.com:5432/dd4kgvgutpv9no'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db = SQLAlchemy(app)

# Database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    
    def __repr__(self) -> str:
        return self.name
