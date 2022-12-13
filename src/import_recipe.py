from classes.Measurement import Measurement
from config import CONFIG
from flows.recipe_flows import create_recipe
import flows.ingredient_flows as iflow
from utils import connect_to_db, standardize_name

def import_recipe(database_name, ingredient_collection_name, recipe_collection_name, recipe_name, recipe_filepath, directions_filepath):
    db_client = connect_to_db(database_name)
    recipe_name = standardize_name(recipe_name)
    # Check if the recipe has already been created
    recipe_exists = True if db_client.get_item(recipe_collection_name, recipe_name) else False
    
    if recipe_exists:
        # Please use update_recipe.py to make edits
        print(f"{recipe_name} recipe has already been created.")
    
    else:
        # Read in data for recipe
        print(f"Creating {recipe_name} recipe")
        standardized_ingredient_names, ingredient_data, measurement_data = iflow.request_ingredient_data(recipe_filepath)
        directions = iflow.request_direction_data(directions_filepath)
        
        
        #Check for ingredients in db
        create_new_ingredients , non_existent_ingredients = db_client.query_ingredient(ingredient_collection_name, standardized_ingredient_names)
        if create_new_ingredients == True:
            new_ingredients = iflow.create_ingredients(ingredient_data, non_existent_ingredients)
            db_client.uploadMany_ingredients(ingredient_collection_name, new_ingredients)
        
        # At this point all ingredients exist in the db
        queried_ingredient_data = db_client.get_ingredients(ingredient_collection_name, standardized_ingredient_names)
        ingredients = iflow.get_instances(queried_ingredient_data)
        measurements = Measurement.createMany_measurements(measurement_data)

        #create Recipe
        new_recipe = create_recipe(recipe_name,ingredients,measurements,directions)
        db_client.uploadOne_recipe(recipe_collection_name,new_recipe)

# recipe_filepath = CONFIG["RECIPE_FILEPATH"]
# directions_filepath = CONFIG["DIRECTIONS_FILEPATH"]

# database_name = CONFIG["DATABASE_NAME"]
# ingredient_collection = CONFIG["INGREDIENT_COLLECTION_NAME"]
# recipe_collection = CONFIG["RECIPE_COLLECTION_NAME"]
# recipe_name = standardize_name(input("What is the name of this recipe?"))

# database_name = CONFIG["TEST_DATABASE_NAME"]
# ingredient_collection = CONFIG["TEST_COLLECTION_NAME"]
# recipe_collection = CONFIG["TEST_COLLECTION_NAME2"]
# recipe_name = standardize_name("pizza")


if __name__ == "__main__":
    import_recipe()
    
    




    