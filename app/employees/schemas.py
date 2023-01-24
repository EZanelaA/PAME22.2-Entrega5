from app.extensions import ma
from .models import Employees

class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employees
        load_instance = True
        ordered = True

    # identificação
    id = ma.Integer(dump_only = True)
    # nome do funcionário
    username = ma.String(required = True)
    # data de admissão
    date = ma.String(required = True)

