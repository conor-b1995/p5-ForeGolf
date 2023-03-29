from django.db import models


class Category(models.Model):
    """ Category model for each different category """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """ Meta class for category model """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Gender(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        """ Meta class for gender model """
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Products Model """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey('Gender', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    description = models.TextField()
    has_degrees = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    """ Brand model """
    name = models.CharField(max_length=100, null=False, unique=True, blank=False)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=False, unique=True, blank=False)
    description = models.TextField(max_length=2500, null=False, blank=False)

    class Meta:
        """ Meta class for Brand model """
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def __str__(self):
        """ String representation of Brand model """
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
