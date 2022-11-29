#will have measurement type mass, volume, or size
from . import Measurement

class Ingredient:
    """
    An ingredient object has several attributes:
        Name: The name of the ingredient
        Matter: Solid or liquid
        Measurement_type: Volume or mass
        Food_group: Fruit, vegetable, grain, protein, or dairy
        
    
    """
    def __init__(self, name, matter, measurement_type, food_group):
        self.name = name
        self.mass_type = matter
        self.measurement_type = measurement_type
        self.food_group = food_group

    def assign_units(self, units):
        """
        Used to assign units of measurement (cups, grams, whole, etc)
        """
        self.units = units
    
    def assign_measurement(self, amount, units):
        self.amount = amount
        self.assign_units(units)


            
