# salesperson_dao_test.py
# France Cheong
# 21/01/2019

"""
The test is best done on an sapty database as the salesperson_id used is 1
And it can be run more than once
"""

# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from salesperson_dao import SalesPersonDAO

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

def test_create():
    # Get a session
    session = get_db_session()
    
    # Instantiate the salesperson DAO
    sap = SalesPersonDAO()

    # Setup the data as a dictionary
    """
    data = {}
    data['firstname'] = "France"
    data['lastname'] = "Cheong"
    data['title'] = "Mr"
    data['email'] = "f.cheong@gmail.com"
    data['work_phone'] = "(02) 9999 9999"
    """

    # Alternatively, the data could be set up in JSON format
    data = {
        'firstname':"France",
        'lastname': "Cheong",
        'title': "Mr",
        'email': "f.cheong@gmail.com",
        'work_phone': "(02) 9999 9999" # no comma on last item
    }

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = sap.create(session, data)

    # Print the result
    print(result)

    # Close the session
    session.close()

def test_find_by_id():
    # Get a session
    session = get_db_session()
    
    # Instantiate the salesperson DAO
    sap = SalesPersonDAO()

    # Assign an salesperson_id
    salesperson_id = 1 # exists
    #salesperson_id = 2 # does not exist?
    
    # Call the find_by_id() method from the DAO
    # and pass the salesperson_id as parameter - could pass it directly
    result = sap.find_by_id(session, salesperson_id)

    # Print the result
    print(result)
    
    # Close the session
    session.close()

def test_find_all():
    # Get a session
    session = get_db_session()
    
    # Instantiate the salesperson DAO
    sap = SalesPersonDAO()

    # Call the find_all() method from the DAO
    result = sap.find_all(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_find_by_lastname():
    # Get a session
    session = get_db_session()
        
    # Instantiate the salesperson DAO    
    sap = SalesPersonDAO()
      
    # Assign a lastname  
    lastname = "cheong" # exists
    #lastname = "xyz" # does not exist

    # Call the find_by_lastname() method from the DAO
    # and pass the lastname as parameter - could pass it directly
    result = sap.find_by_lastname(session, lastname)

    # Print the result
    print(result)

    # Close the session
    session.close()  

def test_find_ids():
    # Get a session
    session = get_db_session()
    
    # Instantiate the salesperson DAO
    sap = SalesPersonDAO()

    # Call the find_ids() method from the DAO
    result = sap.find_ids(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_update():
    # Get a session
    session = get_db_session()

    # Instantiate the salesperson DAO
    sap = SalesPersonDAO()

    # Assign an salesperson_id 
    salesperson_id = 1 # exists
    #salesperson_id = 2 # does not exist?

    # Create a dictionary and add items
    # Do not add the salesperson_id to the dict
    data = {}
    data['firstname'] = "Joe"
    data['lastname'] = "cheong"
    data['title'] = "Mr"
    data['email'] = "j.cheong@gmail.com"
    data['work_phone'] = "(02) 8888 9999"
    # Alternatively, the data could be defined in JSON format
        
    # Call the update() method from the DAO
    # and pass the salesperson_id and data as parameters    
    result = sap.update(session, salesperson_id, data)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_delete():
    # Get a session
    session = get_db_session()
        
    sap = SalesPersonDAO()

    # Assign an salesperson_id
    salesperson_id = 1 # exists
    #salesperson_id = 2 # does not exist?

    # Call the delete() method from the DAO
    # and pass the salesperson_id as parameter - could pass it directly
    result = sap.delete(session, salesperson_id)

    # Print the result
    print(result)

    # Close the session
    session.close()          

if __name__ == "__main__":

    # You may wish to comment/uncomment the functions calls below
    # To select which ones to run or not to run

    # If you run test_create() twice in a row
    # You will try to insert the same record twice
    # You Will get an integrity error
    # Phone number has to be unique
    # Either comment out test_create() (to run the other function calls)
    # Or use DB Browser for SQLite to delete the record

    # You may want to run test_delete() last
    # Because if you delete the record as soon as you insert
    # You cannot run the other tests like test_find_by_id(), test_update()

    # Use DB Browser for SQLite to check if data was really inserted/updated/deleted

    # If the database is opened in DB Browser for SQLite, 
    # you might not run the tests as the database will be locked
    # Need to close the database in DB Browser for SQLite

    print("\nTesting ...")

    # Test the create() method
    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_lastname()

    test_find_ids()

    test_update()

    test_delete()

