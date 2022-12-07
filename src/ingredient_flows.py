import pandas as pd
from classes.Ingredient import Ingredient

def standardize_ingredient_name(ingredient_name):
    if type(ingredient_name) != str:
        standardized_ingredient_name = ingredient_name 
    else:   
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
    TODO: Make output a list of  dicts 
    """
    new_ingredients = []
    print("Creating " + str(len(non_existent_ingredients)) + " ingredient objects...")
    for ingredient in ingredient_data:
        if (ingredient[0] in non_existent_ingredients):
            new_ingredients.append(Ingredient(ingredient[0], ingredient[1], ingredient[2]).__dict__)
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
    # ingredient_names = list(df_removena.name)

    standardized_ingredient_names = []
    standardized_headings = []
    #Grab headings from table and designate as keys
    # keys = []
    # for heading in headings:
    #     keys.append(heading.lower())

    # #parse ingredient names and standardize format
    # for dirty in ingredient_names:
    #     clean = standardize_ingredient_name(dirty)
    #     standardized_ingredient_names.append(clean)

    for dirty in headings:
        clean = standardize_ingredient_name(dirty)
        standardized_headings.append(clean) 

    #ingredient data (should be a tuple: ingredient name, matter, food group)
    ingredient_data = []
    measurement_data = []

    heading_dict = {old_name:new_name for (old_name,new_name) in zip(headings, standardized_headings)}
    df_clean = df_removena.rename(columns=heading_dict)
    
    for row in range(len(df_clean)):
        # name = standardized_ingredient_names[row]
        name = standardize_ingredient_name(df_clean.name.iloc[row])
        standardized_ingredient_names.append(name)
        matter = standardize_ingredient_name(df_clean.matter.iloc[row])
        foodgroup = standardize_ingredient_name(df_clean.food_group.iloc[row])
        quantity = df_clean.quantity.iloc[row]
        units = standardize_ingredient_name(df_clean.units.iloc[row])

        ingredient_data.append([name,matter,foodgroup])
        measurement_data.append([quantity, units])


    print("Successfully imported recipe data")
    return standardized_ingredient_names, ingredient_data, measurement_data

    def request_direction_data(csv_filepath):

        """
        Used to create a dictionary from a csv.

        Input: filepath
        Output: dict
        """

        print("Importing direction data and buildling dictionary...")

        data = pd.read_csv(csv_filepath)
        df = pd.DataFrame(data)
        df_removena = df.dropna(thresh=3)

        steps = list(df_removena.steps)
        directions = list(df_removena.directions)

        direction_dict = {steps:directions for step,directions in zip(step,directions)}

        print("Sucessfully created Directions dictionary")
        return direction_dict