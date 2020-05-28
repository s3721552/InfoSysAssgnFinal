# schema.py
# Omar Adnan
# 04/05/2020

# Import packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float, Date, ForeignKey
# Used by classes PurchaseOrder and PurchaseOrderItem
from sqlalchemy.orm import relationship 

# Get a base class from which all mapped classes should inherit
Base = declarative_base()

# SalesPerson class should inherit from Base class
# Note that "SalesPerson" is spelt with an UPPERCASE "S"
class SalesPerson(Base): 

    # Define the name of the table i.e. employee (all lower case, singular)
    # Note that "employee" is spelt with a LOWERCASE "e"
    # Also note that there are TWO UNDERSCORES before and after "tablename"
    __tablename__ = 'salesperson'

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    salesperson_id = Column(Integer, primary_key=True) # primary key
    firstname = Column(String(255), nullable=False) # non null
    lastname = Column(String(255), nullable=False) # non null
    title = Column(String(255), nullable=False) # non null, unique
    email = Column(String(255), nullable=False, unique=True) # non null, unique
    work_phone = Column(String(20), nullable=False, unique=True) # non null, unique
    pass

# Define other classes in the database

# Supplier class should inherit from Base class
class Customer(Base):

    # Define the name of the table i.e. customer (all lower case, singular)
    __tablename__ = 'customer'

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    customer_id = Column(Integer, primary_key=True) # primary key
    customer_firstname = Column(String(255), nullable=False)
    customer_lastname = Column(String(255), nullable=False)
    customer_title = Column(String(255), nullable=False)
    customer_address = Column(String(255), nullable=False)
    customer_phone = Column(String(20), nullable=False, unique=True)
    customer_email = Column(String(255), nullable=False, unique=True)
    
# Product class should inherit from Base class    
class Vehicle(Base):

    # Define the name of the table 
    __tablename__ = 'vehicle' # i.e. vehicle (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    vehicle_id = Column(Integer, primary_key=True) # primary key
    salesperson_id = Column(Integer, ForeignKey("salesperson.salesperson_id")) # foreign key
    customer_id = Column(Integer, ForeignKey("customer.customer_id")) # foreign key 
    vehicle_make = Column(String(255), nullable=False)
    vehicle_model = Column(String(255), nullable=False)
    year_manu = Column(Integer, nullable=False)
    vehicle_price = Column(Float, nullable=False) # Float, not Integer
    
# Purchase class should inherit from Base class     
class Purchase(Base):

    # Define the name of the table
    __tablename__ = 'purchase' # i.e. purchase (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    purchase_id = Column(Integer, primary_key=True) # primary key
    salesperson_id = Column(Integer, ForeignKey("purchase.salesperson_id")) # foreign key
    order_date = Column(Date, nullable=False)
    card_payment = Column(Integer, nullable=False)
    cash_payment = Column(Integer, nullable=False)
    commision_sale = Column(Float, nullable=False) # Float, not Integer



    # Define the 1:m relationship between purchase_order and purchase_order_items
    # format: field_name = relationship("ClassName", back_populates="field_name")
    # "back_populates" means populate the other side of the mapping
    # "cascade="all, delete-orphan" needed for 
    # cascading the deletion of a purchase_order to its purchase_order_items
    # "all" means the child object should follow along with its parent in all cases, 
    # and be deleted once it is no longer associated with that parent
    purchase_order_items = relationship("PurchaseOrderItem", 
                                        back_populates="purchase", 
                                        cascade="all, delete-orphan")


# PurchaseOrderItem class should inherit from Base class
class PurchaseOrderItem(Base):

    # Define the name of the table # i.e. purchase_order_item (all lower case, singular)
    __tablename__ = 'purchase_order_item' 

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate

    # If having its own single column primary key
    purchase_order_item_id = Column(Integer, primary_key=True) # Primary key

    """
    # If having a composite primary key made up
    # purchase_order_id + product_id
    purchase_order_id = Column(Integer, 
                               ForeignKey("purchase_order.purchase_order_id"), 
                               nullable=False, 
                               primary_key=True, 
                               autoincrement=False) # set autoincrement to false
    product_id = Column(Integer, 
                        ForeignKey("product.product_id"), 
                        nullable=False, 
                        primary_key=True) # product_id is also part of the composite key
    """

    purchase_order_id = Column(Integer, 
                               ForeignKey("purchase.purchase_id"),
                               nullable=False,
                               primary_key=True,
                               autoincrement=False) # Foreign key
    vehicle_id = Column(Integer, 
                        ForeignKey("vehicle.vehicle_id"),
                        nullable=False,
                        primary_key=True)

    quantity = Column(Integer, nullable=False)
    date_required = Column(Date, nullable=False)

    # Define the m:1 relationship between purchase_order_items and purchase_order
    # format: field_name = relationship("ClassName", back_populates="field_name")
    # "back_populates" required to populate the other side of the mapping
    purchase = relationship("Purchase", back_populates="purchase_order_items")