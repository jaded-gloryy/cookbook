import csv
from utils import clean_dictionary, parse_dictionary

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
