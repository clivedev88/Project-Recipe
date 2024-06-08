from django.contrib import admin
from django.urls import path
from recipes.views import home
from recipes.views import recipe

urlpatterns = [
        path('', home, name= 'recipes-home'), #Home
        path('recipes/<int:id>/', recipe, name='recipes-recipe'), #Home
       
]