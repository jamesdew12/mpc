from django.urls import path

from .views import RecipeView


app_name = "api"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('recipe/', RecipeView.as_view()),
    path('ingredient/', RecipeView.as_view()),
    path('recipe/<int:id>/', RecipeView.as_view()),
]
