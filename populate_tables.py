# populate_tables.py
# France Cheong
# 22/01/2019

# ########
# Packages
# ########
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ###########################################
# Import your classes defined in other files
# ###########################################
# From file xxx.py import class Xxxx
from schema import Employee
from schema import Supplier
from schema import Product
from schema import PurchaseOrder
from schema import PurchaseOrderItem

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def populate():

    # Get a session
    session = get_db_session()


    # Insert a list [] of Employees to employee table 
    # using the Employee constructor
    session.add_all([
        Employee(firstname = 'George', 
                 lastname = 'Tanner', 
                 title = 'Mr', 
                 email = 'g.tanner@theorg.com', 
                 work_phone = '(03) 98120001'),

        Employee(firstname = 'Samantha', 
                 lastname = 'Riley', 
                 title = 'Mrs', 
                 email = 's.riley@theorg.com',
                 work_phone = '(03) 98120002'),

        Employee(firstname = 'Rebecca', 
                 lastname = 'White', 
                 title = 'Ms', 
                 email = 'r.white@theorg.com', 
                 work_phone='(03) 98120003'),    
        ])


    # Insert a list [] of Products to product table
    # using the Product constructor
    session.add_all([
        Product(product_name='Paper ream', 
            product_description='80gm 500 sheets', 
            product_category='Stationery', 
            reorder_level=50, 
            lead_time_days=3, 
            unit_price=12.58, 
            discontinued=0),

        Product(product_name='Plastic pockets', 
            product_description='100 pack', 
            product_category='Stationery', 
            reorder_level=10, 
            lead_time_days=2, 
            unit_price=3.97, 
            discontinued=1),

        Product(product_name='Desk chair', 
            product_description='Standard gas-lift chair', 
            product_category='Furniture', 
            reorder_level=5, 
            lead_time_days=2, 
            unit_price=89.99, 
            discontinued=0)
    ])

    # Insert a list [] of Suppliers to supplier table
    # using the Supplier constructor
    session.add_all([
        Supplier(supplier_name='Quick Supplies', 
            contact_firstname='Jane', 
            contact_lastname='Jones', 
            contact_title='Ms', 
            street_address='50 Collins Street', 
            city='Melbourne', 
            postcode='3000',
            state='Victoria',
            country='Australia',
            phone='(03) 98672354',
            email='j.jones@quicksupplies.com.au',
            notes=''),

        Supplier(supplier_name='Supplies2U', 
            contact_firstname='Thomas', 
            contact_lastname='Smith', 
            contact_title='Mr', 
            street_address='396 George Street', 
            city='Sydney', 
            postcode='2000',
            state='New South Wales',
            country='Australia',
            phone='(02) 285671423',
            email='thomas.smith@supplies2u.com.au',
            notes=''),

        Supplier(supplier_name='SuppliesPlus', 
            contact_firstname='Sam', 
            contact_lastname='Brown', 
            contact_title='Mr', 
            street_address='105 Sydney Road', 
            city='Melbourne', 
            postcode='3000',
            state='Victoria',
            country='Australia',
            phone='(03) 99783521',
            email='sambrown@suppliesplus.com.au',
            notes='')    
    ])

    # etc

    # Commit the transactions
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
        populate()
