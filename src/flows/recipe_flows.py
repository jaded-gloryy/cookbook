from classes.Recipe import Recipe
from flows.ingredient_flows import createOne_measurement
from utils import standardize_name


def get_instance(dictionary):
    """
    Function to instantiate a class object from a dict (specifically, from a db query)
    Should be used after getting a recipe from a db.
    Input: Dict
    Output: Recipe object
    """
    if type(dictionary) is not dict:
        print("Recipe cannot be instantiated.")
        recipe = None
    else:
        name = dictionary["name"]
        measured_ingredients = dictionary["measured_ingredients"]
        directions = dictionary["directions"]
    
        recipe = Recipe(name, measured_ingredients, directions)
    
    return recipe

def create_recipe(recipe_name, ingredient_objects, measurement_objects, directions):
    """
    Create a recipe to upload to a db. Ask user for inputs: recipe name, ingredients and measurements, directions.
    recipe_name: string
    ingredients: list of Ingredient objects
    measurements: list of Measurement objects
    directions: dict {int; step: str; instruction} 

    Output: Dict containing a recipe
    TODO: create measured ingredients using create_measured_ingredient function?
    """

    standardized_recipe_name =  standardize_name(recipe_name)

    ingredient_names = []
    for ingredient in ingredient_objects:
        ingredient_names.append(ingredient.name)

    measured_ingredients = {ingredient:measurement for ingredient,measurement in zip(ingredient_names,measurement_objects)}
    recipe_object = Recipe(standardized_recipe_name, measured_ingredients ,directions).__dict__    

    return recipe_object


def create_measured_ingredients(ingredient_names,measurement_objects):
    """
    Function to create ingredient-measurement pairs
    """
     
    measured_ingredients = {ingredient:measurement for ingredient,measurement in zip(ingredient_names,measurement_objects)}
    return measured_ingredients

def createOne_recipe(recipe_dicts):
    """
    Create one recipe object from a list of recipe dictionaries.

    Inputs: [list]
    recipe_dicts: [list]; A list of dictionaries: keys = "ingredient_name", "measurement", "quantity", "recipe_name", "step", "directions"

    Output: List of Recipe objects
    """
    measured_ingredients = []
    direction_list = {}

# use dict.get in case the key doesn't exist
    for item in recipe_dicts:
        recipe_name = item.get("recipe_name")
        ingredient_name = item.get("ingredient_name")
        unit = item.get("units")
        quantity = item.get("quantity")
        step = item.get("step")
        directions = item.get("directions")
    
        if quantity:
            measurement = createOne_measurement(quantity, unit)
            measured_ingredient = {ingredient_name:measurement}
            measured_ingredients.append(measured_ingredient)
        
        if directions:
            direction_list.update({step:directions})

        recipe = Recipe(recipe_name, measured_ingredients, direction_list)
    
    return recipe


# def get_recipe():
#     """
#     Query database for recipe. Search by recipe name, ingredients, meal, or get a random recipe

#     """
#     return
# def create_measured_ingredient(ingredient_name, measurement_object):
#     """Used to create an ingredient - measurement pairing.
    
#     Input:  ingredient_name: "str"
#             measurement_object: {dict} 
#     Output: dict; {ingredient_name: measurement_object}
#     """
#     measured_ingredient = {ingredient_name:measurement_object}
#     return measured_ingredient


def calculate_servings():
    """
    Build a serving size scaler. This wwill be used to scale the recipe to the number of serving you want to make

    """

    return
