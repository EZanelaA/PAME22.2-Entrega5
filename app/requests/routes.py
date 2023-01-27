from flask import Blueprint
from .controller import RequestController, RequestDetails

request_api = Blueprint("request_api", __name__)

request_api.add_url_rule(
    "/requests",
    view_func = RequestController.as_view("request_controller"),
    methods = ["GET"]
)

request_api.add_url_rule(
    "/requests/<int:id>",
    view_func = RequestDetails.as_view("request_details"),
    methods = ["GET"]
)