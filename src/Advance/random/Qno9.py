"""
Qno9 - Random Recipe Generator
Difficult words:
- recipe: instructions to cook food
- collection: grouped items
"""

import random

recipes = [
    "Pasta Alfredo",
    "Vegetable Stir Fry",
    "Chicken Biryani",
    "Fruit Salad",
    "Grilled Sandwich",
]

print("Today's random recipe:", random.choice(recipes))
