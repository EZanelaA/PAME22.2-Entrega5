from flask import request
from flask.views import MethodView
from .models import Employees
from .schemas import EmployeeSchema
from app.products.models import Products
from app.products.schemas import ProductsSchema

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

# /employees/<id>
class EmployeeDetails(MethodView):
    # get
    def get(self, id):
        schema = EmployeeSchema()
        employee = Employees.query.get(id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        return schema.dump(employee), 200
    # put
    def put(self, id):
        schema = EmployeeSchema()
        employee = Employees.query.get(id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        data = request.json
        try:
            employee = schema.load(data, instance = employee)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        employee.save()
        return schema.dump(employee), 201
    # patch
    def patch(self, id):
        schema = EmployeeSchema()
        employee = Employees.query.get(id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        data = request.json
        try:
            employee = schema.load(data, instance = employee, partial = True)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        employee.save()
        return schema.dump(employee), 201
    # delete
    def delete(self, id):
        #schema = EmployeeSchema()
        employee = Employees.query.get(id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        employee.delete(employee)
        return {}, 204

# /employees/<id>/products
class EmployeeProductController(MethodView):
    # post
    def post(self, employee_id):
        schema = ProductsSchema()
        employee = Employees.query.get(employee_id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        data = request.json
        try:
            product = schema.load(data)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        product.save()
        return schema.dump(product), 201

# /employees/<id>/products/<id>
class EmployeeProductDetails(MethodView):
    # put
    def put(self, employee_id, product_id):
        schema = ProductsSchema()
        employee = Employees.query.get(employee_id)
        product = Products.query.get(product_id)
        if not employee and not product:
            return {"ERROR 404": "NOT FOUND"}, 404 
        data = request.json
        try:
            product = schema.load(data, instance = product)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        product.save()
        return schema.dump(product), 201
    # patch
    def patch(self, employee_id, product_id):
        schema = ProductsSchema()
        employee = Employees.query.get(employee_id)
        product = Products.query.get(product_id)
        if not employee and not product:
            return {"ERROR 404": "NOT FOUND"}, 404 
        data = request.json
        try:
            product = schema.load(data, instance = product, partial = True)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        product.save()
        return schema.dump(product), 201
    # delete
    def delete(self, employee_id, product_id):
        employee = Employees.query.get(employee_id)
        product = Products.query.get(product_id)
        if not employee and not product:
            return {"ERROR 404": "NOT FOUND"}, 404 
        product.delete(product)
        return {}, 204
    pass