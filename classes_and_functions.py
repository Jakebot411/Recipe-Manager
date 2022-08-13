from example_objects import *

class Recipe:

    # Atomic means it's already a raw material
    # Non-Atomic means the recipe contains another recipe
    def __init__(self, recipe_product: str, method_of_crafting: str, ingredients : dict):

        self.recipe_product = recipe_product
        self.method_of_crafting = method_of_crafting
        self.ingredients = ingredients

    @property
    def raw_materials(self) -> list[tuple[str, int]]:
        raw_materials = []

        for ingredient, amount in self.ingredients.items():

            if isinstance(ingredient, Recipe):

                for sub_ingredient in ingredient.raw_materials:
                    
                    # Corrects for the amount of non-atomic ingredients in a recipe
                    sub_ingredient = list(sub_ingredient)
                    sub_ingredient[1] *= amount
                    raw_materials.append(tuple(sub_ingredient))
            
            else:
                raw_materials.append((ingredient, amount))

        return raw_materials

def compile_ingredients(input_recipes: list) -> dict[str, int]:

    # Creates a list of all the ingredients from input_recipes including non-atomic ingredients
    ingredients_list = [ingredient for recipe in input_recipes for ingredient in recipe.raw_materials] 

    ingredients_dict = {}

    # Compiles all the ingredients into a dictionary
    for ingredient in ingredients_list:
        if ingredient[0] not in ingredients_dict:
            ingredients_dict[ingredient[0]] = ingredient[1]
        else:
            ingredients_dict[ingredient[0]] += ingredient[1]
    
    return ingredients_dict