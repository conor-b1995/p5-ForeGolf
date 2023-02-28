from django.contrib import admin
from .models import Category, Product


# Register your models for the admin panel
admin.site.register(Category)
admin.site.register(Product)
