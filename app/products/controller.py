from flask.views import MethodView
from .models import Products
from .schemas import ProductSchema

# /products
class ProductController(MethodView):
    # get
    def get(self):
        schema = ProductSchema()
        product = Products.query.all()
        return schema.dump(product, many = True), 200

# /product/<id>
class ProductDetails(MethodView):
    # get
    def get(self, id):
        schema = ProductSchema()
        product = Products.query.get(id)
        if not product:
            return {"ERROR 404": "NOT FOUND"}, 404
        return schema.dump(product), 200