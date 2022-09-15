from sqlalchemy import Column, String, Integer, Boolean

from app.main import db, bcrypt

class User(db.Model):
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
