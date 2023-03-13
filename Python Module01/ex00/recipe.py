class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

        if not isinstance(self.name, str):
            raise ValueError("Name must be a string")
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl < 1 or self.cooking_lvl > 5:
            raise ValueError("Cooking level must be an integer")
        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            raise ValueError("Cooking time must be an integer")
        if not isinstance(self.ingredients, list):
            raise ValueError("Ingredients must be a list")
        if not isinstance(self.recipe_type, str) or self.recipe_type not in ("starter", "lunch", "dessert"):
            raise ValueError("Recipe type must be a string")
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")