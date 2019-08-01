from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Recipe, User, Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'likes',
        ]

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'name',
        ]

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'auth_token',
        ]
