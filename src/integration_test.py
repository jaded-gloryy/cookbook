#Goal: Recreate test.py without using a database
import csv
import os
from config import CONFIG
from flows.ingredient_flows import createOne_ingredient, createMany_ingredients, createOne_measurement, createMany_measurements
from flows.recipe_flows import createOne_recipe, create_measured_ingredients 
from utils import clean_dictionary, parse_dictionary, standardize_name

recipe_csv = "test_recipe_data.csv"
recipe_filepath = CONFIG["TEST_DOCS_FILEPATH"]
test_data = os.path.join(recipe_filepath, recipe_csv)

recipes = []
ingredients = []

view_recipe_names = ["pizza", "mocha", "cereal"]


fake_measurement_updates = [(1000, "cups"), (1000, "tsp")]
fake_ingredient_list = ["flour", "salt"]
fake_measurement_objects = createMany_measurements(fake_measurement_updates)

recipe_to_update = "pizza"
recipe_to_update2 = "new_fake_recipe_name"
update_measured_ingredients = create_measured_ingredients(fake_ingredient_list, fake_measurement_objects)
update_directions = {"1": "new", "2":"directions", "3":"added"}
update_recipe_name = "new_fake_recipe_name"

recipe_update_config = {"recipe_name":update_recipe_name, "measured_ingredients":update_measured_ingredients, "directions":update_directions}
# recipe_update_config = {"recipe_name":update_recipe_name, "measured_ingredients":{}, "directions":{}}
recipe_update_config2 = {"recipe_name":"", "measured_ingredients":{}, "directions":{}}


def import_recipe_data(csv_file):
    """
    Function to read in and clean a csv file containing recipes. Each recipe should be separated by a blank line.
    Returns a list of clean recipe data, separated by recipe.

    Input: csv file
    Output: [list]
    """
    print("Importing recipe data...")

    recipe_data = []
    with open(csv_file, newline='') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        one_recipe = []
    
        for row  in dict_reader:
            dont_clean = row["step"] or row["directions"]
            if not dont_clean:
                clean_dictionary(row)
            name = row["recipe_name"]
            if not name: 
                recipe_data.append(one_recipe)
                one_recipe = []
            else:
                one_recipe.append(row)
        
    recipe_data.append(one_recipe)
    print("Recipe data sucessfully imported")
    return recipe_data

def parse_recipe_data (recipe_data):
    """
    Parses recipe data. Returns a list of data for object creation.

    Input: 
        [dict]; recipe_data: a list of dicts
    Output: 
        [dict]; object_data: a list of object data dicts
    """
    object_data = []
    ingredient_keys = ["ingredient_name", "matter", "food_group"]
    recipe_keys = ["ingredient_name", "units", "quantity", "recipe_name", "step", "directions"]
    for recipe in recipe_data:
        recipe_object_data = []
        ingredient_object_data = []
        one_object_data = {}
        for row in recipe:
            one_ingredient_dict = parse_dictionary(ingredient_keys,row)
            ingredient_object_data.append(one_ingredient_dict)
            one_recipe_dict = parse_dictionary(recipe_keys,row)
            recipe_object_data.append(one_recipe_dict)
        
        one_object_data.update({"ingredient_data":ingredient_object_data, "recipe_data":recipe_object_data})
        object_data.append(one_object_data)
        
    return object_data

def get_recipe (recipe_name, recipe_storage):
    """
    Function to get a recipe.

    Inputs: 
        "str" ; recipe_name: the name of a recipe to get
        [recipe objects]; recipe_storage: a list containing all created recipes
    Output:
        recipe object: A recipe object
    """
    

    for recipe_object in recipe_storage:
        found_recipe = True if recipe_object.name == recipe_name else False
        if found_recipe:
            return recipe_object
    if not found_recipe:
        print(f"Recipe: {recipe_name} not found")


def view_recipe(recipe_names, recipe_storage):
    """
    Function to view a recipe.

    Inputs: 
        [list] ; recipe_name: a list of recipes to view
        [list]; recipe_storage: a list containing all created recipes
    Output:
        recipe object: A recipe object view
    """
    for recipe_request in recipe_names:
        print(f"Viewing {recipe_request} recipe")

        view_this_recipe = get_recipe(standardize_name(recipe_request), recipe_storage)
        if not view_this_recipe:
            print(f"Recipe: {recipe_request} doesn't exist")
        else:
            new_line = '\n'
            print(f". {new_line}. {new_line} Recipe name: {view_this_recipe.name} {new_line} Ingredients: {new_line} {view_this_recipe.measured_ingredients} {new_line} Directions: {new_line} {view_this_recipe.directions} {new_line}.{new_line}.")   
                    

def update_recipe(recipe_name, update_dict, recipe_storage):
    """
    Function to update an existing recipe.

    Inputs: 
        "str"; recipe_name: the name of the recipe to update
        {dict}; update_dict: contains the desired changes
        [list]; recipe_storage: a list containing all created recipes

    """
    
    #get recipe to update

    for recipe in recipe_storage:
        recipe_found = True if recipe.name == recipe_name else False
        update_dict_exists = True if update_dict else False

        if update_dict_exists and recipe_found:
            # update_this_recipe = recipe

            #make the changes
            if update_dict["recipe_name"]:
                new_name = update_dict["recipe_name"]
                recipe.name = standardize_name(new_name)
                print(f"Updated {recipe_name} recipe name to {new_name}")

            if update_dict["measured_ingredients"]:
                new_measured_ingredients = update_dict["measured_ingredients"]
                recipe.measured_ingredients = new_measured_ingredients
                updated_this = []

                for ingredient in new_measured_ingredients:
                    updated_this.append(ingredient)   
                print(f"Updated these ingredient measurements for {recipe_name}: {updated_this}")

            if update_dict["directions"]:
                new_directions = update_dict["directions"]
                recipe.directions = new_directions
                print(f"Updated {recipe_name} directions")
            break
        elif not update_dict_exists:
            print(f"No changes were provided for {recipe_name}")
            break
    if update_dict_exists and not recipe_found:
        print(f"Recipe: {recipe_name} doesn't exist")

                
def delete_one_recipe(recipe_name, recipe_storage):      
    """
    Function to delete a recipe. 

    Inputs: 
        "str"; recipe_name
        [recipe objects]; recipe_storage: a list containing all created recipes
    """

    for recipe_object_index in range(len(recipe_storage)):
        recipe_object = recipe_storage[recipe_object_index]
        found_recipe = True if recipe_object.name == recipe_name else False
        if found_recipe:
            recipe_storage.pop(recipe_object_index)
            print(f" Recipe: {recipe_name} has been deleted.")
            break
    if not found_recipe:
        print(f"{recipe_name} was not deleted because it doesn't exist.")


    

if __name__ == "__main__":
    # Step 1: Import a recipe
    print("Starting recipe import test...")
    # a. Read in recipe data
    all_recipe_data = import_recipe_data(test_data)
    #clean and parse data
    all_object_data = parse_recipe_data(all_recipe_data)

    # b. Create ingredient and recipe objects
    for objects in all_object_data:
        create_this_recipe = objects["recipe_data"]
        create_these_ingredients = objects["ingredient_data"]

        many_ingredients = createMany_ingredients(create_these_ingredients)

        for ingredient_obj in many_ingredients:
            ing_name = ingredient_obj.name
            if ing_name in ingredients:
                print(f"{ing_name} already exists.")
            else:
                ingredients.append(ingredient_obj)
                print(f"Ingredient: {ing_name} has been created and saved.")

        recipe = createOne_recipe(create_this_recipe)
        rec_name = recipe.name
        if rec_name in recipes:
            print(f"{rec_name} already exists.")
        else:
            recipes.append(recipe)
            print(f"Recipe: {rec_name} has been created and saved.")

    print("Completed recipe import test.")
    # Step 2: View a recipe
    start_view_test = input("Start view test? y or n ")
    if start_view_test == "y":
        print("Starting recipe view test...")
        view_recipe(view_recipe_names, recipes)
        print("Recipe view test completed.")
    
    start_update_test = input("Start update recipe test? y or n ")
    if start_update_test == "y":
        print("Starting update recipe test...")
        update_recipe(recipe_to_update,recipe_update_config,recipes)
        print("Update recipe test completed.")

        print("Starting update recipe test...")
        update_recipe("mocha",None,recipes)
        print("Update recipe test completed.")
        
        print("Starting update recipe test...")
        update_recipe(recipe_to_update2, recipe_update_config2, recipes)
        print("Update recipe test completed.")

    view_recipe([update_recipe_name], recipes)

    #Step 4: Delete a recipe
    
    
    print("Starting deletion test...")
    print("Deleting the following recipe...")
    recipe_to_delete = view_recipe([update_recipe_name], recipes)

    delete_one_recipe(update_recipe_name, recipes)
    deleted_recipe = view_recipe([update_recipe_name], recipes)