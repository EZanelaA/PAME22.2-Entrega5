from app.extensions import ma
from .models import Products

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Products
        load_instance = True
        ordered = True

    # identificação
    id = ma.Integer(dump_only = True)
    # nome do funcionário
    name = ma.String(required = True)
    # data de chegada no estoque
    entry_date = ma.String(required = True)
    # data de validade
    expiration_date = ma.String()
    inserted_by = ma.Integer()