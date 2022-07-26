# import default modules
from sqlalchemy import Column, String, Integer, Boolean

# import database, bcrypt
from app.main import db, bcrypt


# User model, fields(user_id, first_name, last_name, username, email, password_hash)
class User(db.Model):
    """ User model, fields(user_id, first_name, last_name, username, email, password_hash) """
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    # generate password_hash with password
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    # check saved password_hash with password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
