
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class ClimateModel(db.Model):
    def __init__(self, db):
        self.db = db
    id = db.Column('id', db.Integer, primary_key=True)
    temp_max = db.Column('temp_max', db.Float)
    temp_min = db.Column('temp_min', db.Float)
    date = db.Column('date', db.String(128))
    rainfall = db.Column('rainfall', db.String(128))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}