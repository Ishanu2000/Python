import json

#Represent a recipe with a name, ingredients, and instructions
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients  #List of ingredients
        self.instructions = instructions  #String with instructions

#Manage a recipe book
class RecipeBook:
    def __init__(self):
        self.recipes = {}  #Dictionary to store recipes with name as key

    #Add a recipe to the recipe book
    def add_recipe(self, recipe):
        if recipe.name in self.recipes:
            print(f"Recipe '{recipe.name}' already exists.")
        else:
            self.recipes[recipe.name] = recipe
            print(f"Recipe '{recipe.name}' added.")

    #Remove a recipe from the recipe book
    def remove_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe '{name}' removed.")
        else:
            print("Recipe not found.")

    #Search for a recipe by name
    def search_recipe(self, name):
        recipe = self.recipes.get(name)
        if recipe:
            print(f"\n----- Recipe for '{recipe.name}' -----")
            print("Ingredients:")
            for ingredient in recipe.ingredients:
                print(f"- {ingredient}")
            print("Instructions:")
            print(recipe.instructions)
        else:
            print("Recipe not found.")

    #Save all recipes to a JSON file
    def save_to_json(self, filename):
        try:
            with open(filename, 'w') as file:
                #Convert recipes to a JSON-compatible format
                json_data = {name: {"ingredients": recipe.ingredients, "instructions": recipe.instructions}
                             for name, recipe in self.recipes.items()}
                json.dump(json_data, file, indent=4)
            print(f"Recipes saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving to JSON: {e}")

    #Load recipes from a JSON file
    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.recipes = {name: Recipe(name, details["ingredients"], details["instructions"])
                                for name, details in data.items()}
            print(f"Recipes loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading from JSON: {e}")

#Example
#Create a RecipeBook instance
recipe_book = RecipeBook()

#Add recipes to the recipe book
recipe_book.add_recipe(Recipe("Milk Toffee", ["Sugar", "Milk", "Butter"], "Mix all ingredients and cook.\n"))
recipe_book.add_recipe(Recipe("Cake", ["Flour", "Sugar", "Butter", "Eggs"], "Mix all and Bake.\n"))

#Search for a recipe
recipe_book.search_recipe("Milk Toffee")

#Remove a recipe
recipe_book.remove_recipe("Cake")

#Display all recipes after removal
recipe_book.search_recipe("Cake")

#Save recipes to a JSON file
recipe_book.save_to_json("recipes.json")

#Load recipes from a JSON file
recipe_book.load_from_json("recipes.json")

#Display a loaded recipe
recipe_book.search_recipe("Pancakes")
