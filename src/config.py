from os import environ
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "CONNECTION_STRING": environ["CONNECTION_STRING"],
    "DATABASE_NAME": environ["DATABASE_NAME"],
    "RECIPE_COLLECTION_NAME": environ["RECIPE_COLLECTION_NAME"],
    "INGREDIENT_COLLECTION_NAME": environ["INGREDIENT_COLLECTION_NAME"],
    "TEST_DATABASE_NAME": environ["TEST_DATABASE_NAME"],
    "TEST_COLLECTION_NAME": environ["TEST_COLLECTION_NAME"],
    "RECIPE_FILEPATH": environ["RECIPE_FILEPATH"],
    "DIRECTIONS_FILEPATH": environ["DIRECTIONS_FILEPATH"]
    # "": environ[""],
    # "": environ[""]
}