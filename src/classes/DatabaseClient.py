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

    def get_ingredients(self, collection_name, ingredient_names):
        """
        Get existing ingredients from db
        """
        ingredients = []
        collection = self._get_collection(collection_name)
        for name in ingredient_names:
            ingredient_name = name
        
            ingredient = collection.find_one(
            { "name": ingredient_name}
            )
            ingredients.append(ingredient)
        return ingredients
    
    def uploadOne_ingredient(self, collection_name, ingredient):
        """
        Upload a sinlge ingredient object to a db
        """
        collection = self._get_collection(collection_name)
        collection.insert_one(ingredient)

    def uploadMany_ingredients(self, collection_name, many_ingredients):
        """
        Upload many ingredient objects to a db
        """
        print("Uploading " + str(len(many_ingredients)) + " ingredient objects...")
        collection = self._get_collection(collection_name)
        collection.insert_many(many_ingredients)
        print("Ingredients successfully uploaded")
        
    def uploadOne_recipe(self, collection_name, recipe):
        """
        Upload a recipe object to a db
        """
        recipe_name = recipe["name"]
        collection = self._get_collection(collection_name)
        collection.insert_one(recipe)
        print(f"{recipe_name} recipe successfully uploaded")

    def get_item(self, collection_name, item_name):
        """
        Get an item from a db
        TODO: Add query terms and logic for recipes with the same name. Should I return them all?
        """
        collection = self._get_collection(collection_name)
        item = collection.find_one(
            { "name": item_name }
            )
        if not item:
            # Please use import_recipe.py if item doesn't exist
            print(f"{item_name} does not exist and needs to be created.")
        return item

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
                { "name": ingredient}
                )
                #may need to check if its already in nonexist list. don't add dups
            if existing_ingredient == None:
                non_existent_ingredients.append(ingredient)
        
        
        if len(non_existent_ingredients) != 0:
            create_new_ingredients = True
            print("Some ingredients were not found. Please create ingredient objects to continue and try again.)")


        return create_new_ingredients , non_existent_ingredients

    def updateOne_document(self, collection_name, document_name, target, new_value, filter_field = "name"):
        """
        Used to update a value in a document(recipe). This function finds the document by it's 
        filter_field. By default, filter_field is "name". 

        collection_name: str;
        filter_field: str; field to search by (ex. name)
        document_name: str; field value (ex. name of the recipe or ingredient)
        target: str; desired field to change (name, measured_ingredient, directions)
        new_value_dict: str or dict; the updated (new) value (ex. )
        """
        collection = self._get_collection(collection_name)
        # For a recipe: field = name, name = name of recipe
        filter = { filter_field: document_name}
        
        document = collection.find_one(filter)
        #copy is the current, unchanged version of the field
        if type(new_value) is dict:
            for key in new_value.keys():
                ingredient_key = key
            copy = document[target]
            copy.pop(ingredient_key)
            copy.update(new_value)

            newvalues = { "$set": {target: copy} }
        #get
        # Values to be updated
        else:
            newvalues = { "$set": {target: new_value} }
        
        collection.update_one(filter, newvalues)
        print("Successfully updated " + target)
        # collection.update_one(filter, copy)
    
    def deleteOne_document(self,collection_name, filter_field, document_name):
        """
        Used to delete a document.

        collection_name: str;
        filter_field: str; field to search by (ex. name)
        document_name: str; field value (ex. name of the recipe or ingredient)
        """
        collection = self._get_collection(collection_name)
        
        filter = { filter_field: document_name }
        document_deleted = collection.delete_one(filter)
        count_deleted = document_deleted.deleted_count 
        if count_deleted == 0:
            print("No documents were deleted. Please check your filter terms and try again")
        else: 
            print("Successfully deleted documents: " + str(count_deleted))


    


    # def get_measurement_type(self, collection_name):
    #     """
    #     Used to query db for ingredient measurement type (whole)
    #     """
    #     collection = self._get_collection(collection_name)
    #     collection.insertOne(recipe)
            