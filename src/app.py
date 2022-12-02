import certifi
import pandas as pd
from pymongo import MongoClient
from classes.DatabaseClient import NoSQLDatabaseClient
from classes.Ingredient import Ingredient
from classes.Recipe import Recipe
from config import CONFIG
from recipe_flows import create_recipe

# three steps:

#connect to db
def standardize_ingredient_name(ingredient_name):
    ingredient = ingredient_name.lower()
    standardized_ingredient_name = ingredient.replace(" ","_")

    return standardized_ingredient_name

def request_ingredient_data(csv_filepath):
    """
    Used to request data for ingredient object creation.
    Requests user to provide a filepath to a csv containing the following ingredient data:

    Name: str; The name of the ingredient
    Matter: str; Solid or liquid
    Food_group: str; Ex: Fruit, vegetable, grain, protein, dairy, spice, activator, sweetener, oil
    Quantity: int; Quantity of the ingredient needed in a recipe
    Units: str; The units of measure for the ingredient (ex, cups, tsp)

    Input: filepath
    Output: 3 lists: ingredient names, 
    (name, matter, food_group),
    (quantity, units)
    """
    print("Importing recipe data...")
    data = pd.read_csv(csv_filepath)
    df = pd.DataFrame(data)
    df_removena = df.dropna(thresh=3)
    headings= list(df_removena.columns)
    ingredient_names = list(df_removena.name)

    standardized_ingredient_names = []
    
    #Grab headings from table and designate as keys
    # keys = []
    # for heading in headings:
    #     keys.append(heading.lower())

    #parse ingredient names and standardize format
    for dirty in ingredient_names:
        clean = standardize_ingredient_name(dirty)
        standardized_ingredient_names.append(clean)

    #ingredient data (should be a tuple: ingredient name, matter, food group)
    ingredient_data = []
    measurement_data = []
    for row in range(len(df_removena)):
        name = df_removena.name.iloc[row]
        matter = df_removena.matter.iloc[row]
        foodgroup = df_removena.food_group.iloc[row]
        quantity = df_removena.quantity.iloc[row]
        units = df_removena.units.iloc[row].lower()

        ingredient_data.append([name,matter,foodgroup])
        measurement_data.append([quantity, units])


    print("Successfully imported recipe data")
    return standardized_ingredient_names, ingredient_data, measurement_data


def connect_to_db():
    """
    Function to connect to cookbook db. 
    """
    print("Setting up Database Connection...")
    mongo_client = MongoClient(CONFIG["CONNECTION_STRING"], serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())
    print("Successfully connected to Database")

    print("Creating Database Client...")
    db_client = NoSQLDatabaseClient(mongo_client, CONFIG["DATABASE_NAME"])
    print("Database Client created")
    
    return db_client

ingredient_collection = CONFIG["INGREDIENT_COLLECTION_NAME"]
recipe_collecition = CONFIG["RECIPE_COLLECTION_NAME"]
recipe_filepath = CONFIG["RECIPE_FILEPATH"]

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
    standardized_ingredient_names, ingredient_data, measurement_data = request_ingredient_data(recipe_filepath)
    db_client = connect_to_db() 
    create_new_ingredients , non_existent_ingredients = db_client.query_ingredient(ingredient_collection, standardized_ingredient_names)

    if create_new_ingredients == True:
        print("Creating and uploading " + len(create_new_ingredients)) + " ingredient objects..."
        for ingredient in non_existent_ingredients:
            new_ingredient = Ingredient(ingredient_data[0], ingredient_data[1], ingredient_data[2])
            db_client.upload_ingredient(ingredient_collection, new_ingredient)
    

    #make measure obs


    #create Recipe
    recipe = Recipe()



    