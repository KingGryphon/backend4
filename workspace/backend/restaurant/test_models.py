from django.test import TestCase
from restaurant import models
from decimal import Decimal


class TestMenu(TestCase):
    def test_get_item(self):
        item=models.Menu.objects.create(Title="Ice Cream", Price=Decimal(80.00), Inventory=100, id=60)
        self.assertEqual(str(item), "Ice Cream : 80.00")

