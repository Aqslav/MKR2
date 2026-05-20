from django.shortcuts import render
from .models import Recipe, Category
from django.db.models import Count


def main_view(request):
    latest_recipes = Recipe.objects.order_by('-id')[:5]
    context = {'recipes': latest_recipes}
    return render(request, 'main.html', context)


def category_list_view(request):
    categories_with_count = Category.objects.annotate(recipes_count=Count('categories'))
    context = {'categories': categories_with_count}
    return render(request, 'category_list.html', context)
