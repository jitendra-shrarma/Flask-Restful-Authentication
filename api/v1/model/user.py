from sqlalchemy import Column, String, Integer

from . import db, ma

class User(db.Model):
    username = Column(String(50), primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String)
    password = Column(String)
