import uuid

from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50), nullable=False,
                     default=str(uuid.uuid4()))
    username = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())

    def __str__(self):
        return self.username

    @classmethod
    def new(cls, username, name, password):
        return User(username=username, name=name, password=password)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
