from django.test import TestCase
from restaurant import models


class TestMenu(TestCase):
    def test_get_item(self):
        item=models.Menu.objects.create(Title="Ice cream", Price=80, Inventory=100, id=60)
        self.assertEqual(item, "Ice Cream : 80")

