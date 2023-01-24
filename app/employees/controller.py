from flask import request
from flask.views import MethodView
from .models import Employees
from .schemas import EmployeeSchema

# /employees
class EmployeeController(MethodView):
    # post
    def post(self):
        schema = EmployeeSchema()
        data = request.json
        try:
            employee = schema.load(data)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        employee.save()
        return schema.dump(employee), 201
    # get
    def get(self):
        schema = EmployeeSchema()
        employees = Employees.query.all()
        return schema.dump(employees, many = True), 200
    # put
    # patch
    # delete
    pass

# /employees/<id>
class EmployeeDetails(MethodView):
    # post
    # get
    def get(self, id):
        schema = EmployeeSchema()
        employee = Employees.query.get(id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        return schema.dump(employee), 200
        
    # put
    # patch
    # delete
    pass