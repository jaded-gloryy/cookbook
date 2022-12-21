
from classes.Ingredient import Ingredient
from classes.Measurement import Measurement

def create_one_ingredient(ingredient_dict): 
    """
    Function to create one ingredient object from a dictionary.

    Inputs:
    ingredient_dict: {dict}; keys = ingredient_name, matter, food_group

    Output: One ingredient object
    """

    name = ingredient_dict["ingredient_name"]
    matter = ingredient_dict["matter"]
    food_group = ingredient_dict ["food_group"]
    ingredient = Ingredient(name, matter, food_group)
    
    return ingredient

def create_many_ingredients(ingredient_dicts):
    """
    Function to create ingredient objects from a list of ingredients.

    Inputs:
    ingredient_dicts: [list]; A list of dictionaries: keys = ingredient_name, matter, food_group

    Output: List of ingredient objects
    TODO: provide a storage location and check if object exists there already, only create if it doesn't exist.
    TODO: add logic for removing duplicates in this function
    """
    many_ingredients = []
    
    for item in ingredient_dicts:
        if item and len(item.values()) == 3:
            name = item["ingredient_name"]
            matter = item["matter"]
            food_group = item ["food_group"]
            ingredient = Ingredient(name, matter, food_group)
            many_ingredients.append(ingredient)
    
    return many_ingredients

def create_one_measurement(quantity, unit):
    """
    A function to combine a quantity with unit
    Inputs: quantity: int, unit: str
    Output: A measurement object
    """
    measurement_object = Measurement(str(quantity), unit).__dict__
    return measurement_object

def create_many_measurements(measurement_data):
        """
        Helper function to generate a list of measurement objects for recipe creation.
        Input: list of quantity, unit pairs;
            quantity: int, unit: "str"
        Output: A list of measurement objects
            
        """
        measurement_objects = []
        for measurement in measurement_data:
            new_measurement_obj = Measurement(str(measurement[0]), measurement[1])

            measurement_objects.append(new_measurement_obj)
        
        return measurement_objects
