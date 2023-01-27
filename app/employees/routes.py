from flask import Blueprint
from .controller import EmployeeController, EmployeeDetails, EmployeeProductController, EmployeeProductDetails, EmployeeRequestController, EmployeeRequestDetails, EmployeeLogin

employee_api = Blueprint("employee_api", __name__)

employee_api.add_url_rule(
    "/login",
    view_func = EmployeeLogin.as_view("employee_login"),
    methods = ["POST"]
)

employee_api.add_url_rule(
    "/employees",
    view_func = EmployeeController.as_view("employee_controller"),
    methods = ["GET", "POST"]
)

employee_api.add_url_rule(
    "/employees/<int:id>",
    view_func = EmployeeDetails.as_view("employee_details"),
    methods = ["GET", "PUT", "PATCH", "DELETE"]
)

employee_api.add_url_rule(
    "/employees/<int:employee_id>/products",
    view_func = EmployeeProductController.as_view("employee_product_controller"),
    methods = ["POST", "GET"]
)

employee_api.add_url_rule(
    "/employees/<int:employee_id>/products/<int:product_id>",
    view_func = EmployeeProductDetails.as_view("employee_product_details"),
    methods = ["PUT", "PATCH", "DELETE"]
)

employee_api.add_url_rule(
    "/employees/<int:employee_id>/requests",
    view_func = EmployeeRequestController.as_view("employee_request_controller"),
    methods = ["POST", "GET"]
)

employee_api.add_url_rule(
    "/employees/<int:employee_id>/requests/<int:request_id>",
    view_func = EmployeeRequestDetails.as_view("employee_request_details"),
    methods = ["PUT", "PATCH", "DELETE"]
)