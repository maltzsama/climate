from flask_restful import Resource
from flask import jsonify
from climatemodel import ClimateModel
from climatemodel import db

class Climate(Resource):

    def get(self, cli_id):
        if not cli_id:
            self.error_handler('not valid')
        response = ClimateModel.query.filter_by(id=cli_id).first()
        if response:
            return jsonify(response.as_dict())
        else:
            self.error_handler('not found')

    def delete(self, cli_id):
        if not cli_id:
            self.error_handler('not valid')

        response = ClimateModel.query.filter_by(id=cli_id).first()
        if response:
            db.session.delete(response);
            x = db.session.commit()
            print x
            return jsonify(str(x))
        else:
            self.error_handler('not found')

    def error_handler(self, message):
        return jsonify({'Error': message})