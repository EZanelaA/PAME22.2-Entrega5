from flask import request
from flask.views import MethodView
from .models import Employees
from .schemas import EmployeeSchema, LoginSchema
from app.products.models import Products
from app.products.schemas import ProductSchema
from app.requests.models import Requests
from app.requests.schemas import RequestSchema
from flask_jwt_extended import create_access_token, jwt_required

class EmployeeLogin(MethodView):
    def post(self):
        schema = LoginSchema()
        data = request.json
        employee = Employees.query.filter_by(username = data["username"]).first()
        if not employee:
            return {"ERROR": "EMPLOYEE NOT FOUND"}, 404
        elif not employee.check_password(data["password"]):
            return {"ERROR": "WRONG PASSWORD"}, 401
        token = create_access_token(identity = employee.id)
        return {"employee": schema.dump(employee), "token": token}, 200


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
    decorators = [jwt_required()]
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
    decorators = [jwt_required()]
    # post: o funcionário <id> adiciona um produto em products
    def post(self, employee_id):
        schema = ProductSchema()
        employee = Employees.query.get(employee_id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        data = request.json
        data["inserted_by"] = employee_id
        try:
            product = schema.load(data)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        product.save()
        return schema.dump(product), 201
    
    # get: pega todo os itens que o funcionário <id> colocou em products
    def get (self, employee_id):
        schema = ProductSchema()
        employee = Employees.query.get(employee_id)
        if not employee:
            return {}, 404
        product = employee.inserted_products
        return schema.dump(product, many = True), 200

# /employees/<id>/products/<id>
class EmployeeProductDetails(MethodView):
    decorators = [jwt_required()]
    # put
    def put(self, employee_id, product_id):
        schema = ProductSchema()
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
        schema = ProductSchema()
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
        elif product not in employee.inserted_products:
            return {}, 401
        product.delete(product)
        return {}, 204

# /employees/<id>/requests
class EmployeeRequestController(MethodView):
    decorators = [jwt_required()]
    # post: o funcionário <id> adiciona um pedido em requests
    def post(self, employee_id):
        schema = RequestSchema()
        employee = Employees.query.get(employee_id)
        if not employee:
            return {"ERROR 404": "NOT FOUND"}, 404
        data = request.json
        data["requests_made"] = employee_id
        try:
            eRequest = schema.load(data)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        eRequest.save()
        return schema.dump(eRequest), 201
    
    # get: pega todo os pedidos feitos por funcionário <id>
    def get (self, employee_id):
        schema = RequestSchema()
        employee = Employees.query.get(employee_id)
        if not employee:
            return {}, 404
        eRequest = employee.requests_made
        return schema.dump(eRequest, many = True), 200

# /employees/<id>/requests/<id>
class EmployeeRequestDetails(MethodView):
    decorators = [jwt_required()]
    # put
    def put(self, employee_id, request_id):
        schema = RequestSchema()
        employee = Employees.query.get(employee_id)
        eRequest = Requests.query.get(request_id)
        if not employee and not eRequest:
            return {"ERROR 404": "NOT FOUND"}, 404 
        data = request.json
        try:
            eRequest = schema.load(data, instance = eRequest)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        eRequest.save()
        return schema.dump(eRequest), 201
    # patch
    def patch(self, employee_id, request_id):
        schema = RequestSchema()
        employee = Employees.query.get(employee_id)
        eRequest = Requests.query.get(request_id)
        if not employee and not eRequest:
            return {"ERROR 404": "NOT FOUND"}, 404 
        data = request.json
        try:
            eRequest = schema.load(data, instance = eRequest, partial = True)
        except:
            return {"ERROR 400": "BAD REQUEST"}, 400
        eRequest.save()
        return schema.dump(eRequest), 201
    # delete
    def delete(self, employee_id, request_id):
        employee = Employees.query.get(employee_id)
        eRequest = Requests.query.get(request_id)
        if not employee and not eRequest:
            return {"ERROR 404": "NOT FOUND"}, 404 
        elif eRequest not in employee.requests_made:
            return {}, 401
        eRequest.delete(eRequest)
        return {}, 204