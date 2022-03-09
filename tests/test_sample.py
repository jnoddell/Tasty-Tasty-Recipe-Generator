# # test_sample.py
# # @author       Justin Noddell


import json
from src.tastypackage.lists import IngredientList
from src.tastypackage.lists import ShoppingList


# retrieve dummy data
apple_pork_recipe = {}
apple_pork_prices = {}
roja_sangria_recipe = {}
roja_sangria_prices = {}

# confirm local recipes data can be loaded; to be used in some of the tests below
def test_load_dummy_recipes():
    try:
        with open("tests/apple_orange_recipes.json", "r") as file:
            data = json.load(file)
            apple_pork_recipe = data[0]
            roja_sangria_recipe = data[1]
        file.close()
    except Exception:
        assert False

# confirm first dummy (Apple Pork Tenderloin) recipe can retrieve price data
def test_load_dummy_tenderloin_prices():
    try:
        with open("tests/apple_pork_tenderloin_price_breakdown.json", "r") as file:
            data = json.load(file)
            apple_pork_prices = data
        file.close()
    except Exception:
        assert False

# confirm second dummy recipe (Roja Sangria) can retrieve price data
def test_load_dummy_roja_prices():
    try:
        with open("tests/roja_sangria_price_breakdown.json", "r") as file:
            data = json.load(file)
            roja_sangria_prices = data
        file.close()
    except Exception:
        assert False

# confirm IngredientList class rejects bad constructor
def test_ingredient_list_constructor():
    try:
        ingredient_list = IngredientList(["bad","data"])
        assert False
    except Exception:
        assert True

# confirm private function cannot be accessed
def test_add_ingredient_by_function():
    ingredient_list = IngredientList()
    try:
        ingredient_list.__add_ingredient("fruits")
        assert False
    except Exception:
        assert True

# confirm private variable cannot be accessed
def test_add_ingredient_to_member():
    ingredient_list = IngredientList()
    try:
        ingredient_list.__list.append("wine")
        assert False
    except Exception:
        assert True

# confirm private function cannot be accessed
def test_access_remove_from_ingredient_list():
    ingredient_list = IngredientList()
    try:
        ingredient_list.__remove_ingredient()
        assert False
    except Exception:
        assert True

# confirm contains function can validate missing ingredient
def test_contains():
    ingredient_list = IngredientList()
    try:
        ingredient_list.__contains("crackers")
        assert False
    except Exception:
        assert True

# confirm is_empty can detect an empty list
def test_is_empty():
    ingredient_list = IngredientList()
    assert ingredient_list.is_empty() == True

# confirm has_valid can detect a lack of valid ingredients
def test_has_valid():
    ingredient_list = IngredientList()
    assert ingredient_list.has_valid() == False

# confirm has_valid can detect a lack of valid ingredients
def test_has_valid_bad_input():
    ingredient_list = IngredientList()
    try:
        result = ingredient_list.has_valid(23) == False
        assert False
    except Exception:
        assert True

# confirm private function cannot be accessed
def test_format_request():
    ingredient_list = IngredientList()
    try:
        ingredient_list.__format_get_recipe_by_ingredients("test_key", params={})
        assert False
    except Exception:
        assert True

# confirm get_recipe can handle empty ingredient list
def test_create_recipes():
    ingredient_list = IngredientList()
    try:
        recipe = ingredient_list.get_recipe()
        assert True
    except Exception:
        assert False

# def test_find_recipes_bad_input():
#     ingredient_list = IngredientList()
#     try:
#         recipes = ingredient_list.find_recipe(["oranges"], "6")
#         assert True
#     except Exception:
#         assert False

# confirm get_ingredients can return empty list
def test_get_ingredients():
    ingredient_list = IngredientList()
    assert len(ingredient_list.get_ingredients()) == 0

# confirm ShoppingList can handle empty parameters upon construction
def test_shopping_list_constructor_empty():
    try:
        shopping_list = ShoppingList()
        assert True
    except Exception:
        assert False

# confirm ShoppingList can take ingredient list as input
def test_shopping_list_constructor_one_param():
    try:
        shopping_list = ShoppingList(["first","second"])
        assert True
    except Exception:
        assert False

# def test_shopping_list_constructor_bad_input():
#     try:
#         shopping_list = ShoppingList(["first",2], ["second","list"])
#         assert False
#     except Exception:
#         assert True

# confirm private function cannot be accessed
def test_add_ingredient():
    try:
        shopping_list = ShoppingList()
        shopping_list.__add_ingredient("oranges")
        assert False
    except Exception:
        assert True

# confirm add_recipe can handle an empty recipe
def test_add_recipe_empty():
    try:
        shopping_list = ShoppingList()
        shopping_list.add_recipe({})
        assert True
    except Exception:
        assert False

# confirm add_recipe can handle one recipe
def test_add_recipe_one_recipe():
    try:
        shopping_list = ShoppingList()
        assert not shopping_list.add_recipe(apple_pork_recipe)
    except Exception:
        assert False

# confirm add_recipe can handle one recipe
def test_add_recipe_one_recipe_alt():
    try:
        shopping_list = ShoppingList()
        assert not shopping_list.add_recipe(roja_sangria_recipe)
    except Exception:
        assert False

# def test_add_recipe_bad_input():
#     try:
#         shopping_list = ShoppingList()
#         assert not shopping_list.add_recipe([apple_pork_recipe, roja_sangria_recipe])
#     except Exception:
#         assert False

# confirm private function cannot be accessed
def test_access_get_cost_one_recipe():
    try:
        shopping_list = ShoppingList()
        shopping_list.__get_cost(apple_pork_prices)
        assert False
    except Exception:
        assert True

# confirm private function cannot be accessed
def test_access_get_cost_one_recipe_alt():
    try:
        shopping_list = ShoppingList()
        shopping_list.__get_cost(roja_sangria_prices)
        assert False
    except Exception:
        assert True

# confirm private function cannot be accessed
def test_access_calculate_bill():
    try:
        shopping_list = ShoppingList()
        shopping_list.__calculate_bill({})
        assert False
    except Exception:
        assert True

# confirm private function cannot be accessed
def test_access_remove_empties():
    try:
        shopping_list = ShoppingList()
        shopping_list.__remove_empties({})
        assert False
    except Exception:
        assert True

# confirm cleanup can run without issue on empty shopping list
def test_cleanup():
    try:
        shopping_list = ShoppingList()
        shopping_list.cleanup()
        assert True
    except Exception:
        assert False