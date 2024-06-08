from django.shortcuts import render
from recipes.utils import main


# Create your views here.

def home(request):
    
    return render(request, 'recipes/pages/home.html',
                  context={
                      'recipes': [main.make_recipe() for _ in range(10)],
                      
                  })
    # HTTP Response

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html',context={
        'recipe': main.make_recipe(),
        'is_detail_page': True
    })
    # HTTP Response
    