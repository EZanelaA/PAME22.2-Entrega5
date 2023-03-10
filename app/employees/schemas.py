from app.extensions import ma
from .models import Employees
from app.products.schemas import ProductSchema
from app.requests.schemas import RequestSchema

class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employees
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    username = ma.String(required = True)
    password = ma.String(load_only = True, required = True)
    email = ma.String(required = True)
    hire_date = ma.String(required = True)
    inserted_products = ma.List(ma.Nested(ProductSchema), dump_only = True)
    requests_made = ma.List(ma.Nested(RequestSchema), dump_only = True)

class LoginSchema(ma.Schema):
    username = ma.String(required = True)
    password = ma.String(required = True, load_only = True)