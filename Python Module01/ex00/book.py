""" Book class
"""
from datetime import datetime

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