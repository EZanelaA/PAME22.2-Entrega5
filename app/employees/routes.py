from flask import Blueprint
from .controller import EmployeeController, EmployeeDetails, EmployeeProductController, EmployeeProductDetails

employee_api = Blueprint("employee_api", __name__)

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
    methods = ["POST"]
)

employee_api.add_url_rule(
    "/employees/<int:employee_id>/products/<int:product_id>",
    view_func = EmployeeProductDetails.as_view("employee_product_details"),
    methods = ["PUT", "PATCH", "DELETE"]
)