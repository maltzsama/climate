from flask_restful import Resource
from flask import jsonify
from climatemodel import ClimateModel
from climatemodel import db


class Prediction(Resource):

    def get(self):
        response = ClimateModel.query.all()[-1:]
        if response:
            return jsonify(response[::-1][0].as_dict())
        else:
            self.error_handler('not found')

    def error_handler(self, message):
        return jsonify({"fail": message})

