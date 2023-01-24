from app.models import BaseModel
from app.extensions import db

class Employees(BaseModel):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    # dd/mm/yyyy
    date = db.Column(db.String(10))