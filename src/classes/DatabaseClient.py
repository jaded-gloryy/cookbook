class BaseClient:
    """
    A base class that can be used to setup receiving and driving with a 3rd party client
    """
    def __init__(self, client, name):
        self.client = client
        self.name = name

class NoSQLDatabaseClient(BaseClient):
    """
    This class is used for driving noSQL DB clients
    TODO: Add update and delete methods
    """
    def __init__(self, db_client, db_name):
        self.db_client = db_client
        self.db_name = db_name
        self._check_client_connection()

    def _check_client_connection(self):
        # The ping command is cheap and does not require auth.
        self.db_client.admin.command('ping')

    def _get_database(self):
        # Create the database for our example (we will use the same database throughout the tutorial
        return self.db_client[self.db_name]
    
    def _get_collection(self, name):
        return self._get_database().get_collection(name)
    
    def list_collection_names(self):
        return self._get_database().list_collection_names()

    def get_ingredient(self, collection_name, ingredient_name):
        """
        Get an existing ingredient from db
        """
        collection = self._get_collection(collection_name)
        ingredient = collection.find(
            { "name": ingredient_name}
            )
        return ingredient
    
    def upload_ingredient(self, collection_name, ingredient):
        """
        Upload an ingredient object to a db
        """
        collection = self._get_collection(collection_name)
        collection.insertOne(ingredient)

    def upload_recipe(self, collection_name, recipe):
        """
        Upload a recipe object to a db
        """
        collection = self._get_collection(collection_name)
        collection.insertOne(recipe)

    def get_recipe(self, collection_name, recipe_name):
        """
        Get a recipe object from a db
        TODO: Add query terms and logic for recipes with the same name. Should I return them all?
        """
        collection = self._get_collection(collection_name)
        recipe = collection.find(
            { "name": recipe_name}
            )
        return recipe

    def query_ingredient(self, collection_name, ingredient_names):
        """
        Used to query db for existing ingredient objects. 

        Inputs: 
        collection_name: string
        ingredient_names: list

        Outputs:
        create_new_ingredients: boolean
        non_existent_ingredients: list
        """
        collection = self._get_collection(collection_name)
        non_existent_ingredients = []
        create_new_ingredients = False

        for ingredient in ingredient_names:
            existing_ingredient = collection.find_one(
                { "name": ingredient_names}
                )
            if existing_ingredient == None:
                non_existent_ingredients.append(ingredient)
        
        
        if len(non_existent_ingredients) != 0:
            create_new_ingredients = True
            print("Some ingredients were not found. Please create ingredient objects to continue and try again. Ex. : Ingredient(" /" + ingredient /" + ", matter=, food_group=)")


        return create_new_ingredients , non_existent_ingredients
    # def get_measurement_type(self, collection_name):
    #     """
    #     Used to query db for ingredient measurement type (whole)
    #     """
    #     collection = self._get_collection(collection_name)
    #     collection.insertOne(recipe)
            