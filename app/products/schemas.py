from app.extensions import ma
from .models import Products

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Products
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    name = ma.String(required = True)
    storage_date = ma.String(required = True)
    expiration_date = ma.String()
    inserted_by = ma.Integer()