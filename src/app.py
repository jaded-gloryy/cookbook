import certifi
import pandas as pd
from pymongo import MongoClient
from classes.DatabaseClient import NoSQLDatabaseClient
from classes.Ingredient import Ingredient
from classes.Recipe import Recipe
from classes.Measurement import Measurement
from config import CONFIG
from recipe_flows import create_recipe
import ingredient_flows as iflow

# three steps:

#connect to db
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

# Comment when testing
# database_name = CONFIG["DATABASE_NAME"]
# ingredient_collection = CONFIG["INGREDIENT_COLLECTION_NAME"]
# recipe_collecition = CONFIG["RECIPE_COLLECTION_NAME"]
recipe_filepath = CONFIG["RECIPE_FILEPATH"]
directions_filepath = CONFIG["DIRECTIONS_FILEPATH"]
recipe_name = "Pizza"

# Uncomment when testing
database_name = CONFIG["TEST_DATABASE_NAME"]
ingredient_collection = CONFIG["TEST_COLLECTION_NAME"]
recipe_collecition = CONFIG["TEST_COLLECTION_NAME"]

#1. Create recipes
#a. read in ingredients using request_ingredient_data
#b. check for ingredient objects in db, add them if they don't exist
#c. create measurement objs

#instatiate a recipe object
# recipe = Recipe()
# ingredient_collection.query_ingredient("apple")
#2. Search and View Recipes

#3. Get recipe recommendations



if __name__ == "__main__":
    # Read in data for recipe
    standardized_ingredient_names, ingredient_data, measurement_data = iflow.request_ingredient_data(recipe_filepath)
    directions = iflow.request_direction_data(directions_filepath)
    db_client = connect_to_db(database_name) 
    
    #Check for ingredients in db
    create_new_ingredients , non_existent_ingredients = db_client.query_ingredient(ingredient_collection, standardized_ingredient_names)
    if create_new_ingredients == True:
        new_ingredients = iflow.create_ingredients(ingredient_data, non_existent_ingredients)
        db_client.uploadMany_ingredients(ingredient_collection, new_ingredients)
    
    # At this point all ingredients exist in the db
    ingredients = db_client.get_ingredients(ingredient_collection, standardized_ingredient_names)
    measurements = Measurement.createMany_measurements(measurement_data)

    #create Recipe
    new_recipe = create_recipe(recipe_name,ingredients,measurements,directions)
    




    