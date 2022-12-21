#Goal: Recreate test.py without using a database
import os
from config import CONFIG
from flows.ingredient_flows import create_many_ingredients, create_many_measurements
from flows.recipe_flows import create_one_recipe, create_measured_ingredients, get_recipe 
from prep_data import import_recipe_data, parse_recipe_data

recipe_csv = "test_recipe_data.csv"
recipe_filepath = CONFIG["TEST_DOCS_FILEPATH"]
test_data = os.path.join(recipe_filepath, recipe_csv)

recipes = []
ingredients = []

view_recipe_names = ["pizza", "mocha", "cereal"]


fake_measurement_updates = [(1000, "cups"), (1000, "tsp")]
fake_ingredient_list = ["flour", "salt"]
fake_measurement_objects = create_many_measurements(fake_measurement_updates)

recipe_to_update = "pizza"
recipe_to_update2 = "new_fake_recipe_name"
update_measured_ingredients = create_measured_ingredients(fake_ingredient_list, fake_measurement_objects)
update_directions = {"1": "new", "2":"directions", "3":"added"}
update_recipe_name = "new_fake_recipe_name"

recipe_update_config = {"recipe_name":update_recipe_name, "measured_ingredients":update_measured_ingredients, "directions":update_directions}
# recipe_update_config = {"recipe_name":update_recipe_name, "measured_ingredients":{}, "directions":{}}
recipe_update_config2 = {"recipe_name":"", "measured_ingredients":{}, "directions":{}}
                    

if __name__ == "__main__":
    # Step 1: Import a recipe
    print("Starting recipe import test...")
    # a. Read in recipe data
    all_recipe_data = import_recipe_data(test_data)
    #clean and parse data
    all_object_data = parse_recipe_data(all_recipe_data)

    # b. Create ingredient and recipe objects
    for objects in all_object_data:
        create_this_recipe = objects["recipe_data"]
        create_these_ingredients = objects["ingredient_data"]

        many_ingredients = create_many_ingredients(create_these_ingredients)

        for ingredient_obj in many_ingredients:
            ing_name = ingredient_obj.name
            if ing_name in ingredients:
                print(f"{ing_name} already exists.")
            else:
                ingredients.append(ingredient_obj)
                print(f"Ingredient: {ing_name} has been created and saved.")

        recipe = create_one_recipe(create_this_recipe)
        rec_name = recipe.name
        if rec_name in recipes:
            print(f"{rec_name} already exists.")
        else:
            recipes.append(recipe)
            print(f"Recipe: {rec_name} has been created and saved.")

    print("Completed recipe import test.")
    # Step 2: View a recipe
    start_view_test = input("Start view test? y or n ")
    if start_view_test == "y":
        print("Starting recipe view test...")
        for name in view_recipe_names:
            recipe = get_recipe(name, recipes)
            recipe.view()
        print("Recipe view test completed.")
    
    start_update_test = input("Start update recipe test? y or n ")
    if start_update_test == "y":
        print("Starting update recipe test...")
        update_this_recipe = get_recipe(recipe_to_update, recipes)
        update_this_recipe.update(recipe_update_config)
        print("Update recipe test completed.")

        print("Starting update recipe test...")
        update_this_recipe = get_recipe("mocha", recipes)
        update_this_recipe.update(None)
        print("Update recipe test completed.")
        
        print("Starting update recipe test...")
        update_this_recipe = get_recipe(recipe_to_update2, recipes)
        update_this_recipe.update(recipe_update_config2)
        print("Update recipe test completed.")

    get_recipe(update_recipe_name. recipes).view()

    #Step 4: Delete a recipe
    
    
    print("Starting deletion test...")
    print("Deleting the following recipe...")
    recipe_to_delete = get_recipe(update_recipe_name, recipes).view()
    delete_this_recipe = get_recipe(update_recipe_name, recipes)
    delete_this_recipe.delete_one_recipe()
    deleted_recipe = get_recipe(update_recipe_name, recipes).view()