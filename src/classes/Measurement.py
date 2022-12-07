#will have a integer and measurement type (cups, teaspoons, tablespoons --> volume, mass, size?)
class Measurement:

    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit
        # #matter= liquid or solid
        # self.matter = matter 
        # #measurement type = cups, teaspoons, grams, etc
        # self.measurement_type = measurement_type

    # def get_measurement_type(self, ingredient_name):
    #     """
    #     A function to query the ingredient for the type of measurement (volume or mass)
    #     """
    #     ingredient_name = 


    def create_measurement(quantity, unit):
        """
        A function to combine a quantity with unit
        Inputs: quantity: int, unit: str
        Output: A measurement object
        """
        measurement_object = Measurement(quantity, unit)
        return measurement_object

    def createMany_measurements(measurement_data):
        """
        Helper function to generate a list of measurement objects for recipe creation.
        Input: list of quantity, unit pairs;
            quantity: int, unit: str
        Output: A list of measurement objects
            
        """
        measurement_objects = []
        for measurement in measurement_data:
            new_measurement = Measurement.create_measurement(measurement[0], measurement[1])

            measurement_objects.append(new_measurement)
        
        return measurement_objects