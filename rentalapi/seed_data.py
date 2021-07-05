import sys
import click

from flask.cli import with_appcontext
from .dao.models import db, UserTypes, Vendors, Vehicles, Users, Rentals
from datetime import datetime

@click.command('dummy')
@with_appcontext
def insert_dummy_data():

    try:
        userT = UserTypes(name='USER')
        driverT = UserTypes(name='DRIVER')
        supplierT = UserTypes(name='SUPPLIER')

        user = Users(
            first_name='user',
            last_name='userl',
            username='user',
            email='user@email.com',
            password='user',
            rate=0)
        user.hash_password()
        user.usertype = userT
        db.session.add(user)

        driver = Users(
            first_name='driver',
            last_name='driverl',
            username='driver',
            email='driver@email.com',
            password='driver',
            rate=0)
        driver.hash_password()
        driver.usertype = driverT
        db.session.add(driver)

        supplier = Users(
            first_name='supplier',
            last_name='supplierl',
            username='supplier',
            email='supplier@email.com',
            password='supplier',
            rate=0)
        supplier.hash_password()
        supplier.usertype = supplierT
        db.session.add(supplier)
        db.session.commit()

        seed_prod_data()
    except Exception:
        import traceback
        traceback.print_exc(file=sys.stdout)
        db.session.rollback()

@click.command('seed')
@with_appcontext
def seed_data():
    try:
        from faker import Faker
        from faker_vehicle import VehicleProvider
        
        vendor_cache = {}

        fake = Faker()
        fake.add_provider(VehicleProvider)

        for i in range(100):
            fake_vehicle = fake.vehicle_object()
            vehicle1 = Vehicles(
            name=fake_vehicle['Model'],
            seats=fake.random_choices(elements=(2,4,5,7,8), length=1),
            color=fake.random_choices(elements=('Silver', 'Gray', 'White', 'Red', 'Blue', 'Sublime', 'Sublime', 'Glowing Yellow', 'Yellow', 'Stainless Steel', 'Purple', 'Pearl', 'Gold', 'Green', 'Orange', 'Copper'), length=1),
            make_year=fake_vehicle['Year'],
            rate=fake.random_int(min=4000, max=8000, step=350),
            type=fake_vehicle['Category'].split(',')[0])

            vendor_name = fake_vehicle['Make']

            if(not vendor_name in vendor_cache):
                vendor_cache[vendor_name] = Vendors(name=vendor_name)

            vendor = vendor_cache[vendor_name]
            
            vehicle1.vendor = vendor
            db.session.add(vehicle1)
        db.session.commit()
    except Exception:
        import traceback
        traceback.print_exc(file=sys.stdout)
        db.session.rollback()

def seed_prod_data():
    try:
        adminT = UserTypes(name='Admin')

        admin = Users(
            first_name='admin',
            last_name='admin',
            username='admin',
            email='admin@admin.com',
            password='admin123',
            rate=0)
        admin.hash_password()
        admin.usertype = adminT
        db.session.add(admin)
        db.session.commit()
    except Exception:
        import traceback
        traceback.print_exc(file=sys.stdout)
        db.session.rollback()