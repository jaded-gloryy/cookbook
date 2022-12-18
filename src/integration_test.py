#Goal: Recreate test.py without using a database
import csv
import os
from config import CONFIG
from flows.ingredient_flows import createOne_ingredient, createMany_ingredients
from flows.recipe_flows import createOne_recipe
from utils import clean_dictionary, parse_dictionary

recipe_csv = "test_recipe_data.csv"
recipe_filepath = CONFIG["TEST_DOCS_FILEPATH"]

recipes = []
ingredients = []

dirty_recipe_names = []
test_data = os.path.join(recipe_filepath, recipe_csv)


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

    Input: [list]; recipe_data: a list of dicts
    Output: {dict}; object_data: a dict of object data
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


    # # Gather a list of all recipe names in the files
    #         dirty_recipe_name = row["recipe_name"]
    #         if dirty_recipe_name not in dirty_recipe_names:
    #             dirty_recipe_names.append(dirty_recipe_name)

    #         ## Make ingredient objects
    #         # read ingredient names
    #         ingredient_name = standardize_name(row["ingredient_name"])
    #         # check if they exist in ingredient list
    #         # if ingredient_name not in ingredients:

                
    #         # parse row dict
    #         ingredient_keys = ["ingredient_name", "matter", "food_group"]
    #         one_ingredient_dict = parse_dictionary(ingredient_keys, row)
    #         #create ingredients and update ingredient object list
    #         one_ingredient = createOne_ingredient(one_ingredient_dict)
    #         ingredients.update(one_ingredient)

    #         ## Make recipe objects
    #         # read 


if __name__ == "__main__":
    # Step 1: Import a recipe
    # a. Read in recipe data
    all_recipe_data = import_recipe_data(test_data)

    #clean and parse data
    all_object_data = parse_recipe_data(all_recipe_data)
    # I want all_object_data to looli like this:
        #{ingredient_data:[data], recipe_data:[data]}

    # b. Create ingredient and recipe objects
    for objects in all_object_data:
        create_this_recipe = objects["recipe_data"]
        create_these_ingredients = objects["ingredient_data"]

        many_ingredients = createMany_ingredients(create_these_ingredients)
        for ingredient_obj in many_ingredients:
            ing_name = ingredient_obj.name
            if ing_name in ingredients:
                print(f"{ing_name} has already exists.")
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
    

    # c. Create recipe objects
        # many_recipes = 

    # Step 2: View a recipe

    # Step 3: Update a recipe

    #Step 4: Delete a recipe