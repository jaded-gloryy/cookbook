# What defines a recipe?
# list of measured ingredients
# list of instructions

class Recipe:
    """
    A recipe object has several attributes:
        Name: The name of the recipe
        Ingredients: A list of ingredients dicts {ingredient : measurement}
        Directions: A dict of steps on how to prepare the recipe

        TODO: Add a way to assign a pic for a recipe    
    """
    def __init__(self, name, ingredients, directions):
        self.name = name
        self.ingredients = ingredients
        self.directions = directions

    # def create_recipe():
        # Recipe("pizza", ingredients, directions,12)

    def add_cook_time(self, cook_time):
        self.cook_time = cook_time
    def add_prep_time(self, prep_time):
        self.prep_time = prep_time
    def add_servings (self, servings, serving_size=None):
        self.servings = servings
        self.serving_size = serving_size

class Component(Recipe):
    """
    Component is a subclass of a Recipe. 
    """
    def __init__(self, name,ingredients, directions):
        self.name = name
        Recipe.__init__(self, ingredients, directions)
       
       
    def assign_ingredient(self, ingredient):   
        self.ingredients = ingredient

    def assign_directions(self, directions):
        self.directions = directions

    def add_component(self,component):
        """
        Specify components of a recipe ex. Dough and sauce for pizza
        """
        self.components.append(component)

    def assign_ingredient_to_component(self, component, ingredient):
        """
        Assigns an ingredient to a specific recipe component. 
        Ex. Dough: Ingredients = ["flour", "yeast", "salt"]
        """
        self.component.ingredient = ingredient