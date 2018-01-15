from flask import Flask
import flask_restful
from climate import Climate
from climatelist import ClimateList
from prediction import Prediction
from climatemodel import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/dalbuquerque/Workspace/python/cli/dataset.db'
db.init_app(app)

api = flask_restful.Api(app)

api.add_resource(ClimateList, '/climate/')
api.add_resource(Climate, '/climate/<int:cli_id>')
api.add_resource(Prediction, '/climate/predict')

if __name__ == '__main__':
    app.run(debug=True)
