import string
from xml.etree.ElementTree import tostring
from db.models import User
from db import db


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        User(),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return tostring(User.query.all())