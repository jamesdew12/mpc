from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import User, Recipe, Ingredient
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer, UserSerializer, IngredientSerializer
from django.http import JsonResponse

class RecipeView(APIView):
    def get(self, request):
        recipes = Recipe.objects.order_by('likes')
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = RecipeSerializer(recipes, many=True)
        return Response({"recipes": serializer.data})
    def post(self, request):
        recipe = request.data.get('Recipe')
        # Create an recipe from the above data
        serializer = RecipeSerializer(data=recipe)
        if serializer.is_valid(raise_exception=True):
            recipe_saved = serializer.save()
        return Response({"success": "Recipe '{}' created successfully".format(recipe_saved.name)})
    def post(self, id):
        recipe = get_object_or_404(Recipe, pk=id)
        serializer = RecipeSerializer(recipe, partial=True)
        return Response({"You liked" :serializer.data})

class IngredientView(APIView):
    def post(self, request):
        ingredient = request.data.get('Ingredient')
        # Create an recipe from the above data
        serializer = IngredientSerializer(data=ingredient)
        if serializer.is_valid(raise_exception=True):
            ingredient_saved = serializer.save()
        return Response({"success": "Ingredient '{}' added successfully".format(ingredient_saved.name)})
