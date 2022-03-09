# # start.py
# # @author   Justin Noddell


from src.tastypackage.lists import IngredientList
from src.tastypackage.lists import ShoppingList
import src.tastypackage.command_line_functions as CLI


# the purpose of this script is to generate the user's shopping list by order of completing the following steps:
#   0:      confirm internet & api are available, welcome user
#   1:      collect user ingredients
#   2:      generate and suggest recipes
#   3:      prepare and return the final version of the shopping list


# step 0: confirm internet and Spoonacular are available, greet user

ingredient_list = IngredientList()
if not ingredient_list.exists("apples"):
    
    print()
    CLI.api_error()
    CLI.pause()

else:

    CLI.greet_user()

    # step 1: collect ingredients 

    ingredient_list.print_guide()
    while ingredient_list.is_empty() or not ingredient_list.has_valid():
        
        ingredient_list.create()

        if ingredient_list.is_empty():

            print("Please enter at least one ingredient.\n")
        
        elif not ingredient_list.has_valid():

            print("Please enter at least one valid ingredient.\n")

    # step 2: suggest recipes

    shopping_list = ShoppingList(ingredient_list.get_ingredients())
    while True:

        # generate recipes to use, display to user
        recipe = ingredient_list.get_recipe()

        if recipe:

            shopping_list.print_recipe(recipe)

            # prompt requested-action to accept or reject
            if CLI.confirm("Do you like this recipe?"):

                successfully_added = shopping_list.add_recipe(recipe)

                # case: loss of internet
                if not successfully_added:

                    CLI.pause()
                    break

                shopping_list.cleanup()

            if CLI.confirm("Would you like to view your shopping list ingredients?"):

                shopping_list.print_basic()
                if CLI.confirm("Are you satisfied with this shopping list?"):

                    # step 3: prepare and return the final shopping list to the user

                    shopping_list.print_detailed()
                    CLI.pause()
                    break

        # case: API requests limit reached for current execution
        else:

            CLI.pause()
            break