from django.test import TestCase
from django.urls import reverse
from ..models import Recipe, Category

class RecipeNewViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Soup")
        for i in range(7):
            Recipe.objects.create(title=f"Recipe {i}", category=self.category)