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
    db_client = NoSQLDatabaseClient(mongo_client, database_name)
    print("Database Client created")
    
    return db_client

def standardize_name(name):
    if type(name) != str:
        standardized_name = name 
    else:   
        lowercase_name = name.lower()
        standardized_name = lowercase_name.replace(" ","_")
    
    return standardized_name

def clean_dictionary (dictionary):
    """
    Function to standardize the values in a dict.

    Inputs: {dict}
    """
    for key, value in dictionary.items():
        # value = standardize_name(value)
        dictionary[key] = standardize_name(value)

def parse_dictionary(new_keys, dictionary):
    """
    Function to create a dictionary from an existing dictionary.

    Inputs: [list]; new_keys - a list of keys
            {dict}; row - a row dict from DictReader
    Output: {dict} 
    """
    parsed_dictionary = {}
    for key in dictionary:
        if key in new_keys:
            value = dictionary[key]
            if value:
                parsed_dictionary.update({key:value}) 
            
    if parsed_dictionary:
        return parsed_dictionary

def package_objects(object_data, object_names):
    """
    Function to package up objects.
    Returns n lists. n= len(object_names)

    Input: [list]; object_data: list of bundled data
    Output: n [lists]; 
    """
    for row in object_data:
        for i in range(len(row)):
            object_data[i]
