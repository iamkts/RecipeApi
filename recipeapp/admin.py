# admin.py

from django.contrib import admin
from .models import Cuisine, MealType, Ingredient, Recipe, RecipeReview

admin.site.register(Cuisine)
admin.site.register(MealType)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeReview)
