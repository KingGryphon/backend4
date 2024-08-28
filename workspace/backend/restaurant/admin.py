from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display= ('Title', 'Price', 'Inventory')
    search_fields= ('Title', 'Price', 'id', 'Inventory')

@admin.register(Booking)
class BookoingAdmin(admin.ModelAdmin):
    list_display= ('Name', 'No_of_guests', 'BookingDate')
    search_fields= ('id', 'Name', 'No_of_guests', 'BookingDate')