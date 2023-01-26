from app.models import BaseModel
from app.extensions import db

class Products(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    # dd/mm/yyyy
    entry_date = db.Column(db.String(10))
    expiration_date = db.Column(db.String(10))
    inserted_by = db.Column(db.Integer, db.ForeignKey("employees.id"))