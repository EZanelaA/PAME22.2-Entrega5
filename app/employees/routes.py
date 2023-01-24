from flask import Blueprint
from .controller import EmployeeController, EmployeeDetails

employee_api = Blueprint("employee_api", __name__)

employee_api.add_url_rule(
    "/employees",
    view_func = EmployeeController.as_view("employees_controller"),
    methods = ["GET", "POST"]
)

employee_api.add_url_rule(
    "/employees/<int:id>",
    view_func = EmployeeDetails.as_view("employees_cdetails"),
    methods = ["GET"]
)