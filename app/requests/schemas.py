'''from app.extensions import ma
from .models import Requests

class RequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Requests
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only = True)
    requested_by = ma.Integer()'''