from django.contrib import admin
from .models import Category, Product


# Register your models for the admin panel
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'sku',
        'price',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
