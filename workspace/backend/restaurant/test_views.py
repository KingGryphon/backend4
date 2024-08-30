from django.test import TestCase
from decimal import Decimal
from .models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .serializers import MenuSerializer


class TestMenuView(TestCase):
    def setup(self):
        self.client=APIClient()
        Menu.objects.create(Title="Ice Cream", Price=Decimal('80.00', Inventory=100))
        Menu.objects.create(Title="Pizza", Price=Decimal('120.00'), Inventory=50)
        Menu.objects.create(Title='Burger', Price=Decimal('60.00'), Inventory=200)


    def test_getall(self):
        response=self.client.get(reverse('menu'))
        menus=Menu.objects.all()
        serializer=MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)