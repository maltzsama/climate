from flask_restful import Resource
from flask import jsonify
from climatemodel import ClimateModel

class Climate(Resource):

    def get(self, cli_id):
        if not cli_id:
            return jsonify({'Error'})
        response = ClimateModel.query.filter_by(id=cli_id).first()
        return jsonify(response.as_dict())
