from sqlite3 import Timestamp
from tkinter import CASCADE
from unittest import skip
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    # All ingredients that are needed for all the dishes 
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return "/ingredients"
    
    def __str__(self):
        return f"""
        name={self.name};
        quantity={self.quantity};
        unit={self.unit};
        price_per_unit={self.price_per_unit}
        """
    
class MenuItem(models.Model):
    # Represent the menu of the restaurant
    dish_name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"dish_name={self.dish_name}; price={self.price}"

    def available(self):
        return all(ingredient.enough()for ingredient in self.reciperequirement_set.all())

class RecipeRequirement(models.Model):
    # Represents an ingredient required for a recipe for a Menuitem 
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"

    def get_absolute_url(self):
        return '/menu'
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; created_at={self.created_at}"

    def get_absolute_url(self):
        return "/purchases"