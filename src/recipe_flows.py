from classes.Recipe import Recipe

def create_recipe(recipe_name, ingredient_objects, measurement_objects, directions):
    """
    Create a recipe to upload to a db. Ask user for inputs: recipe name, ingredients and measurements,
    recipe_name: string
    ingredients: list of Ingredient objects
    measurements: list of Measurement objects
    directions: dict {int; step: str; instruction} 

    Output: Dict containing a recipe
    """
    ingredient_names = []
    for ingredient in ingredient_objects:
        ingredient_names.append(ingredient.name)

    measured_ingredients = {ingredient:measurement for ingredient,measurement in zip(ingredient_names,measurement_objects)}
    recipe_object = Recipe(recipe_name, measured_ingredients ,directions).__dict__    

    return recipe_object


# def get_recipe():
#     """
#     Query database for recipe. Search by recipe name, ingredients, meal, or get a random recipe

#     """
#     return


def calculate_servings():
    """
    Build a serving size scaler. This wwill be used to scale the recipe to the number of serving you want to make

    """

    return
