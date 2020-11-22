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

        honda = Vendors(name='Honda')
        hero = Vendors(name='Hero')
        hyundai = Vendors(name='Hyundai')

        vehicle1 = Vehicles(
            name='Amaze',
            seats='4',
            color='Red',
            make_year='2018',
            rate='4000',
            type='CAR')
        vehicle1.vendor = honda
        db.session.add(vehicle1)

        vehicle2 = Vehicles(
            name='Creta',
            seats='5',
            color='Orange',
            make_year='2019',
            rate='5000',
            type='CAR')
        vehicle2.vendor = hyundai
        db.session.add(vehicle2)

        vehicle3 = Vehicles(
            name='Glamour',
            seats='2',
            color='Blue',
            make_year='2019',
            rate='5000',
            type='BIKE')
        vehicle3.vendor = hero
        db.session.add(vehicle3)
        db.session.commit()

        rental1 = Rentals(
            # driver_id
            # user_id
            days = 7,
            driver_rate = 2000,
            vehicle_rate = 4000,
            status = 'BOOKED',
            dispatched = datetime.now(),
            returned = None,
            vehicle = vehicle1,
            driver = driver,
            user = user,
        )
        db.session.add(rental1)
        db.session.commit()
        
    except Exception:
        import traceback
        traceback.print_exc(file=sys.stdout)
        db.session.rollback()
