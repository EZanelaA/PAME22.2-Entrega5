from app.models import BaseModel
from app.extensions import db

class Requests(BaseModel):
    __tablename__ = "requests"
    
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(50))
    quantity = db.Column(db.String(25))
    entry_date = db.Column(db.String(10))
    requested_by = db.Column(db.Integer, db.ForeignKey("employees.id"))