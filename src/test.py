from classes.Measurement import Measurement
from classes.Recipe import Recipe
from config import CONFIG
from utils import connect_to_db, standardize_name
import flows.ingredient_flows as iflow
from flows.recipe_flows import get_instance
from import_recipe import import_recipe
import os



# def test_updater(test_type):
#     if test_type == "import":
#         test_recipe_importer()

#     if test_type == "view":
#         test_view()

#     if test_type == "update":
#         test_update()

#     if test_type == "delete":
#         test_delete()

def test_recipe_importer (database_name, recipe_collection_name, ingredient_collection_name, directory_path, new_recipes):
    run = 1
    for recipe in new_recipes:
        print("**** Importing recipe " + str(run) + " of " + str(len(new_recipes))+ "*****")
        recipe_filepath = os.path.join(directory_path, recipe["recipe_filename"])
        directions_filepath = os.path.join(directory_path, recipe["directions_filename"])
        import_recipe(database_name=database_name, recipe_collection_name = recipe_collection_name,ingredient_collection_name=ingredient_collection_name, recipe_name=recipe["name"],recipe_filepath= recipe_filepath, directions_filepath=directions_filepath )
        run +=1
    print("Done testing imports")

def test_view(dbclient, collection_name, recipe_names):
    for recipe in recipe_names:
        print(f"Viewing {recipe} recipe")
        recipe_dict = dbclient.get_item(collection_name, recipe)
        if not recipe_dict:
            print(f"{recipe} doesn't exist")
        else:
            recipe_obj = get_instance(recipe_dict)
            new_line = '\n'
            print(f".{new_line}.{new_line}Recipe name: {recipe_obj.name} {new_line} Ingredients: {new_line}{recipe_obj.measured_ingredients} {new_line} Directions: {new_line}{recipe_obj.directions} {new_line}.{new_line}.")

def test_update(update_this, dbclient, recipe_collection, document_name):
    if update_this == "name":
        #test for updating name
        target="name"
        new_value = "new pizza"
        
    if update_this == "measurement":
    #test for updating a measurement
        target = "measured_ingredients"
        new_value = {"flour": {"quantity":"1000", "unit":"cups"}}
        
    if update_this == "directions":
        #test for updating diretions
        target = "directions"
        new_value= {"1": "new", "2":"directions", "3":"added"}
    
    dbclient.updateOne_document(recipe_collection, document_name=document_name, target=target , new_value = new_value)

def test_delete(dbclient, collection_name, filter_field, document_names):
    for name in document_names:
        dbclient.deleteOne_document(collection_name= collection_name, filter_field=filter_field, document_name= name)
    print("Completed deletion test")







# Uncomment when testing

# recipe_name = standardize_name("pitta")

database_name = CONFIG["TEST_DATABASE_NAME"]
recipe_collection_name = CONFIG["TEST_RECIPE_COLLECTION"]
ingredient_collection_name = CONFIG["TEST_INGREDIENT_COLLECTION"]

# recipe_names = ["pizza", "cerEAL", "hot milk"]
# recipe_filepaths = ["/Users/jadeevans/Documents/Code/cookbook/test docs/pizza_ing.csv","/Users/jadeevans/Documents/Code/cookbook/test docs/cereal_ing.csv","/Users/jadeevans/Documents/Code/cookbook/test docs/milk_ing.csv"]
# directions_filepaths = ["/Users/jadeevans/Documents/Code/cookbook/test docs/directions.csv","/Users/jadeevans/Documents/Code/cookbook/test docs/cereal_directions.csv","/Users/jadeevans/Documents/Code/cookbook/test docs/hot_milk_directions.csv"]
directory_path = "/Users/jadeevans/Documents/Code/cookbook/test docs"
new_recipes = [
    {
        "name": "pizza",
        "recipe_filename":"pizza_ing.csv",
        "directions_filename":"directions.csv"
    },
    {
        "name": "cerEAL",
        "recipe_filename":"cereal_ing.csv",
        "directions_filename":"cereal_directions.csv"
    },
    {
        "name": "hot milk",
        "recipe_filename":"milk_ing.csv",
        "directions_filename":"hot_milk_directions.csv"
    }

]

view_recipes = ["pizza", "cerEAL", "cats"]
delete_these = ["pizza","pasta"]
test_update_doc_name = "pizza"

# recipe_object = get_instance(dbclient.get_recipe(recipe_collection, recipe_name))
# dbclient.updateOne_document(recipe_collection, document_name=document_name, target=target , new_value = new_value)
# dbclient.deleteOne_document(recipe_collection, "name","pizza")

if __name__ == "__main__":
    dbclient = connect_to_db(database_name)
    # test_recipe_importer(database_name= database_name, recipe_collection_name=recipe_collection_name, ingredient_collection_name=ingredient_collection_name, recipe_names=recipe_names, recipe_filepaths=recipe_filepaths, directions_filepaths=directions_filepaths)
    test_recipe_importer(database_name= database_name,recipe_collection_name=recipe_collection_name, ingredient_collection_name=ingredient_collection_name, directory_path = directory_path,new_recipes=new_recipes  )
    
    start_next_test = input("Start next test: View? y or n ")
    if start_next_test == "y":
        test_view(dbclient, collection_name=recipe_collection_name, recipe_names= view_recipes)
    
    start_next_test = input("Start next test: Update? y or n ")
    if start_next_test == "y":
        print("Starting update test...")
        # update_this = input("Starting update test. What do you want to update? (name, measured_ingredients, directions)")
        update_these = ["measurement", "directions"]
        for this in update_these:
            test_update(this, dbclient,recipe_collection=recipe_collection_name, document_name=test_update_doc_name)
    
    start_next_test = input("Start next test: Delete? y or n ")
    if start_next_test == "y":
        print("Starting deletion test...")
        test_delete(dbclient, collection_name=recipe_collection_name, filter_field="name", document_names= delete_these)
