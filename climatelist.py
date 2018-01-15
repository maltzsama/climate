from flask_restful import Resource
from flask import jsonify
# from climatemodel import ClimateModel
from climatemodel import ClimateModel

class ClimateList(Resource):

    def get(self):
        climates = ClimateModel.query.all()[:100]
        response = []
        for c in climates:
            response.append(c.as_dict())
        return jsonify(response)
