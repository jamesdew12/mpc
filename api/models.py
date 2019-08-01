from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=200)
    auth_token = models.CharField(max_length=20)

class Recipe(models.Model):
    # ingredients = models.ManyToManyField(Ingredient)
    name = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=200)
    vegan = models.BooleanField()
    def __str__(self):
        return self.name
