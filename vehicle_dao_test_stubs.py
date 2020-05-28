# vehicle_dao_test.py
# Omar Adnan
# 04/05/2020

# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from vehicle_dao import VehicleDAO

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def test_create():
    session = get_db_session()

    vhc = VehicleDAO()

    data = {}
    data['vehicle_make'] = "Toyota"
    data['vehicle_model'] = "Camry"
    data['year_manu'] = "2008"
    data['vehicle_price'] = "8999"

    result = vhc.create(session, data)

    print(result)

    session.close()

def test_find_by_id():
    session = get_db_session()

    vhc = VehicleDAO()

    vehicle_id = 1

    result = vhc.find_by_id(session, vehicle_id)

    print(result)

    session.close()

def test_find_all():
    sesison = get_db_session()

    vhc = VehicleDAO()

    result = vhc.find_all(session)

    print(result)

    session.close()    

def test_find_ids():
    session = get_db_session()

    vhc = VehicleDAO()

    result = vhc.find_ids(session)

    print(result)

    session.close()   

def test_update():
    session = get_db_session()

    vhc = VehicleDAO()

    vehicle_id = 1

    data = {}
    data['vehicle_make'] = "Holden"
    data['vehicle_model'] = "Commodore"
    data['year_manu'] = "2014"
    data['vehicle_price'] = "13000"

    result = vhc.update(session, vehicle_id, data)

    print(result)

    session.close()   

def test_delete():
    session = get_db_session()

    vhc = VehicleDAO()

    vehicle_id = 1

    result = vhc.delete(session, vehicle_id)

    print(result)

    session.close()         

if __name__ == "__main__":

    print("\nTesting ...")

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_ids()

    test_update()

    test_delete()

