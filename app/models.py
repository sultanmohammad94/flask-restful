from app import app
from flask_sqlalchemy import SQLAlchemy

DATABASE_NAME = 'flask_dev.db'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"
db = SQLAlchemy(app)

# Database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    
    def __repr__(self) -> str:
        return self.name
