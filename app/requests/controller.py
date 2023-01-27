from flask.views import MethodView
from .models import Requests
from .schemas import RequestSchema

# /requests
class RequestController(MethodView):
    # get
    def get(self):
        schema = RequestSchema()
        eRequest = Requests.query.all()
        return schema.dump(eRequest, many = True), 200

# /requests/<id>
class RequestDetails(MethodView):
    # get
    def get(self, id):
        schema = RequestSchema()
        eRequest = Requests.query.get(id)
        if not eRequest:
            return {"ERROR 404": "NOT FOUND"}, 404
        return schema.dump(eRequest), 200