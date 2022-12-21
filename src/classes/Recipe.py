from utils import standardize_name

class Recipe:
    """
    A recipe object has several attributes:
        Name: The name of the recipe
        Ingredient section: A list of ingredients dicts {ingredient : measurement}
        Directions: A dict of steps on how to prepare the recipe

        TODO: Add a way to assign a pic for a recipe    
    """
    def __init__(self, name, measured_ingredients, directions):
        self.name = name
        self.measured_ingredients = measured_ingredients
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
    def delete_one_recipe(self, recipe_storage):      
        """
        Function to delete a recipe. 

        Inputs: 
            [recipe objects]; recipe_storage: a list containing all created recipes
        """

        for recipe_object_index in range(len(recipe_storage)):
            recipe_object = recipe_storage[recipe_object_index]
            found_recipe = True if recipe_object.name == self.name else False
            if found_recipe:
                recipe_storage.pop(recipe_object_index)
                print(f" Recipe: {self.name} has been deleted.")
                break
        if not found_recipe:
            print(f"{self.name} was not deleted because it doesn't exist.")

    def view(self):
        """
        Function to view a recipe.

        Inputs: 
            [list]; recipe_storage: a list containing all created recipes
        Output:
            recipe object: A recipe object view
        """
        print(f"Viewing {self.name} recipe")
        new_line = '\n'
        print(f". {new_line}. {new_line} Recipe name: {self.name} {new_line} Ingredients: {new_line} {self.measured_ingredients} {new_line} Directions: {new_line} {self.directions} {new_line}.{new_line}.")

    def update(self, update_dict):
        """
        Function to update an existing recipe.

        Inputs: 
            {dict}; update_dict: contains the desired changes
            [list]; recipe_storage: a list containing all created recipes

        """
                #make the changes
        update_dict_exists = True if update_dict else False
        if update_dict["recipe_name"]:
            new_name = update_dict["recipe_name"]
            self.name = standardize_name(new_name)
            print(f"Updated recipe name to {new_name}")

        if update_dict["measured_ingredients"]:
            new_measured_ingredients = update_dict["measured_ingredients"]
            self.measured_ingredients = new_measured_ingredients
            updated_this = []

            for ingredient in new_measured_ingredients:
                updated_this.append(ingredient)   
            print(f"Updated these ingredient measurements for {self.name}: {updated_this}")

        if update_dict["directions"]:
            new_directions = update_dict["directions"]
            self.directions = new_directions
            print(f"Updated {self.name} directions")

        elif not update_dict_exists:
            print(f"No changes were provided for {self.name}")

class Component(Recipe):
    """
    Component is a subclass of a Recipe. 
    """
    def __init__(self, name,measured_ingredients, directions):
        self.name = name
        Recipe.__init__(self, measured_ingredients, directions)
       
       
    def assign_ingredient(self, measured_ingredients):   
        self.measured_ingredients = measured_ingredients

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