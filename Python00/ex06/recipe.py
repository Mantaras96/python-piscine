import sys

def print_recipe_names(cookbook):
    print("Recipe names")
    for name in cookbook:
        print (name)

def print_details(cookbook, name):
    print("Details {name}:".format(name = name))
    if name in cookbook:
        recipe = cookbook[name]
        print(f"Recipe for {name}:")
        print(f"Ingredients list: {', '.join(recipe['ingredients'])}")
        print(f"To be eaten for {recipe['meal']}.")
        print(f"Takes {recipe['prep_time']} minutes of cooking.")
    else:
        print(f"No recipe found with name {name}.")

def delete_recipe(cookbook, name):
    if name in cookbook:
        del cookbook[name]

def add_recipe(cookbook):
    recipe_name = input("Enter recipe name: ")
    ingredients = input("Enter comma-separated list of ingredients: ").split(",")
    meal_type = input("Enter meal type: ")
    prep_time = int(input("Enter preparation time (in minutes): "))

    recipe = {
        "ingredients": [ingredients],
        "meal": meal_type.strip(),
        "prep_time": prep_time
    }

    cookbook[recipe_name] = recipe
    print 

cookbook = {}

sandWich = {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
}

cookbook["sandwich"] = sandWich

cake = {
    "ingredients": ["flour", "sugar", "eggs"],
    "meal": "dessert",
    "prep_time": 60
}

cookbook["cake"] = cake

salad = {
    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
}

cookbook["salad"] = salad

#Empieza el programa
while 42: 
    print("\nWelcome to the cookbook!")
    print("Please choose an option:")
    print("1. Print all recipes")
    print("2. Print recipe details")
    print("3. Add a new recipe")
    print("4. Delete a recipe")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print_recipe_names(cookbook)
    elif choice == "2":
        recipe_name = input("Enter recipe name: ")
        print_details(cookbook, recipe_name)
    elif choice == "3":
        add_recipe(cookbook)
    elif choice == "4":
        recipe_name = input("Enter recipe name: ")
        delete_recipe(cookbook, recipe_name)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Error code. Please enter a number from 1 to 5.") 


    


