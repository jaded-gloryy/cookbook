import pandas as pd
from classes.Ingredient import Ingredient

def standardize_ingredient_name(ingredient_name):
    ingredient = ingredient_name.lower()
    standardized_ingredient_name = ingredient.replace(" ","_")

    return standardized_ingredient_name

def create_ingredients(ingredient_data, non_existent_ingredients):
    """
    Function to create ingredient objects from a list of ingredients.

    Inputs:
    ingredient_data: list; (name, matter, food_group)
    non_existent_ingredients: list; (ingredient names)

    Output: A list of ingredient objects
    """
    new_ingredients = []
    print("Creating " + len(non_existent_ingredients) + " ingredient objects...")
    for ingredient in ingredient_data:
            if ingredient in non_existent_ingredients:
                new_ingredients.append(Ingredient(ingredient[0], ingredient[1], ingredient[2]))
    print("Sucessfully created ingredient objects")
    
    return new_ingredients

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
        name = standardized_ingredient_names[row]
        matter = df_removena.matter.iloc[row]
        foodgroup = df_removena.food_group.iloc[row]
        quantity = df_removena.quantity.iloc[row]
        units = df_removena.units.iloc[row].lower()

        ingredient_data.append([name,matter,foodgroup])
        measurement_data.append([quantity, units])


    print("Successfully imported recipe data")
    return standardized_ingredient_names, ingredient_data, measurement_data
