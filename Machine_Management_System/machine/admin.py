from django.contrib import admin
from .models import Laptop


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'comment','status']
