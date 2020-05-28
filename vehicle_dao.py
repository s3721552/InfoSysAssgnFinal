# vehicle_dao.py
# Omar Adnan
# 04/05/2020

# Import packages
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from schema import Vehicle

class VehicleDAO():

    def create(self, session, data):

        print("\nCreating a Vehicle...")
        print(data)


        vehicle = Vehicle(vehicle_make=data['vehicle_make'],
                    vehicle_model=data['vehicle_model'],
                    year_manu=data['year_manu'],
                    vehicle_price=data['vehicle_price']
                    )
        
        session.add(vehicle)
        session.commit()

        result = {}
        result['message'] = 'Vehicle added successfully'
        inserted_vehicle_id = vehicle.vehicle_id
        result['vehicle_id'] = inserted_vehicle_id

        return result

    def find_by_id(self, session, vehicle_id):
        print("\nFinding a vehicle")
        print(vehicle_id)

        vhc = session.query(Vehicle).get(vehicle_id)

        result = {}

        if not vhc:
            result['message'] = "Vehicle NOT found!"
        else:
            d = {}
            d['vehicle_id'] = vhc.vehicle_id
            d['vehicle_make'] = vhc.vehicle_make
            d['vehicle_model'] = vhc.vehicle_model
            d['year_manu'] = vhc.year_manu
            d['vehicle_price'] = vhc.vehicle_price

            result['vehicle'] = d

        return result
 
    def find_all(self, session):
        print("\nFinding all vehicles...")

        result = {}

        rows = session.query(Vehicle).all()

        if not rows:
            result['message'] = "NO vehicles found!" 
        else:
            list_vhc = []
            for x in rows:
                d = {}
                d['vehicle_id'] = x.vehicle_id
                d['vehicle_make'] = x.vehicle_make
                d['vehicle_model'] = x.vehicle_model
                d['year_manu'] = x.year_manu
                d['vehicle_price'] = x.vehicle_price
                list_vhc.append(d)
                pass

            result['vehicles'] = list_vhc

    def find_ids(self, session):
        """
        This is a special method similar to find_all but returns product_ids only, 
        not the full details
        """
        print("\nFinding all vehicle ids...")

        result = {}

        rows = session.query(Vehicle).all()

        if not rows:
            result['message'] = "NO Vehicles found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.vehicle_id)
                pass

            result['vehicle_id'] = list_ids

        return result

    def update(self, session, vehicle_id, data):
        print('\nUpdating vehicle...')
        print(vehicle_id)
        print(data)

        result = {}

        vhc = session.query(Vehicle).get(vehicle_id)

        vhc.vehicle_make = data['vehicle_make']
        vhc.vehicle_model = data['vehicle_model']
        vhc.year_manu = data['year_manu']
        vhc.vehicle_price = data['vehicle_price']

        session.commit()

        result['message'] = "Vehicle updated!"

        return result
        
    def delete(self, session, vehicle_id):
        print("\nDeleting vehicle...")
        print(vehicle_id)

        result = {}

        vhc = session.query(Vehicle).get(vehicle_id)
        session.delete(vhc)
        session.commit()

        result['message'] = "Vehicle deleted!"

        return result
     