from django.shortcuts import render
from .models import Recipe

def main_view(request):
    latest_recipes = Recipe.objects.order_by('-id')[:5] 
    context = {'recipes': latest_recipes}
    return render(request, 'main.html', context)