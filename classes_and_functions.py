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

        # Iterates through the dictionary of ingredients
        for ingredient, amount in self.ingredients.items():

            if isinstance(ingredient, Recipe):
                
                # Iterates through the ingredients of the Recipe object
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
        temp = []

        for ingredient, amount in self.ingredients.items():

            if isinstance(ingredient, Recipe):

                temp.append((ingredient, amount))

                for sub_ingredient in ingredient.non_atomic_materials:
                    
                    temp.append(sub_ingredient)

            else:
                pass       

        return temp

def compile_raw_ingredients(input_recipes: list) -> dict[str, int]:

    # Creates a list of all the ingredients from input_recipes including the ingredients of non-atomic elements
    ingredients_list = [ingredient for recipe in input_recipes for ingredient in recipe.raw_materials] 

    ingredients_dict = {}

    # Compiles all the ingredients into a dictionary
    for ingredient in ingredients_list:
        if ingredient[0] not in ingredients_dict:
            ingredients_dict[ingredient[0]] = ingredient[1]
        else:
            ingredients_dict[ingredient[0]] += ingredient[1]
    
    return ingredients_dict

# Compiles a list of non-atomic ingredients given an input list of recipes - Does not include any atomic ingredients
def compile_non_atomic_ingredients(input_recipes: list) -> dict[str, int]:

    # Generates a list of tuple(str, int) of all non-atomic ingredients derived from input_recipes
    ingredients_list = [ingredient for recipe in input_recipes for ingredient in recipe.non_atomic_materials]

    ingredients_dict = {}

    # Compiles all the ingredients into a dictionary
    for ingredient in ingredients_list:
        if ingredient[0].recipe_product not in ingredients_dict:
            ingredients_dict[ingredient[0].recipe_product] = ingredient[1]
        else:
            ingredients_dict[ingredient[0].recipe_product] += ingredient[1]
    
    return ingredients_dict
    

titanium_alloy = Recipe("Titanium Alloy", "Forge", {
    "Titanium Bar" : 1,
    "Foo Bar" : 3
})

handle = Recipe("Handle", "Workbench", {
    "Leather" : 4,
    titanium_alloy : 2,
    "Wood" : 3
})

blade = Recipe("Sword Blade", "Anvil", {
    "Steel" : 11,
    titanium_alloy : 7,

})

sword = Recipe("Sword", "Anvil", {
    blade : 1,
    handle : 1,
    "Love" : 1
})

dwarven_chestplate = Recipe("Dwarven Chestplate", "Anvil", {
    "Steel" : 10,
    "Elven Blood" : 5
})

# print(compile_raw_ingredients([sword, dwarven_chestplate]))
print(compile_non_atomic_ingredients([sword]))