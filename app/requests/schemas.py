from app.extensions import ma
from .models import Requests

class RequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Requests
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    product_name = ma.String(required = True)
    quantity = ma.String(required = True)
    entry_date = ma.String(required = True)
    requested_by = ma.Integer()