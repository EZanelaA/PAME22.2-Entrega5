from app.models import BaseModel
from app.extensions import db

class Employees(BaseModel):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    entry_date = db.Column(db.String(10))
    inserted_products = db.relationship("Products", backref = "employees")
