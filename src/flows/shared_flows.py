import certifi
from pymongo import MongoClient
from classes.DatabaseClient import NoSQLDatabaseClient
from config import CONFIG

def connect_to_db(database_name):
    """
    Function to connect to cookbook db. 
    """
    print("Setting up Database Connection...")
    mongo_client = MongoClient(CONFIG["CONNECTION_STRING"], serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())
    print("Successfully connected to Database")

    print("Creating Database Client...")
    db_client = NoSQLDatabaseClient(mongo_client, database_name )
    print("Database Client created")
    
    return db_client

def standardize_name(name):
    if type(name) != str:
        standardized_name = name 
    else:   
        lowercase_name = name.lower()
        standardized_name = lowercase_name.replace(" ","_")
    
    return standardized_name