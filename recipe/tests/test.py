from django.test import TestCase
from django.urls import reverse
from ..models import Recipe, Category

class RecipeNewViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Soup")
        for i in range(7):
            Recipe.objects.create(title=f"Recipe {i}", category=self.category)

    def test_main_view_returns_latest_five(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertEqual(len(response.context['recipes']), 5)

    def test_category_list_view_counts(self):
            response = self.client.get(reverse('category_list'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'category_list.html')
            categories_in_context = response.context['categories']
            test_category = categories_in_context.get(id=self.category.id)
            self.assertEqual(test_category.recipes_count, 7)