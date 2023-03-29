from django import forms
from .models import Product, Category, Gender, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        genders = Gender.objects.all()
        brands = Brand.objects.all()
        friendly_names_category = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_gender = [(g.id, g.get_friendly_name()) for g in genders]
        friendly_names_brand = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = friendly_names_category
        self.fields['gender'].choices = friendly_names_gender
        self.fields['brand'].choices = friendly_names_brand
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
