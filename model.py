from config import db

class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    vip = db.Column(db.Boolean, nullable=False)

    accounts = db.relationship('Account', backref='person', cascade="all, delete", lazy=True)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, VIP: {self.vip}'

class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, default=0)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return f'ID: {self.id}, Balance: {self.balance}'
