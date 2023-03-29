from django.contrib import admin
from .models import Category, Product, Gender, Brand


# Register your models for the admin panel
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'brand',
        'gender',
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


class GenderAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'friendly_name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Brand, BrandAdmin)
