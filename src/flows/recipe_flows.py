from classes.Recipe import Recipe
from flows.ingredient_flows import create_one_measurement
from utils import standardize_name


def create_measured_ingredients(ingredient_names,measurement_objects):
    """
    Function to create ingredient-measurement pairs
    """
     
    measured_ingredients = {ingredient:measurement for ingredient,measurement in zip(ingredient_names,measurement_objects)}
    return measured_ingredients

def create_one_recipe(recipe_dicts):
    """
    Create one recipe object from a list of recipe dictionaries.

    Inputs: [list]
    recipe_dicts: [list]; A list of dictionaries: keys = "ingredient_name", "measurement", "quantity", "recipe_name", "step", "directions"

    Output: List of Recipe objects
    TODO: provide a storage location and check if object exists there already, only create if it doesn't exist.
    TODO: add logic for removing duplicates in this function
    """
    measured_ingredients = []
    direction_list = {}

# use dict.get in case the key doesn't exist
    for item in recipe_dicts:
        recipe_name = standardize_name(item.get("recipe_name"))
        ingredient_name = item.get("ingredient_name")
        unit = item.get("units")
        quantity = item.get("quantity")
        step = item.get("step")
        directions = item.get("directions")
    
        if quantity:
            measurement = create_one_measurement(quantity, unit)
            measured_ingredient = {ingredient_name:measurement}
            measured_ingredients.append(measured_ingredient)
        
        if directions:
            direction_list.update({step:directions})

    recipe = Recipe(recipe_name, measured_ingredients, direction_list)
    
    return recipe

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
        
def calculate_servings():
    """
    Build a serving size scaler. This wwill be used to scale the recipe to the number of serving you want to make

    """

    return
