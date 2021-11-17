from app import db, login
from flask_login import UserMixin

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String, nullable=False)
    module = db.Column(db.SmallInteger())

    def __repr__(self) -> str:
        return f"{self.id}. {self.description}"

class AdminUser(UserMixin, db.Model):
    __tablename__ = "adminusers"
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}. {self.login} - {self.password}"

@login.user_loader
def load_user(id):
    return AdminUser.query.get(int(id))