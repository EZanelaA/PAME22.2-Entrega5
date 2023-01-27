from app.models import BaseModel
from app.extensions import db
import bcrypt

class Employees(BaseModel):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.LargeBinary(128))
    email = db.Column(db.String(50))
    hire_date = db.Column(db.String(10))
    inserted_products = db.relationship("Products", backref = "employees")
    requests_made = db.relationship("Requests", backref = "employees")

    @property
    def password(self):
        raise AttributeError|("password: write-only field")

    @password.setter
    def password(self, psswrd):
        self.password_hash = bcrypt.hashpw(psswrd.encode(), bcrypt.gensalt())

    def check_password(self, psswrd):
        return bcrypt.checkpw(psswrd.encode(), self.password_hash)