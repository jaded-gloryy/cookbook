#will have measurement type mass, volume, or size

class Ingredient:
    """
    An ingredient object should only exist in the scope of a Recipe. It has several attributes:
        Name: The name of the ingredient
        Matter: Solid or liquid
        Measurement_type: Volume or mass
        Food_group: Fruit, vegetable, grain, protein, dairy, spice, activator, sweetener, oil
        Attribute: A catchall for ingredient descriptors (macronutrient)
        

    
    """
    def __init__(self, name, matter, food_group):
        self.name = name
        self.matter = matter
        # self.measurement_type = measurement_type
        self.food_group = food_group

    def assign_units(self, units):
        """
        Used to assign units of measurement (cups, grams, whole, etc)
        """
        self.units = units
    
    def assign_measurement(self, amount, units):
        self.amount = amount
        self.assign_units(units)


    # def assign_food_group(self, food_group):

    # def assign_type():
    # def assign_attribute()

    # def import_ingredient_measurements(ingredient, quanitity, unit):
        """
        Use if you have a list of ingredients and measurements (a quanitity - unit pair).
        """
        # measurements = []
        # ingredients = []
        # for i in range(len(quanitity)+1):
        #    measurement = Measurement(quanitity,unit)
        #    measurements.append(measurement)

        # for i in range(len(ingredient)+1):
        #     if ingredient


            
