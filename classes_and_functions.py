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

    @property
    def non_atomic_materials(self) -> list[tuple[str, int,]]:
        non_atomic_materials = []

        # Iterates through the recipes until all non-atomic ingredients have been added to non_atomic_materials
        for ingredient, amount in self.ingredients.items():

            if isinstance(ingredient, Recipe):

                non_atomic_materials.append((ingredient, amount))

                for sub_ingredient in ingredient.non_atomic_materials:

                    sub_ingredient = list(sub_ingredient)
                    sub_ingredient[1] *= amount
                    non_atomic_materials.append(tuple(sub_ingredient))

            else:
                pass  

        return non_atomic_materials

def compile_raw_ingredients(input_recipes: list) -> dict[str, int]:

    # Creates a list of all the ingredients from input_recipes including the ingredients of non-atomic elements
    ingredients_list = [ingredient for recipe in input_recipes for ingredient in recipe.raw_materials] 

    ingredients_dict = {}

    # Compiles all the ingredients into a dictionary
    for ingredient in ingredients_list:
        ingredients_dict[ingredient[0]] = ingredients_dict.get(ingredient[0], 0) + ingredient[1]

    return ingredients_dict

# Compiles a list of non-atomic ingredients given an input list of recipes - Does not include any atomic ingredients
def compile_non_atomic_ingredients(input_recipes: list) -> dict[str, int]:

    # Generates a list of tuple(str, int) of all non-atomic ingredients derived from input_recipes
    ingredients_list = [ingredient for recipe in input_recipes for ingredient in recipe.non_atomic_materials]

    ingredients_dict = {}

    # Compiles all the ingredients into a dictionary
    for ingredient in ingredients_list:
        ingredients_dict[ingredient[0].recipe_product] = ingredients_dict.get(ingredient[0].recipe_product, 0) + ingredient[1]

    return ingredients_dict
    
"""
Example Recipe Objects for Testing
"""

infused_coal = Recipe("Infused Coal", "Oil Machine", {
    "Coal" : 2,
    "Lioren Oil" : 4
})

titanium_bar = Recipe("Titanium Bar", "Smelter", {
    "Titanium Ore" : 3,
    "Coal" : 2
})

foo_bar = Recipe("Foo Bar", "Smelter", {
    "Foo Ore" : 3,
    "Coal" : 2
})

titanium_foo_alloy = Recipe("Foo-Titanium Alloy", "Forge", {
    titanium_bar : 1,
    foo_bar : 2,
    "Coal" : 3
})

titanium_foo_blade = Recipe("Titanium-Foo Blade", "Forge", {
    titanium_foo_alloy : 9,
    titanium_bar : 5,
    infused_coal : 3
})

sturdy_handle = Recipe("Sturdy Handle", "Forge", {
    titanium_foo_alloy : 4,
    titanium_bar : 2,
    "Leather" : 3,
})

foo_sword = Recipe("Foo Sword", "Forge", {
    titanium_foo_blade : 1,
    sturdy_handle : 1,
    foo_bar : 19,
    infused_coal : 5,
    "Essence of Foo" : 11
})