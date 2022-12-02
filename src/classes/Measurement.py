#will have a integer and measurement type (cups, teaspoons, tablespoons --> volume, mass, size?)
class Measurement():
    def _init_(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit
        # #matter= liquid or solid
        # self.matter = matter 
        # #measurement type = cups, teaspoons, grams, etc
        # self.measurement_type = measurement_type

    # def create_measurement():
    #     """
    #     A function to combine 
    #     """
    
    # def get_measurement_type(self, ingredient_name):
    #     """
    #     A function to query the ingredient for the type of measurement (volume or mass)
    #     """
    #     ingredient_name = 