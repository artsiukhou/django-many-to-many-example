from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientInRecipe",
        through_fields=("recipe", "ingredient"),
    )


class IngredientInRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField()
