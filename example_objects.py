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

"""
Example Objects
"""

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