from flask_restful import Resource
from flask import jsonify
from flask import request
from climatemodel import ClimateModel
from climatemodel import db


class ClimateList(Resource):

    def get(self):
        climates = ClimateModel.query.all()[::-1]
        response = []
        for idx, c in enumerate(climates):
            response.append(c.as_dict())
            if idx > 100:
                break
        return jsonify(response)

    def post(self):
        if request.is_json:
            content = request.get_json()
            new = ClimateModel(db)
            if content["temp_max"]:
                new.temp_max = float(content["temp_max"])
            if content["temp_min"]:
                new.temp_min = float(content["temp_min"])
            if content["rainfall"]:
                new.rainfall = bool(content["rainfall"])
            if content["date"]:
                new.date = content["date"]
            db.session.add(new)
            db.session.commit()

            return jsonify({"created": new.as_dict()})
        else:
            error_handler('problem to process')


    def error_handler(message):
        return jsonify({"fail": message})
