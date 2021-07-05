from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import generate_password_hash, check_password_hash

db = SQLAlchemy()
migrate = Migrate()


class TimeStampMixin(object):
    created = db.Column(db.DateTime, nullable=False,
                        server_default=str(datetime.utcnow()))
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


class Vendors(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    vehicles = db.relationship('Vehicles', backref='vendor', lazy=True)

    def __repr__(self):
        return '<Vendor %r>' % self.name


class Vehicles(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    make_year = db.Column(db.String, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'),
                          nullable=False)
    img_url = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<Vehicle id %r with name %r>' % self.id, self.name


class UserTypes(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    users = db.relationship('Users', backref='usertype', lazy=True)

    def __repr__(self):
        return '<User Type %r>' % self.name


class Rentals(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)

    driver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)

    days = db.Column(db.Integer, nullable=False)
    driver_rate = db.Column(db.Float, nullable=False)
    vehicle_rate = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    dispatched = db.Column(db.DateTime)
    returned = db.Column(db.DateTime)

    vehicle = db.relationship('Vehicles', foreign_keys='rentals.c.vehicle_id', backref="vehicle", lazy=True)

    driver = db.relationship('Users', foreign_keys='rentals.c.driver_id',
                              backref='driver', lazy=True)
    user = db.relationship('Users', foreign_keys='rentals.c.user_id',
                            backref='user', lazy=True)

    def __repr__(self):
        return '<Rental %r>' % self.id


class Users(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'),
                        nullable=False)
    rate = db.Column(db.Float, nullable=True, server_default=str(0.0))
    img_url = db.Column(db.String, nullable=True)
    def __repr__(self):
        return '<User %r>' % self.username

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
