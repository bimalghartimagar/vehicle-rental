from flask_restful import Resource
from rentalapi.schema import ma, IndexSchema

index_schema = IndexSchema()


class IndexAPI(Resource):
    def get(self):

        return index_schema.dump({}).data
