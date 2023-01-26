'''from flask.views import MethodView
from .models import Requests
from .schemas import RequestSchema

# /requests
class RequestController(MethodView):
    # get
    def get(self):
        schema = RequestSchema()
        request = Requests.query.all()
        return schema.dump(request, many = True), 200

# /requests/<id>
class RequestDetails(MethodView):
    # get
    def get(self, id):
        schema = RequestSchema()
        request = Requests.query.get(id)
        if not request:
            return {"ERROR 404": "NOT FOUND"}, 404
        return schema.dump(request), 200'''