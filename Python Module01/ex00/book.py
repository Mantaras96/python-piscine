""" Book class
"""
from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = self.last_update
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

        if not isinstance(self.name, str):
            raise ValueError("Name must be a string")
        if not isinstance(self.last_update, str):
            raise ValueError("Last update must be a string")
        if not isinstance(self.creation_date, str):
            raise ValueError("Creation date must be a string")
        if not isinstance(self.recipe_list, list):
            raise ValueError("Recipe list must be a list")
    
    def get_recipe_by_name(self, name):
        for recipe in self.recipe_list.values():
            for meal in recipe:
                if meal.name == name:
                    return meal
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipe_list.keys():
            return self.recipe_list[recipe_type]
        return None
    
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError("Recipe must be a Recipe object")
        self.recipe_list[recipe.recipe_type].append(recipe)
        