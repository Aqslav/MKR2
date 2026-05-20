from django.urls import path
from .views import main_view, category_list_view

urlpatterns = [
    path('', main_view, name='main'),
    path('categories/', category_list_view, name='category_list'),
]
