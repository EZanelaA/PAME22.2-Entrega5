from flask import Blueprint
from .controller import ProductController, ProductDetails

product_api = Blueprint("product_api", __name__)

product_api.add_url_rule(
    "/products",
    view_func = ProductController.as_view("product_controller"),
    methods = ["GET"]
)

product_api.add_url_rule(
    "/products/<int:id>",
    view_func = ProductDetails.as_view("product_details"),
    methods = ["GET"]
)