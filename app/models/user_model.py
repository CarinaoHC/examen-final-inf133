import json
from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    def __init__(self, name, email, password, phone, role=["user"]):
        self.name = name
        self.email = email
        self.role = json.dumps(role)
        self.password_hash = generate_password_hash(password)
        self.phone = phone
    def save(self):
        db.session.add(self)
        db.session.commit()
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()